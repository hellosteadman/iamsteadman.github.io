Title: Keep calm and clean all the things
Category: Blog
Date: 2013-07-03
Tags: appcelerator, titanium, javascript
Summary: How I dealt with one of many blindsiding Appcelerator Titanium bugs

I struggled for about three hours today, trying to build and distribute a
Titanium project for testing. The project built and uploaded to [HockeyApp](http://hockeyapp.net/) (the distribution platform we use at [Substrakt](http://substrakt.co.uk/)) fine, but failed to install on every
device I tried, every time.

Incorrectly and unfairly I railed at @[hockeyapp](http://twitter.com/hockeyapp/)
over Twitter, mainly because I needed someone to shout at, and as the last link
in the chain they were the most visible.

I also tried more practical things, like deleting all the iOS certificates and
provisioning profiles from my machine and the iOS portal, then recreating and
downloading them. Still no luck. I tried the old trick of creating a new
Titanium project and moving the old resources into it; no device. I plugged in a
couple of iPhones and tried copying the app via Xcode, and got the unhelpful
message:

> A signed resource has been added, modified, or deleted

A quick Google around the issue turned up basically the same process I'd gone
through, until I came across a [helpful StackOverflow answer](http://stackoverflow.com/questions/1715253/adhoc-app-installation-failed-in-iphone-why/3179617#3179617), which clued me into the problem.

My hard drive is formatted for the Windows FAT system, which on a Mac means the
operating system creates a bunch of unnecessary hidden files. These get compiled
into the app and cause problems, and it looks like the same might also be true
of Subversion (.svn) directories. So a quick run-through with the digital vacuum
cleaner (via the following script) and the removal of all the .svn directories
(and a final nail in the coffin that makes me think it's time to completely haul
ass over to Git), followed by a rebuild made everything fine again.

```sh
find . -name '._*' -exec rm -v {} \;
```

So this serves as a reminder to me and anyone else in a similar boat. If the app won't install, keep calm and `./clean`.
