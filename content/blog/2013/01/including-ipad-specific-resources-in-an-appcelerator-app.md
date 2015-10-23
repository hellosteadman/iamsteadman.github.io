Title: Including iPad-specific resources in an Appcelerator app
Date: 2013-01-02
Category: Blog
Tags: appcelerator, titanium, javascript
Summary: Exactly what it says in the title

I'm building an app with
[Appcelerator Titanium](http://www.appcelerator.com/platform/titanium-sdk) that
will run on iPhone, iPad and Android. With Titanium it's quite easy to
distribute iPhone- and Android-specific images - custom map pins, native-looking
icons, that sort of thing - but I've only now just figured out how to distribute iPad-specific images aswell. So for anyone else who's struggling, here's how you
do it. (I found the answer through a [ticket](https://jira.appcelerator.org/browse/TIMOB-4483)
raised on the Titanium issue tracker).

Rename your iPad images so that the text `~ipad` appears just before the file
extension (so `mapmarker.png` becomes `mapmarker~ipad.png`, and
`mapmarker@2x.png` becomes `mapmarker@2x~ipad.png`), then place them in the `Resources/iphone` directory. For clarity, it's a tilde (~) symbol, hot a hyphen
(-).

This is inline with the iOS guidelines, but slightly at odds with the (incorrect
but understandable) assumption that you'd put iPad-specific images in a
directory called `Resources/ipad`.
