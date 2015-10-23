Title: Finally doing Django right after all these years
Date: 2014-05-24
Category: Blog
Summary: Details of my new Django setup on DigitalOcean
Tags: django, digitalocean, postgresql, nginx, virtualenv

I first start making websites with some idea of professionalism in 2001. I was
an old-school aSP then .NET guy up until a friend convinced me to use Django. In
2008 I picked it up, and until recently have used MySQL and Apache.

**And I don't feel guilty about that.**

If a nerd tells you they can't be every bit as hipstery as anyone else, get them
over to a developer conference. So many people sneer at MySQL as a database
backend (I think, because it's used by PHP which isn't a sophisticated language,
but is very portable and extremely flexible). I used it because it's what I
knew, and since I was diving into two things I'd never used before (Django and
Python) I wanted some sense of familiarity. 

I used Apache becuase it was, at the time the recommended server. But that was
nearly 6 years ago, and a lot's changed.

I do think there's an element of snobbery in many developers' choice of
technology. They like what's new, what other developers they like ar eusing, and
what has a good buzz about it. I always swim the other way, but that doesn't
mean I'm blind to the benefits that these frameworks and apps' users extole.

So why the change?

Well, I saw an ad on Twitter for [Digital Ocean](https://www.digitalocean.com/).
They run SSD on all their virtual boxes so I went, had a look and spun up two
cheap servers, one for logic, the other for the database. This, I told myself,
was my chance to setup the perfect Django environment, and finally learn what
all the fuss was about.

## virtualenv

virtualenv is a Python package that basically installs a version of \Python in a
given directory with its own separate world. It comes with a package installer
and the packages you choose are only valid inside that environment. The benefit
here is that if one sites needs version Django 1.4 and another needs Django 1.6,
and there's something that makes those two sites incompatible (like a
third-party library that only works on one of those versions and not the other),
both sites have their own separate version of Django.

If it sounds overkill, it isn't. We're not talking massive files, and the setup
doesn't take very long. And crucially it'll save you time in the long-run.

So, following
[instructions from Digital Ocean](https://www.digitalocean.com/community/articles/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn),
I went about setting up an environment for [Poddle.fm](http://poddle.fm/), my
podcasting network.

## PostgreSQL

In truth I think PostgreSQL has been recommended since I started using Django,
but support for MySQL feels like more of an afterthought now, as frankly
PostgreSQL is growing and improving, and MySQL, sort of, isn't.

I don't know nearly enough about PostgreSQL other than having installed it on
the second box and hooked up both machines to talk to each-other. I don't have a
way to browse the databases other than to use the command-line interface, and
I'm not familiar with PostgreSQL's non-standard form of SQL.

I used to think that Django's ORM could only go so far before you'd have to
start writing custom SQL, but it turns out that there are some functions that
only work within PostgreSQL and reduce the need for raw SQL. We'll see how far
that extends though, as I've only migrated two projects that needed database
access.

So far though, I haven't had to worry about timezone data (a problem with MySQL)
or fiddle with the settings too much. We'll see what happens when things start
to break, further down the line... :)

(Not that I'm suggesting a problem with PostgreSQL, but with my understanding of
it.)

## Gunicorn and Nginx

This is where things get a little nottier, for me. I'd played with PostgreSQL
before but never really touched Gunicorn (pronounced "_g-unicorn_" I think) and
was frankly a little afraid of Nginx ("_engine x_"). Within Apache, you install
a handler that passes all requests directly through to a script that spins up an
instance of your Django environment and gets running. Apache is big and heavy
and runs in the background constantly, with lots of different processes taking
up memory that can sit around for a good while.

My understanding - which is probably worng - is that Nginx doesn't work in the
same way. You don't pass requests to an application, instead you proxy from one
server to another. Gunicorn is a server for Python applications that sits on a
hidden port (8000, for example) and takes requests from Nginx. Presumably you
could actually tell Gunicorn to use port 80 if you gave it the permissions, but
that'd stop you from serving any other sites from the same server.

The big change for me involves thinking of each website as a UNIX process, that
sits in the background and has to be spun-up again if it fails. I manage that
with the bundled Upstart application for Ubuntu, but there are lots of other
methods of doing that, and monitoring processes to spin then back up again if
they fall over. But I thought "let's not run before we can walk, eh?"

So basically you create an Upstart configuration file for each site, start the
process running and then leave it. If you ever have to reboot the machine, the
processes should just start up again, along with Nginx.

From what I understand, the benefits are in speed, processing power and memory
savings, as you're using tools defined specifically for those tasks, rather than
all-purpose machines like the Apache web server.

## Bower

When I first saw [Bower](http://bower.co/), I couldn't quite understand the
need. Why couldn't you just go and download what you needed - just the minified
JavaScript or CSS file - and copy it to your app? Honestly there's absolutely no
reason why not. But as I'm developing Django apps (as in "plugins" for Django)
that would normally bundle third-party things in (like Tiwtter's own Bootstrap
framework), it made sense to let something else take care of that process,
rather than me having to bundle in the latest copy of a framework or update my
package every time a new release came out.

So the three projects I've moved over to Digital Ocean now all use Bower to
handle third-party components like jQuery, ZeroClipboard and of course
Bootstrap.

But in order to get this running, I needed Node.js, and I liked ghe idea of
having a separate copy of Node, NPM and Bower for each site, just like my Python
virtualenv setup.
[Calvin Cheng to the rescue](http://calvinx.com/2013/07/11/python-virtualenv-with-node-environment-via-nodeenv/),
with a simple solution, [nodeenv](https://github.com/ekalinin/nodeenv) by Eugene
Kalinin.

## Storage

This is the only remaining piece of the puzzle I don't have a setup for.
Currently all my uploaded media (podcasts, images for blog posts etc) sit in a
directory called /opt/media/, with each site having a separate subdirectory. I
did that, rather than install them individually into their own respective
environment directories because at some point I'll want to switch to a CDN or
similar, and one of the simplest ways of making that work is via an NFS-enabled
provider, so effectively /opt/media/ just because a shortcut to a cloud account
(although I read that's not necessarily good practice).

Either way though, keeping the /ope/media/ directory separate from /opt/env
(where the logic sits) will make the decoupling a little easier I hope. I'm
waiting to hear back from Nimbus.io to see if I can get in on their cloud
hosting platform, as I can't use AWS for... reasons.

## The second box

I decided to get my money's worth out of my database box and use that as a
[Sentry](http://sentry.readthedocs.org/en/latest/) and
[Elasticsearch](http://www.elasticsearch.org/) server.

Sentry, if you don't know is an amazing error-reporting tool that began its life
with Disqus. They're Django users so they built it to monitor Django apps and
intercept errors, logging them and allowing you to reproduce them as well as see
the full stack and bits of sourcecode that generated the errors. Now it supports
lots of differentr languages and frameworks, and I can't recommend it highly
enough.

Elasticsearch is, for me interchangeable with lots of other search engines, as I
only pick those supported by [Haystack](http://haystacksearch.org/). Haystack
does for Django what its own ORM does for databases. You write a Haystack index,
and Haystack converts it into an index readable by whatever provider you want to
use (an over-simplification obviously). I've mostly only used file-based engines
like Xapian and Whoosh, but thought, since I was trying to Do Things Right I
should look into a slightly more powerful, and potentially more efficient
engine. And although Java is horrible - sorry, that might be my own inner
snobbery coming out - it seemed preferable to Solr, which I've used before and
found pretty bloaty.

Again though, both were easy setups on client and server side, thanks in no
small part to good documentation.

## Cloudflare

I was using Cloudflare before, just to take a little strain off my old servers,
but even with it enabeld and pointing to the new server I can see the difference
in speed.

## Conclusion

Honestly, the only headaches I've had have been in converting my big Django
toolset into separate packages and changing the namespaces, then going through
and sorting all the Bower references out. And that's got nothing to do with the
new setup, that was just something I've been doing alongside this.

I had a minor moment of confusion last week when I couldn't get Django to allow
me to upload files larger than 100mb, but it turned out that in that particular
project, I'd set an arbitrary limit and had completely forgotten. (I still had
to change the Nginx config, but the reason it wouldn't work for the next quarter
of an hour is because I'm a dick, not becuase Nginx was ignoring me.)

I'm still using MySQL and Apache in some major production projects and moving
those over will not be a simple task, but I do see the benefit. Also, there's
nothing wrong with trying to write better code to work on older kit, as it'll
make it purr along on a more modern setup. That's just good practice.

All in all it feels good to not only write code I can be proud of, but to run it
in a way that doesn't make me blush. I'm not a sysadmin; I'm not a talented
Django dev. What I'm good at is getting up-to-speed on enough to make good
stuff. I'll never know the internals of half the things I use and will run
straight to Google when they break, but I do understand the value of a good,
solid setup.

So, three down, three more sites to move...
