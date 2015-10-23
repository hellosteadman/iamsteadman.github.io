Title: Meet Aster, Bluebell, Clover and Dahlia
Category: blog
Date: 2014-08-10
Summary: Continuing my DigitalOcean adventure
Tags: django, digitalocean, postgresql, nginx

In May I wrote about finally
"[doing Django right](/blog/2014/05/24/finally-doing-django-right-after-all-these-years/)", but the missing piece was revealed to me by my Substrakt colleague [Max Woolf](http://maxehmookau.github.io/), who clued me into using [Ansible](http://www.ansible.com/home) for development, provisioning and
deployment.

With this in mind I decided to rejig my setup a little, and move all of my major
projects onto their own servers. So now, I have

  * Aster, where this blog lives
  * Bluebell, which is on [Sentry](https://getsentry.com/welcome/) duty
  * Clover, which hosts [Poddle](http://poddle.io/)
  * Dahlia, where [My Next Hack](http://mynexthack.com/) can be found

For the moment this has meant that a couple of projects are homeless:

  * [What's My Lat-Lon](/play/whats-my-lat-lon/) \- This could be hosted
  anywhere, I just haven't felt a burning need to get it up onto Aster yet
  * [Quickdraw](/play/quickdraw/) \- This was a fun project, but basically only
  inhabited by spammers and something I might roll into Poddle

Digital Ocean lets me scale things up and down as I need to, and now due to this product-led setup I've got a good handle on what resources are being used where.

It's not everyone's ideal setup, as many would prefer to keep code, database and
media separate, but for the moment I like this neat approach to devops.

You'll probably have noticed that all my servers are named after flowers. I like
to stick to a naming convention when creating a server setup, and these names
are pretty. When I was with Bytemark I was using cheese names, because I'm a
silly person, and when I used Amazon they were named after characters from
[Stieg Larsson's Millennium trilogy](http://en.wikipedia.org/wiki/Millennium_series).

Poddle will at some point outgrow Clover (in space requirements if nothing
    else), but I'm hoping by then, Digital Ocean will have a handle on
    expandable storage.

So there you go. Clean setup, easy deployment, happy Steadman.
