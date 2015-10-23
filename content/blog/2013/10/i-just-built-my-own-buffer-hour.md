Title: I just built my own Buffer in an hour
Date: 2013-10-19
Category: Blog
Summary: How I built an alternative to Buffer using Django
Tags: django, buffer

Quick disclaimer: I really like [Buffer](https://bufferapp.com/); I think it's a
great service and I like the people behind it, so the title is kind of
tongue-in-cheek and in no way connotes that I think Buffer can be replicated in
next to no time. Everyone I've dealt with there, either over email or in person
has been great, so I hope this doesn't piss anyone off.

I'm starting to get the hang of this social malarky so I've been adding a lot of
stuff to it. It really makes a difference, peppering in the interesting links I
find with shout-outs to friends' achievements and contributions.

But I'm now starting to hit the ceiling of what my free account can hold, and
personally [the "Awesome" plan](https://bufferapp.com/awesome) is a little too
expensive for my taste. I totally see the value, but I feel if I can replicate
enough of what I need it to do myself, I'd be silly not to put my skills to
use. So I knocked up a cheap-ass equivalent in an hour or so. I'm not sharing
the code because it's not fair on the Buffer guys to tout my inferior system as
some kind of real-life equivalent, but here's the gist.

### The backend

I already have a bunch of models for handling my social feeds, so they can be
displayed on my [Live page](http://steadman.io/live/). A couple of the
"providers" I've written can also post stuff, so I didn't have to do much work
in that department.

Also, the [Bambu Tools](https://github.com/iamsteadman/bambu-tools/) package I
put together gives me a basic, pluggable cron system, and in order to get posts
that didn't look like they were mechanically shat out on the hour, I set the
interval to 57 minutes.

The job looks for the latest, unposted item, and posts it to the feeds it was
meant for (this way I can send some stuff to a personal Twitter account, some
    other stuff to a Facebook account or a work Twitter profile, etc). Once it's
    done, the cron job won't run for another 57 minutes so if the very first
    post goes out at 1pm, the next one goes at 1:57pm and the next at 2:54pm,
    and so on.

The titles are limited to 117 characters, so they'll fit alongside a shortened
URL in a tweet (with a space in-between). The URL is shortened with a service
also provided by Bambu Tools - in this case, [bit.ly](https://bitly.com/) \- and
when it's sent, it's marked with a date so it doesn't get picked up again. (For
    this kind of stuff, I prefer using dates rather than booleans as it can be
    useful to know _when_ something's happened, not just that it _has_
    happened.)

And that's it really. Very simple, mostly all using existing bits of code I have
lying around. Like I've said, it's nowhere near as sophisticated as Buffer.
Because it's automated, it's not yet going to care whether it's the middle of
the night; it'll still post away if there's something to post. But - and I
haven't yet given it a thorough testing - it appears to work.

### The frontend

But how stuff is added to this "buffer" (I've called it a "dropfeed" as I liked
the idea of a drip-feed but don't like the term "drip") is the kicker. Buffer is
catching on more and more, so developers are including it as standard in more
apps. Obviously that's not a luxury I have, but as long as I'm at my desk, I've
got a handy bookmarklet that'll do most of the legwork for me. This I _can_ show
you, 'cos it's useful to know that you can make these yourself without too much
bother, even if you're a copy-and-paste ninja:

```javascript
javascript:window.open('<url>/?_popup=true&url=' + escape(window.location), 'dropfeed', 'width=800,height=291');
```

This is a standard bookmark, but instead of pointing to a webpage, it points to
a small piece of JavaScript, that opens a window at a given URL (which Django
    provides). You're supposed to name the windows you create so that you can
    target them, so I've called mine `dropfeed` and I've set the parameters for
    that window (you can set other parameters, but I've found that Chrome
    ignores them). The `<url>` part I've left out just to discourage web
    sniffers from trying their hand, even though it's obviously behind a
username and password. The `_popup` URL parameter, along with the ability to set
the form's properties using the querystring are already provided by Django's
wonderful admin system.

The only inelegant thing at the moment is that once I've hit Save, the window
doesn't automatically close because it's expecting to find a parent window
pointing to a Django admin form. But I can live with that.

### The next step

I'd thought about using one of those nice email-to-URL services that can read
emails and let you parse them. This would let me email a link from myself, as
almost all of the kinds of apps I use have some sort of email facility. But
that's a job for another day, if I ever feel the burning need.

### Why bother?

I'm a developer. Most of what goes into my site is either about doing stuff to
show my skills - a designer's skills can be seen on-screen; developers don't
quite have that luxury - or just because I thought it'd be fun. I have a thing
in my sidebar which shows the events I'm going to, not because I expect people
to flock to me but because I thought I could write that very simply and hook it
up to a public Google Calendar. Often the challenge is the reason, so when the
idea came to me to build a cheap Buffer knock-off for myself, it seemed a good
use of a little spare time.

So there :)
