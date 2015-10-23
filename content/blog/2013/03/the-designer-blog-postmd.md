Title: The designer blog post
Date: 2013-03-07
Category: Blog
Tags: django, blogging
Summary: An update to my Django blogging app, to add the ability to import
static, HTML files as posts

It's been around for a while, but the concept of stylised blog posts - where
each post is uniquely laid out - is increasingly popular, and attractive. I'm
implementing a little of that over on the [Nymblog](http://nymbol.co.uk/blog/)
(the blog for my mobile CMS), but I've now just made the process of building and
uploading stylised blog posts much easier. It's only in Django at the moment,
but I'd like to port this over to WordPress. Here's how it works.

### Every site is different

You download a boilerplate HTML file from the Django admin. This is generated
from a template. In Django - a little like in WordPress - you can override
templates, so the boilerplate file can come from my generic blog app (an app in
Django is like a plugin in WordPress) or from the actual site itself. So I've
created a boilerplate file specifically for the Nymbol blog.

The idea is that, when downloaded, you get an HTML page that you can edit in a
text editor and preview in a browser. All the references to stylesheets and
JavaScript files are absolute, so as long as you're connected to the Internet
your page will look and function pretty much like a normal blog post.

So what's cool is that you're getting a boilerplate file tailored to that
specific site. The same principle would work with a WordPress blog. WordPress
would generate a fake blog post then export the HTML for the author to download.

### Writing the post

There are a few HTML elements with special attributes, which the system uses to
read your blog post. Here's a snippet:


    <h1>
        <a href="#" data-bpfield="title">This is my post</a>
        <small>Posted <span data-bpfield="date">March 8, 2013</span> by
        mark</small>
    </h1>

The `data-bgfield` attributes map to the title and date of the post. I can use
lots of different date formats, and my app will convert that into a date that
can be stored in the database. Then I look for a snippet like this:


    <div data-bpfield="body">...</div>

I put the HTML of my blog post where the ellipses go.

### Styling it up and adding some spice

Of course the whole point of this exercise is to allow custom styling, so to do
that I look for an HTML element like this:


    <style data-bpfield="css">...</style>

I put the CSS for my blog post in here, which is stored in the database in a
separate field, not embedded in the HTML. Usually all the CSS rules would have
to be prefixed with a class that is only applied to single blog posts.

Now here's where it gets cool. I can add images and other files to my blog post.
I start by putting them in the same directory as my HTML file, then just
reference them using a relative URL, like this:


    <img src="kitten.jpg" />

### Zip it and upload!

Once I'm happy that my blog post looks great in the browser, I zip up the files
I've created and upload them via the admin area. The blog app then unpacks the
Zip file, extracts the HTML and looks for any files referenced (basically
anything with an `src` attribute). If it finds a file with that name inside the
zip, it extracts it, adds it as an attachment to the blog post (which naturally
changes its URL), then replaces that URL within the HTML and CSS.

I've added an option in my app which allows me to convert the HTML of the post
body to Markdown (the syntax used by default within my blog app). The nice thing
about Markdown is that it does allow HTML to be added to it, so if I untick that
option, rather than converting the HTML to Markdown, it leaves it as it is. The
first option is useful if you want to edit the post later on; the second is
useful if it's very stylised, with lots of classes and other attributes which
don't have a place within the Markdown syntax.

### Limitations

Probably the biggest limitation so far is that, if you reference an image within
your CSS but don't include it in your HTML, the find-and-replace thing won't
work. That's an easy problem to fix; I just haven't yet.

You can't provide styling for a blog post within a list, only for the single
post page. This is because you don't know the ID of the blog post you're
targeting when you write the HTML locally, so you can't target that specific
element within a list. The way to get over this is to set an ID in the
boilerplate HTML which you can use in your CSS, then replace that ID with the
correct ID of the blog post when published.

There are probably other limitations, but they don't spring to mind just yet.

### Porting

If this doesn't exist already, I think it'd make a really nice WordPress plugin.
Sometimes it's useful to have the designed approach alongside the might of the
WordPress engine, to handle comments, trackbacks, RSS, that sort of thing.
Adding custom CSS for each blog post is as simple as creating a hidden custom
field, and using a plugin to spit out the CSS when needed.

If it does already exist for WordPress, even better 'cos that means I don't have
to write it! But I wanted it for my Django toolset, so now I have it.
