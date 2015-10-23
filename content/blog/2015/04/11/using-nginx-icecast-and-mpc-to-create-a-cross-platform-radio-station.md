Title: Using nginx, Icecast and MPC to create a cross-platform radio station
Category: Blog
Date: 2015-04-01
Summary: How I setup my Poddle server to handle live broadcasts with an off-air fallback stream, in a manner that works on desktop and mobile.

## What is Poddle?

[Poddle is my podcasting network](https://poddle.io/). I want it to look, feel and work awesome...ly? Anyway, I'm proud of what we've built so far and want to continue to make a platform that people can enjoy being a part of, and that feels frictionless to interact with.

Hence I spend too much time setting things up and hosting them myself so that I can control the user experience. But hey-ho, here we go.

## Icecast

I've used Icecast since my first live show, [The 2014 Show](https://poddle.io/2014/) last year. I hooked up the server, got the [Nicecast](https://www.rogueamoeba.com/nicecast/) app for Mac for broadcast and used [jPlayer](http://jplayer.org) to handle playback on the desktop. For mobile I hooked up with [TuneIn](http://tunein.com/).

All worked fine until I started to want to host video podcasts (not even considering the live aspect). I wanted a player that would work well, looked good and was again cross-platform. jPlayer's OK but I really like [VideoJS](http://www.videojs.com) as a nice, out-of-the-box sexy player.

What's great about VideoJS is that it supports RTMP, which for me means that if someone wants to watch 5 seconds of a half-hour video, they haven't had to download more than they've watched, as the video is streamed (not progressively-downloaded).

I hooked that up by installing a specific version of nginx, which comes bundled with the necessary RTMP module.

I do it via Ansible, but basically it's a matter of downloading the [nginx source](http://nginx.org/download/nginx-1.5.2.tar.gz) and the [RTMP module source](https://github.com/arut/nginx-rtmp-module/archive/master.zip), and running this to compile them:

    ./configure --with-http_ssl_module --add-module=./nginx-rtmp-module-master && make && make install

I then deploy my custom nginx script which has all the settings I need (they're very simple, and I'll go thorugh the audio ones in a bit).

nginx is then installed at `/usr/local/nginx/sbin/nginx` and you can stop it by adding `-s stop` to the end of that command.

### But what about Icecast?

I'm on Ubuntu, so I can just run `apt-get install icecast2` to install the Icecast server (or set it up via Ansible as I have). I then have a config that looks like this:

```xml
<icecast>
	...
    <hostname>clover.cloud.steadman.io</hostname>
    <listen-socket>
        <port>8100</port>
    </listen-socket>
    <fileserve>1</fileserve>
    ...

    <mount>
        <mount-name>/stream</mount-name>
        <fallback-mount>/onair</fallback-mount>
        <fallback-override>1</fallback-override>
        <hidden>0</hidden>
        <public>1</public>
    </mount>

    <mount>
        <mount-name>/onair</mount-name>
        <password>...</password>
        <bitrate>96</bitrate>
        <type>audio/mp3</type>
        <subtype>mp3</subtype>
        <fallback-mount>/offair</fallback-mount>
        <fallback-override>1</fallback-override>
        <hidden>0</hidden>
    </mount>

    <mount>
        <mount-name>/offair</mount-name>
        <password>...</password>
        <dump-file>/tmp/dump-offair.mp3</dump-file>
        <bitrate>96</bitrate>
        <type>audio/mp3</type>
        <subtype>mp3</subtype>
    </mount>
	...
    <security>
        <chroot>0</chroot>
    </security>
</icecast>
```

That's not exhaustive, but you should be able to mix and match with your own config. I also needed this 'defaults' file in `/etc/default/icecast2`

    CONFIGFILE="/etc/icecast2/icecast.xml"
    USERID=icecast2
    GROUPID=icecast
    ENABLE=true

When I broadcast via Nicecast, I connect to the `/onair` mount. My players - including TuneIn - are set to use the `/stream` mount. When there's nothing being broadcast live, the `/offair` mount takes over, so `/stream` plays a selection of random archival content. But how?

## MPC and MPD

MPD ([Music Player Daemon](http://www.musicpd.org)) is an insanely convenient package. If I remember rightly, `mpd` is the player and `mpc` is the controller that you use to tell `mpd` what to play. Both are available by those names in the Ubuntu package repos, so it's super easy to install. My MPD config file looks like this:

    music_directory	"/path/to/podcast/episodes"

    ...

    user "mpd"
    bind_to_address "localhost"

    audio_output {
        type "shout"
        encoding "ogg"
        name "Off-air"
    	host "clover.cloud.steadman.io"
    	port "8100"
        mount "/offair"
        password ...
        bitrate "96"
        format "44100:16:1"
        protocol "icecast2"
        user "source"
        description	"Currently off-air"
    }

I'm not entirely sure why MPD needs to output Ogg, but I'm sure I tried it with MP3 and had no luck (at that time I may not have had the right encoder setup, but the whole system works as is).

I then have a series of commands which clear the playback queue (`mpc clear`), then add my media back into it (`mpc add /`), turn on shuffle (`mpc random on`) and repeat (`mpc repeat on`), and hit play (`mpc play`).

Instead of playing the music out through speakers - which don't exist becuase this is a virtual box - it plays out via Icecast. It needs broadcast permission, which you grant by giving it the right username and password.

### Niggle

The one thing that I've not been able to get to work is automatically switching from off-air to on-air, without having to reload the page or restart the stream via the app. It works the other way round (falling back from on-air to off-air), but all the docs that refer to "automatic" switching are really just talking about getting the thing to play the on-air stream when a new listener connects or resets a pre-existing connection.

### Back to nginx

So now I've got a radio station that works via Icecast, but I want that to be playable on the web as well as mobile. I also want to use VideoJS (which I also use to play my audio-only podcasts, because it's awesome and can do that).

This is achieved by rebroadcasting the Icecast MP3 feed as RTMP (Flash), and to do it I need [ffmpeg](https://www.ffmpeg.org).

## ffmpeg

Many of my projects use ffmpeg, and I have a really nifty set of Ansible tasks that install it on my boxes. It probably comes with a bunch of stuff I don't need, but because I use the same script on other sites that need more flexibility in terms of what users upload, I tend to leave well-enough alone.

Once ffmpeg is installed, the next job is telling nginx - with the RTMP module - how to pipe Icecast content through. This took me a lot of faff, and I'm not entirely sure what I did to get it working, but here's the part of the nginx config that matters:

    rtmp {
        server {
            listen 1935;
            chunk_size 4096;

            application radio {
                live on;
                meta off;
                exec_pull /usr/local/bin/ffmpeg -i http://localhost:8100/stream -f flv rtmp://localhost/radio/stream;
            }
        }
    }

Very simply, it uses `exec_pull`, a command native to the nginx RTMP module, to stream content from Icecast, pipe it through ffmpeg and output it to a special URL. The URL has to start with `http://[server][app-name]/`, where `[app-name]` in this case is `radio`.

I think some of the problem ended up being the domain name I was using. Before I was using the fully-qualified domain name of the server (I'm not quite sure why), but changing that to `localhost` and omitting all of the advised conversion options stopped my VLC player - which I was using for testing - from generating unhelpful errors about not being able to play the `undf` format (meaning "I don't know what this is, but it looks like nothing so I can't play it").

The last little wrinkle was using the newest version of VideoJS, but crucially - and this is something I couldn't find anywhere else - **using your own version of the SWF**.

When you're playing Flash content, VideoJS falls back to an SWF (Shockwave file). If you don't tell it where to look, it'll use its own hosted version. That then means your stremaing audio won't work, probably because of some weird cross-domain thing. However, using the latest version of VideoJS and specifying the version of the SWF that was on my machine (which is done when initialising the VideoJS player in JavaScript) did the trick.

## Next steps?

If I got super clever I could look into how to relay my Icecast stream into HLS, so mobile listeners could hear the station without using an app. HLS is basically a series of tiny MP3s that are stitched together and played seamlessly, so it shouldn't be rocket science, and apparently is doable via the RTMP module. But right now I'm not brave enough to try.

## Disclaimer

The above isn't meant as a technical or how-to guide, as I'm absolutely not qualified enough. I'm a run-of-the-mill, mediocre hacker who knows enough of what he knows to get his creative projects running. If I can be of help, you can [find me on Twitter](https://twitter.com/iamsteadman/) and I'll happily try and answer a question about my setup, but if you try it and my advice causes your hardware to blow up, your software to recompile itself backwards or your face to melt off, firstly I'm really sorry about all those awful things happening to you, and secondly, er, what's that over there? _*runs away quickly*_

## Why do all this?

I'm not entirely sure, but I have the idea of Poddle being as friction-free for listeners as possible. I think to a degree this goes against the spit-and-sawdust mentality of the web that many older podcasters grew up using, and still use to this day.

But I run the technical side of a [design-focused web agency](http://substrakt.co.uk/), so I care about user experience. I'd rather spend ages figuring out how to get something installed and running on a server than have an ugly, clunky button on my website that makes the radio happen.

Plus, this shit makes me feel proud. It's nice to achieve something techie, even if it's largely by copying, pasting, searing and Googling.
