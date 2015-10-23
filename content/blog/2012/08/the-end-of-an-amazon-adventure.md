Title: The end of an Amazon adventure
Date: 2012-08-06
Category: Blog
Tags: amazon, aws, hosting
Summary: Learnings from a time hosting with Amazon Web Services

I spent much of this weekend moving my websites from the two Amazon EC2 servers
I had, over to a hosting company I've used before and trust immensely, [Bytemark](http://www.bytemark.co.uk). I thought it might be useful to share
some of the things I've learned from using Amazon for the last 18 months.

### Amazon is slow.

EC2 (the Elastic Compute Cloud) is where you host the files that make your site
run. Back-end code, templates; stuff that is generated dynamically. You usually
run a few "instances" of the same server, so that if one instance goes down,
another is ready to take its place. I just kept the one copy of my two servers
(one server for Django, another for PHP), safe in the knowledge I could ramp up
when needed.

RDS (the Redundant Data Store) is where you stick the data for your site. There
has to be constant communicate between your EC2 instances and the data store,
which may be different physical pieces of hardware, but either way incur network
traffic costs (both in time and money). It's a really good system, because it
means you effectively keep one cloud-distributed copy of your data and share that
between the various instances of your servers.

S3 (their Simple Storage Service) is where you'd put stuff like CSS, JavaScript,
images, and files uploaded by you or your users via a browser. Unless you take
the time to write the right code, you'll probably end up having to upload the
files to your EC2 server which then sends them on to S3. Lost yet? I am. One of
its really nice benefits is CloudFront, which is a content delivery network. It
distributes copies of your files to servers all around the world (or within the
    ertain geographical boundaries that Amazon has setup), and serves that in
    standard downloadable form, or streams it via the Flash streaming protocol
    RTMP. So it's great for streaming audio and video. And because you pay only
    for the space you use, you never hit a storage or bandwidth limit.

But basically all this network traffic, coupled with what seems to be an
inherent slowness in EC2 leads to a noticeable lag. It's probably the
conversation between the web server (EC2) and the database server (S3), but I'm
not one for analysing graphs and numbers. But that wasn't by far the main reason
I decided to jump ship.

### Amazon is expensive.

When you use Amazon's services in the way they're intended, you really _really_
rack up the cost. My last hosting bill came to $700. This is for around a dozen
websites, with two of them streaming a little bit of video. The biggest cost
seemed to be RDS, and all the traffic that's necessary to make my sites work. If
I were running some high-profile, high-traffic sites I could justify the cost,
but for my piddling lot of nonsense it really is just ridiculous to pay that
much.

You can work out all the costs for Amazon's services via their calculator, but
only if you can predict the future. I can guess at how much data I'm going to
store, but how am I to guess how many times a file is going to be streamed or
downloaded? What if something goes viral?

This is where cloud hosting falls down for me. The scalability is wonderful, but
you can't budget for it because you can't predict how your data is going to be
used. Most of the cost for data comes when it's downloaded. Storing and
uploading files is relatively cheap, but downloading and streaming them is
expensive. So, just something to be aware of.

### Amazon is reliable.

I mentioned I had two servers: Colin and Blomkvist. Colin went down a lot, but
I'll put that down to my inability to configure Apache to deal with WordPress'
various holes and inefficiencies (and the blemishes found in third-party
    plugins). Blomkvist however, which had a much harder job, running several
    Django sites with lots of different processes going on (including encoding
        video via ffmpeg) never went down once. Not once. It was an absolute
        trouper of a machine, and it was only a level or two up from Colin, in
        terms of power.

I never had a problem with RDS. I had many of my DNS records hosted with them
and they were fine. All my files stayed in tact and were always available.
Amazon's Control Panel was also there when I needed it, so I really couldn't
complain.

### Amazon is simple.

If you're a developer with experience managing a VPS, you'll have no problem
getting your head round Amazon's setup. Once you know what their various names
and acronyms mean, you're pretty much set.

### Amazon is not available for comment.

Unless you pay for a certain type of account, you don't get any type of support.
I could argue that for $700 I should've had someone sitting with me at all
times, checking that everything was still working, but that's the bargain you
enter into. I don't even think you get email support; your'e left with the
"community" option which, if you're a fan of flaming and lols is probably great
fun. I had one major support issue - which was a problem I caused - and had
no-one at Amazon available to help me. That's a problem if, like me you like a
host that you can call up and say "Hi, can I speak to John; he's been dealing
with my server". I don't want to mis-sell Bytemark's services, but that's a bit
more of the feel you get with them... certainly over email anyway (I don't think
I've ever needed to call them).

### Amazon is no longer my host.

It was basically the price that drove me away. I knew exactly who I wanted to go
back to, and that I could save my business about £400 a month in the process.
The difference in speed was noticeable when I got my first site up, and stayed
that way when I loaded all the rest on. Let's see how it copes with WordPress
and Django bunking up together though :)

If you want to dip your toe in cloud hosting, there may be other providers
better suited, but Amazon really does the complete package, and makes it all
manageable. I don't think all cloud providers have got their head around the
user interface, in the same way that UNIX people think that all developers like
to see yellow fixed-width text on black boxes, and think that any display of
data that isn't in a table is just a "pretty picture". Amazon makes everything
manageable through its web-based control panel, and once you've got a machine
booted up, then your'e into a terminal window and on familiar ground.

After i tweeted my thoughts on Bytemark last week, I got a reply from their MD
asking if I wanted to check out their cloud solution. I'll definitely be
checking it out once the dust has settled on my new server. Cloud hosting works,
but you do have to keep an eye on the money.
