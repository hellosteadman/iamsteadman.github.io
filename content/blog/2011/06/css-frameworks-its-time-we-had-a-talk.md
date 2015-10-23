Title: CSS frameworks: it's time we had a talk
Date: 2011-06-19
Category: Blog
Tags: css
Summary: My thoughts on Blueprint, 960 and responsive web design

[Blueprint](http://www.blueprintcss.org/), we've had some laughs, you and me.
You too, [960](http://960.gs/) (although I never liked your underscores), but
now there's something new in my life, and there just isn't room for you anymore.
It's not you... well, it _is_ you. Y'see, you're just not... flexible enough.

Over the weekend, [Ethan Marcotte](http://unstoppablerobotninja.com/) has been
teaching me, via his book [Responsive Web Design](http://www.abookapart.com/products/responsive-web-design), about
creating flexible, near-fluid designs that adapt to browser (or "viewport")
size, orientation and even capability. I'd tried creating mobile style sheets by
using @media queries to determine the width and height of my iPhone browser, but
hit a brick wall really quickly when I realised that the framework I was using
was simply inflexible.

CSS frameworks are really great for knocking up sites quickly: but they're for
the desktop, really. They confine you to a 960(ish) width (although you can
    change that... but that means creating a whole new stylesheet) and use
    classes within your HTML to determin how many columns wide a block of
    content should be (ie: Blueprint divides its page into 24 columns, so a main
        section might be 16 columns, with 8 left over for a sidebar). It's not
        semantic - but that doesn't bother me because I use other classes (and
            markup) that are.

Smartphones are really good at rendering web pages, but any site that isn't mobile-optimised in some way will have readers itching to pinch, so they can
actually read the stuff that's been rendered in tiny font, or they'll be forever
running their finger back and forth, back and forth, back and forth as they
scroll horizontally through your too-wide page.

So, using my portfolio site and playground,
[moxypark.co.uk](http://moxypark.co.uk) as a guinea pig, my first job was to
replace all my `span-_xx_` classes (where _xx_ is a number of columns, not a
    dull hipster band) with more useful, semantic words, and combinations of
    words (`module`, for standard-size columns, then `module headliner` for
        double-width ones [they're completely arbitrary really, as the HTML
        markup is more semantic]). In Ethan's book, he built a site from
        scratch, whereas I had a load of legacy grot to get rid of, so it took
        me a bit of time.

I looked back through the Blueprint source, got the widths of those `span-xx`
elements and did some calculations to express those as percentages of 950 (the
    maximum width in a Blueprint-styled page). Then, instead of having a
    container that was 950px wide, I made it 90% of the page width, thus giving
    me a fluid layout with no pixels (except for the logo and pullout sections,
        which float absolute left and absolute right, respectively, and _need_
        to be measured in pixels).

You could, if you were inclined, argue that it is possible to make a fluid CSS
framework - and I'm fairly sure they already exist - but the problem is,
although they're flexible, they're not _responsive_: they don't give a monkey's
if you're viewing a site on a mobile and the sidebar is too small to be of any
use, or you're on a hi-res widescreen monitor and you're getting a crick in your
neck from shuttling your head back and forth as you read overly-long lines of
text because the main section is too wide. They're inherently grid-based, which
is fine until you hit a device or a configuration (I'm trying now not to think
in terms of devices [as there are too many to keep track of] but simply viewport
sizes) which makes that grid senseless. Then it's no good having a load of HTML
classes that reference columns if you need to move columns above or below other
columns. 'Cos then, they stop being columns. But anyway, back to the story.

Still following the hints and tips in Ethan's book, I set about creating a bunch
of @media queries with rules to go with them, to provide gradual changes to the
layout of my site, I started big, with a browser width of 1600px, and shrank all
the way down to a 360px iPhone screen.

A useful note that was mentioned in the book is that iPhones render pages at
980px wide, then shrink them down to fit the screen, so all your width and font measurements are still relative to that 980px context (Ethan talks in detail
    about using percentages, not pixels to measure items in a grid). A simple
    meta tag tells the device to render at its device width, 360px. thus making
    the measurements for the mobile version of your style sheet much more
    sensible, as they're a percentage of 360, not 980. Confused? Ah, don't worry
    about it ;)

There are a few stress points in the design: the left-hand logo overlaps the
text in a particular width range, but then as you get smaller the logo backs
away, then completely disappears (as do the social icons in the top-right, in
    order to make room for the full menu).

A nice touch - well I thought so - was the menu. It's quite long for a mobile
site, and would split into two lines, but with an ellipses, a bit of absolute
positioning and a couple of lines of jQuery I was able to make an overflow menu
that put the blog, writing and podcast lists one tap away. (That might not be to
    everyone's tastes, but I prefer as small a menu as possible).

I've also put Ethan's wise words about image resizing to use, but there's more
work to be done here, as mobiles currently are having to download images at a
size they'll never need to deal with, in order to improve the quality for
desktop users. This isn't cool, but I've got a neat little idea for marrying the
[sorl.thumbnail](http://pypi.python.org/pypi/sorl-thumbnail) package which I use
for image resizing with something like the
[Device Atlas](http://deviceatlas.com/) API (only free), to resize images at the
server before pushing them to the client. A challenge yes, but potentially a fun
one.

From a standing start it's taken me about 6 hours to dismantle my Blueprint
world and rebuild it in a flexible image, but I'm really glad I did. The site
looks pretty bloody smart on a mobile now (catering for landscape and portrait),
and it fairs well with much higher resolutions too. Proud Moxy is proud.

I'm not saying my site is perfect by any means. There's a lot of content there
that's relegated to the status of second-class citizen, but I wasn't setting out
t to improve the design, just its rendering under different conditions. But I
now feel newly-armed as a developer, having taken as significant a leap forward
in frontend development as when I first learned to use CSS rather than tables
for layout. I really think it's that significant, although the knowledge that I
can no longer justify the use of CSS frameworks - at least in my own projects; I
don't run the design team where I work... and nor should I - is scary. The
problem is, if you want to be responsive, you can't lock yourself down with HTML
classes that carry visual context, because that context is different for every
device.

There are however some really useful elements to take from CSS frameworks: reset stylesheets, typography and form element styling are things that apply across
the board, and are really nice to establish as a bedrock, so I'll definitely
keep using those kinds of rules in my CSS.

So, here's to the future of responsive web design, and bless you for reading
this far! :)
