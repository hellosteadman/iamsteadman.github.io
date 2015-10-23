Title: Turbulent times with Titanium
Date: 2011-09-17
Category: Blog
Tags: appcelerator, titanium, javascript, meegloo
Summary: My latest roundup of issues with Appcelerator Titanium

Ever since [Chris Unitt](http://twitter.com/chrisunitt) introduced me to
Appcelerator's JavaScript solution to multiple mobile platform woes, [Titanium](http://www.appcelerator.com/products/titanium-cross-platform-application-development/),
I've been something of an advocate, and have blogged about it previously too.
But now I've hit a stumbling block, I want to do one of two things: get help on
the issue if it's available, and warn others who are trying to use the
functionality I'm using... which is broke.

Meegloo, the app I've talked about muchly in my
[video diary](http://moxypark.com/videos/egotrip/), will rely almost exclusively
on users being able to upload content from their mobile. So tonight I got stuck
into uploading audio recorded from the iPhone simulator to my local server. Not
the simplest of processes as I needed to send metadata aswell, and Titanium
doesn't have a way to do that out of the box. No fear though, as
[a very helpful post](http://www.smokycogs.com/blog/titanium-tutorial-how-to-upload-a-file-to-a-server/) got me most of the way there.

So now I had a shiny MP4 file and a way to distribute it. Problem solved, you'd
think, but in fact, it's a problem created. Titanium will _not_ read that file
as multipart form data (which is where you mix text with binary data in the same
    request... the sort of thing your browser does when you submit a contact
    form and attach a Word doc, for example). Whatever I did, I simply got back JavaScript's representation of the file, as a piece of text. I found
    [a module for Titanium](https://github.com/aaronksaunders/base64encodeUtil)
    whose sole purpose is to get round the issue. That doesn't work, so I'm kind
    of stuffed.

It's possible I might not be stuffed though, for two reasons. One is that I
_might_ be able to split my request in two: send the metadata first, get a file
ID back from the server, then send the actual file across, using the ID so the
server knows where to put it. But from the code samples I've seen online, I'm
not convinced of that just yet. The other is a very helpful tweet I just
received, from @[mindelusions](http://twitter.com/mindelusions):

> @moxypark email community@appcelerator.com and we'll help you out with any issues.
>
> — Anthony Decena (@mindelusions) [September 17, 2011](https://twitter.com/mindelusions/statuses/114870331067469826)

I reckon I'll take Anthony up on that offer, and see how far I get. I should say
that this won't stop me using or recommending Titanium, but it is a blow for the
"it can do virtually anything iOS can" argument. For instance, what's the point
of having the facility to record video if you can't upload it somewhere? It's
not like other apps can make use of those files, and Titanium isn't powerful
enough (I don't think anyway) to do full-on video editing.

Anyway, it all remains to be seen.
