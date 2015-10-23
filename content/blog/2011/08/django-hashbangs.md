Title: Django hashbangs
Date: 2011-08-10
Category: Blog
Tags: django, javascript
Summary: Thoughts on implementing hashbangs with Django and JavaScript

Hashbangs (basically URLs starting with the #! code) are a useful way of serving
web pages in sites where only a certain portion of a page is likely to update.
Facebook and Twitter use them throughout their sites to update their main
content panels, while leaving the remainder of the page unchanged. It can save
processing time and bandwidth, as you're only ever serving the part of the page
that changes. But the big advantage is that, unlike normal AJAX requests, you
can save the URL as a bookmark or link to it from outside.

What's vital however is making sure that hashbangs don't "break the web" as is a
common worry among those concerned with accessibility and the semantic web (of
which I'm one). I've now just implemented a hashbang system for Meegloo, which
is still in a testing phase, but I though tI'd run through my workflow from a
Django perspective.

### Client-side

I use jQuery to run through all of the links in my page whose `href` attribute
starts with a slash. That way it discounts any links to external pages, email
addresses or in-page anchors. I then prepend the #! prefix to these links, then
using the
[jQuery Hashchange](http://benalman.com/projects/jquery-hashchange-plugin/)
plugin I can detect when the browser's address bar has updated.

Any URL starting with a hash symbol is ignored by the server, and seen by the
browser as a link to something within the page. The exclamation mark in the #!
prefix is just a useful bit of shorthand so we can tell that we want to request
a URL via AJAX. So now I have a link which used to point to /blog/, but which
now points to #!/blog/.

Once I detect a change in the address bar, I parse the URL so I can get the
/blog/ portion, then request that URL via AJAX, appending a querystring value to
tell Django we're definitely doing a hashbang request, not some other form of
AJAX request. So my new URL is /blog/?hashbang=1.

Because all of this is done in JavaScript, the original URLs are left in tact.
I never hardcode a reference to a URL beginning with #!, but use JavaScript to
prepend it. That way search engines and those browsing without JavaScript can
get to the content in exactly the same way as those using JavaScript.

I place a `div` with an ID of "`bang`" in my template, and wrap that around the
blocks in my template that are most likely to change. I can still change over
areas of the page however (like the header and footer) by means of some clever
JavaScript, which I'll come to later.

### Server-side

Django can already tell when a request has come through from an AJAX request or
not. `The` request.is_ajax() call, combined with a querystring parameter
silently added to the request to confirm that the request came from a hashbang,
means we can serve only the portion of the page that's changed.

### Templates

I use a piece of middleware to add a property called `hashbang` (which is set to
`True`) to my `request` object. My site now has three base templates: base.html, base-std.html and base-bang.html.

All my other templates extend base.html, which then extends either the -std
(standard) or the -bang template. The -std template just renders the page as-is,
but the -bang template does something a little different.

My base-std.html has my <div id="bang">, but also allows me to flag up when other
templates make use of the header or footer blocks, to change those sections. I
use a bit of Django templating magic to wrap those changes in a string that
JavaScript parses, then dynamically places in the relevant area (header or
    footer). Sounds complicated, but it means that I don't have to change any of
    my other templates to make the new hashbang system work (which also means I
        can strip it out in a heartbeat if I find it's not working out too
        well). A big bonus.

Here's an example of what I'm referring to:

```html
<script>
    var nav = '{% filter escapejs %}{% block nav %}{% endblock %}{% endfilter %}';
    if(nav) {
        $('.module.menu').html(nav);
    }
</script>
```

This code is placed in my bang template, so any subtemplates which make use of
the `nav` block can do so normally, but their code will get turned into a
JavaScript string, via the `escapejs` filter. If I detect that custom menu HTML
is being used, I replace the menu that's currently there with the new one.

This might be a bit overkill, but it works at the moment.

### URL rewriting

To ensure that URLs don't get confused (ie: if you visit /blog/, all the
subsequent URLs will become /blog/#!/whatever/, which is very bad form), I
rewrite the URL in JavaScript to prepend the hashbang prefix. Again, because
it's being done in JavaScript, this doesn't affect users who don't have that
capability.

### Conclusion

With this method, which took me a couple of hours, I can serve fast-loading,
dynamic pages which fall back gracefully for non JavaScript users, and work
perfectly for search engines (as they don't parse the JavaScript that changes
the links). If you can see a hole in this methodology, or you have any
questions, [just shout](http://twitter.com/iamsteadman/)!

Unfortunately, Twitter doesn't seem to implement hashbangs in such an accessible
way, and actually doesn't work at all with JavaScript turned off, whereas
Facebook does.
