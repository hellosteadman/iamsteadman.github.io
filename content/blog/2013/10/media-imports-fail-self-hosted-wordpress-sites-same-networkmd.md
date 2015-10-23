Title: Media imports fail on self-hosted WordPress sites on the same network
Date: 2013-10-31
Category: Blog
Summary: How I got round a bizarre WordPress security "feature"
Tags: wordpress, php

At Substrakt I help maintain WordPress sites and networks. We have two big
WordPress networks, one for development and another for production. When we put
a site live, we export the development site into a newly-created production site
on the live network.

Most of the time that works fine, except for
[a recent change](https://github.com/WordPress/WordPress/commit/1ec392175ce5f0320072e7b195a8d091bccddefb)
to the core which validates URLs to see if they're "safe". When a URL isn't
"safe", the WordPress importer assumes there was something wrong with the server,
and not a mistake in the WordPress code, so it gives you the erroneous message:

> Server did not respond

I spent ages Googling and finally dove into the code where I discovered the
function that checks URLs for their "safety". One of the things it does is
checks the IP address of a URL, and if it looks like a local IP - or an address
within the same local area network - it'll reject the URL as unsafe.

Luckily a WordPress developer has created a filter you can hook into to override
this nonsensical decision. Just pop this somewhere in your theme, or create a
plugin to do the same:

```php
function my_http_request_host_is_external() {
    return true;
}

add_filter('http_request_host_is_external', 'my_http_request_host_is_external');
```

I call this a mistake not because it's intentional, but because it's not a
sensible thing to do. A "feature" like this shouldn't be turned on automatically
as it breaks backwards-compatibility and discourages a good server setup, where
you keep two separate machines for development and production, and shuffle data
between the two using the correct method (importing, rather than trying to fudge
the database).

Still, once you know the issue it's a very simple fix. I just wanted to post
this somewhere so that someone else coming across the same issue could be saved
an hour or so of pain.

A+ for the WordPress team for continuing to make security their watchword, but
minus several marks for forgetting not to break stuff that works, in order to
fix an edge case. (This is just my opinion as a grizzled developer, so [shout at
me on Twitter](http://twitter.com/iamsteadman) if you feel differently.)
