Title: Sentry and Virtualenv
Date: 2013-06-02
Category: Blog
Summary: My first adventure with Virtualenv
Tags: virtualenv

This weekend I had my first real dalliance with Virtualenv, the system that
basically allows you to run different versions of Python modules for different
environments (ie: different websites). Some people like to go a bit overboard
and think that you should have a virtualenv for each website. I think this is
overkill and not sensibly maintainable, but then I base a lot of my decisions on
the fact that I have to be a Jack of all trades, not solely a developer or a
system admin.

Anyway, I'd never needed them so I've never used them, until this weekend when I
tried to get Sentry working on a server running Django 1.5. For whatever reason,
Sentry's requirements are at the moment frozen at 1.4, so I did what the guide
suggested and installed Virtualenv plus Sentry. Which then overwrote my Django installation. But hang on, isn't it not supposed to do that?

To which the answer is "yes, unless you specifically state the environment you
want your package installed into". I use
[PIP](https://pypi.python.org/pypi/pip), so I needed to add an `-E` argument
followed by the directory of my Sentry environment. Once done, I needed MySQL
installed in the same environment. I'd previously installed the Python MySQL
wrapper via Ubuntu's package manager, but that wouldn't work for my virtualenv
so I downloaded a package that would give me access to the `mysql_config`
program Python needed, then built the MySQL module from source. Pretty easy
really.

Once done I had a fully-working installation of Sentry. But I'd been here
before, only a few days ago, except without virtualenv. Every time I sent a test
message to Sentry, the client (the site sending the message) would time out.
Every friggin' time. And it wasn't until a few hours ago that I thought "Oh hang
on, I've not installed sendmail". Suffice it to say, that sorted all my
problems, and I'm an idiot for the second time this weekend (I can't remember
what Saturday's one was).

I often find myself frustrated when everyone else seems to think that something
works, when it clearly doesn't. Usually this is because of a small piece of
knowledge _everyone else_ takes for granted. That's not a slam, but it is a fact
of the Internet, so hopefully this post will serve as a friendly note to anyone
who's having difficulties. If you're dealing with a virtual environment, you've
activated it (via the `source` command or similar) but your packages don't seem
to install into that environment, check whatever system you're installing that
it knows which environment you want.

  * If using `python setup.py install`, make sure you've activated the
  environment so that the `python` binary you're referring to is the virtualised
  one.
  * If you're using `pip`, make sure to specify `-E /path/to/env` at the end of
  the command, because PIP is a system-wide command and it doesn't automatically
  recognise that you're in a specific virtualenv, so by default it'll put its
  packages in the "global" `dist-packages` directory (or equivalent).

Happy coding!
