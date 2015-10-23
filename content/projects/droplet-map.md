Title: Droplet Map
Date: 2014-01-23
Category: Projects
Summary: Tracking the top companies taking money through Droplet, and the kinds
of things people buy.
Tags: django, twitter, dropletpay

After seeing a few tweets over the past few months pointing to people's [Droplet](http://dropletpay.com/) purchases (ala the example below), I thought
I'd map out the kinds of things people buy, and the amounts of money they spend.

> I just paid [@urbancoffeeco](https://twitter.com/urbancoffeeco) £1.50 via [@dropletpay](https://twitter.com/DropletPay)
>
> — Craig Edmunds (@craigtech) [June 19, 2013](https://twitter.com/craigtech/statuses/347361214860505089)

For the uninitiated, Droplet is a way of paying for stuff using your phone. You
charge up your phone with "credit" using your bank card, and you can pay for
stuff simply and easily. I know a couple of the gents who founded the company
who are based in my native Brum, so it's really cool to see the thing begin to
spread.

So, to the hack. Last night I set about using the Twitter search API to find
tweets mentioning @[dropletpay](http:/twitter.com/dropletpay), and matching a
particular pattern ("I just paid [company name or Twitter handle] £x via
@dropletpay"). I then parsed the tweet, pulled out the relevant details and
stored them in a database. I then use the Twitter users API to get a bit more
info on each company, like their full name, location, URL and description. The
resulting map looks something like this (it's interactive, so you can click, pan
and zoom):

(You'll need to read the article in full to see the map)

The data's really sparse at the moment as tweets drop off the search index after
a week, so I've only got the last few days to play with, but it should update
fairly rapidly so hopefully the leaderboard will start to become a bit more
interesting.

<a class="btn" href="https://github.com/iamsteadman/droplet-map">
    <span class="octicon octicon-git-branch"></span>
    Fork it on GitHub
</a>
