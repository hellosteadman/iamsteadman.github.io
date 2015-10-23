Title: Do we need another grid framework?
Date: 2012-01-17
Tags: bootstrap, html, css
Category: Blog
Summary: My initial thoughts on Twitter's Bootstrap CSS framework

I've just been taking a look at
[Boostrap](http://twitter.github.com/bootstrap/), a CSS framework developed by
the folks at Twitter. The examples look lovely: crisp, clean and well thought
out, but it's unfortunately yet another non-semantic CSS framework that relies
on setting class names that have everything to do with appearance, and nothing
to do with content.

We're moving into a world of responsive design, where the same web pages can be
taken from desktop to tablet to mobile, with the user of each device getting an
optimised version of the same content. So setting a grid system means every
device gets the same content with the same layout. Does a mobile with a
320px-wide screen really need a web page 960 pixels wide?

The team have tried to nod towards this by adding in a perfunctory, albeit more
semantic "fluid layout", but that's not what responsive design is about. It's
not simply a matter of squashing columns together; in many cases it's about
removing columns or stacking them like rows.

[meegloo.com](http://meegloo.com/), although being very far from perfect, makes
good headway with a responsive stylesheet. and has so far meant no need for a
specific mobile stylesheet or dedicated site. There's still more work that needs
to be done, but it's infinitely easier to make small changes to a long
stylesheet than to create a whole new website for a number of handheld devices,
then face the dilemma of which site to serve for which tablet device.

Bootstrap really does look beautiful (if you like Twitter's aesthetic... which I
do). There's a hell of a lot they've thought of, from nice-looking tables and
forms, to tabs, sexy dropdown menus and alert messages. It works with IE7 and up
(no mean feat), and can also work with the Less framework, which is growing ever
more popular as a way to write more human-readable CSS.

I just wish the team had thought about ditching the grid and letting us plug our
own in. But this is nigh-on impossible when producing a generic framework for
the masses. I know: I've tried, and I tied myself in knots!
