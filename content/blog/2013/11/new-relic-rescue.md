Title: New Relic to the rescue!
Category: Blog
Date: 2013-11-17
Summary: I get to grips with the New Relic app monitoring site
Tags: newrelic, django

### Update

I made a speculation about New Relic which was refuted (politely) on Twitter. I
just wanted to set the record straight :)

> Great success story by [@iamsteadman](https://twitter.com/iamsteadman) on our free plan. To clarify we will NEVER sell ANY customer data to ANYONE. <http://t.co/l3O8zat61r>
>
> — Lew Cirne (@sweetlew) [November 18, 2013](https://twitter.com/sweetlew/statuses/402262409890385920)

As [Nymbol](http://nymbol.co.uk/) slowly gains more traction and my personal
server groans under the weight of my flights-of-fancy, I gathered it was about
time I got my monitoring shit together.

I'd heard of a thing called [New Relic](http://newrelic.com/) but couldn't
remember what it was, and was convinced that whatever it did it was overpriced.
But when searching for server monitoring solutions it was the first one that
caught my eye, and to my wide-eyed surprise I discovered I could use it for
free.

It was ridiculously easy to install for the Django sites I host on my two
servers. Each application can be monitored separately, but I can also see how
the servers are doing overall. IT's already helped me fix memory leaks, overcome
speedbumps and more importantly gin a much better understanding of how my
machinery works, so that the next time there's an outage, I'll be more likely to
know whether it was down to my host or - more likely - a loose bit of code
rattling around somewhere.

So you can consider this a recommendation. I reckon we'll be using it at [Substrakt](http://substrakt.co.uk/) soon, as although our hosting partners have
given us near-100% uptime, it's always good to gauge the health of your servers,
when those boxes are your livelihood.

So, [check them out](http://newrelic.com/). Their paid plans are very expensive
but you probably won't need them. If a server goes down you probably won't need
more than 24 hours of data retention - which is what you get for free - and
there's so much great documentation available that you shouldn't need their
support.

My guess is that server data is being sold on to third parties, but I haven't
checked this. That's the only reason I can imagine for why so much is available
for free and why there's such a jump between that and the paid account. This
doesn't bother me particularly, but it might be worth looking into T&Cs if
you're worried. Like I say, that's _pure speculation_ on my part; I'm just
trying to figure out the catch.
