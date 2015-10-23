Title: Format-rules
Date: 2014-05-03
Category: Projects
Tags: django, markdown
Summary: Syntactical sugar ontop of Markdown for adding extra formatting, expressed in a human-readable way

In [The designer blog post](http://journal.steadman.io/the-designer-blog-post/),
I wrote about updating the blogging app in my toolset to allow easy offline
creation of blog posts. For standard pages I've gone a different direction, with
a library I've started, called formatrules.

With this Django app - which, for the uninitiated is the Django community's word
for what most people might call a plugin - I've created the ability to define
multi-column layouts in Markdown, without writing any complex HTML. Or any HTML
at all, for that matter. Here's an example of the text of a page:


    Donec id elit non mi porta gravida at eget metus.
    Donec sed odio dui. Nullam id dolor id nibh
    ultricies vehicula ut id elit. Praesent commodo
    cursus magna, vel scelerisque nisl consectetur et.

    // Block of three
    Aenean lacinia bibendum nulla sed consectetur.
    Maecenas sed diam eget risus varius blandit sit
    amet non magna. Cras mattis consectetur purus sit
    amet fermentum. Curabitur blandit tempus porttitor.

    // Block of three
    Cras mattis consectetur purus sit amet fermentum.
    Donec ullamcorper nulla non metus auctor fringilla.
    Donec id elit non mi porta gravida at eget metus.
    Cum sociis natoque penatibus et magnis dis parturient
    montes, nascetur ridiculus mus.

    // Block of three
    Cras justo odio, dapibus ac facilisis in, egestas
    eget quam. Nulla vitae elit libero, a pharetra augue.
    Donec id elit non mi porta gravida at eget metus.

The text is formatted so that it can be put through the Markdown filter. But
where it gets fun is in those double-slashes. They're not just comments, but
instructions to a filter which reads them and then wraps the proceeding content
in Bootstrap columns. "Block of three" basically means "one third of a page".
I could equally say "block of two", "four", "six" or "twelve". I can even get
cleverer with "two-thirds block" and "half-block". So here's the process the
code runs through:

  1. Use a regular expression to look for new lines starting with a double-slash
  and an instruction.
  2. Check whether that instruction matches a given list of regular expressions
  3. Parse the text, taking everything from just past that // line, to the next
// line (or the end the text if there are no more instructions)
  4. Pass that parsed text to the function we matched up in the second step
  5. Replace the parsed text with the result of that function
  6. Look for the next set of double-slashes
Step three involves a third-party function. Well, it's actually a class, and it
can do a couple of nice things. It can parse the text given to it, and also clean
up after itself. I'll explain.

The // comments aren't nested; one instruction is processed after another, so if
there's no need for an explicit "end block" instruction. However, with Bootstrap
you have to create columns inside a "row", so my class knows when its parsing
function is being called for the first time, and it opens a `<div>` with a class
of `row`. The formatrules filter runs the `cleanup` function on any class that's
been used during the parsing of the text, so the cleanup function is run on my
class and the "row" element is closed.

The real-world example - being the only parser I've developed for the
formatrules filter so far - is probably a bit overcomplicated, so let's
simplify.

What if I wanted a whole block of text to be bold? Rather than surrounding it in
double asterisks in the Markdown way, I could have an instruction like so:

    // Bold

    All of the rest of this text will be bold.

I'd create a class that responds to the regular expression `^Bold$`, and add a
function that wraps the proceeding text in a <`div>` tag with a `style` or
`class` attribute. I wouldn't, as that would be ghastly and antisemantic, but
you get the idea.

Any instructions that followed would override the bold instruction, because I
figure simplicity is better than flexibility when you're dealing with a
web-based text editor.

As I mentioned, the "block" parser is the only one I've written so far as that's
all I wanted to do, but you get an idea of how useful it is when you see the
layout it produces, with very simplistic - and more-importantly, human
readable - instructions.

![Screen Shot 2013-03-26 at 23.48.15](/images/2013/03/presenting-formatrules.png)

I love the uncluttered simplicity that Markdown provides, so I wanted to develop
something that echoed that approach. There are loads of ways this can be
extended and improved and made more flexible for developers - allowing the
classes the parsers produce to be overridden for example - and I've made
developing new parsers pretty simple. However the biggest limitation I've come
across so far is that, because you're wrapping Markdown text in HTML elements,
the Markdown parser - at least the Python one - ignores the paragraphs as it
assumes that whatever is in that box is "raw" HTML, so I'm having to parse the
text inside each "block" with Markdown, then parsing the whole lot through again (obviously the parser then ignores the bits inside HTML tags so it's not exactly
doing the same thing twice). This is inefficient but hey, it's a start.

If you like the idea, bambu-tools is a set of Django reusable apps that I've
built and use in production environments. It's not well documented right now,
but it's up on [PyPi](https://pypi.python.org/pypi/bambu-tools) for your
perusal, judgement, comments and suggestions. You'll also [find the code on BitBucket](https://bitbucket.org/marksteadman/bambu-tools) (without some of the
changes in the PyPi version. There's a reason for this, it's just not a good
one).

If you like the idea, feel free to steal it and build it into your next project.
Just maybe gimme a credit and get in touch if you have any questions.

<a class="btn" href="https://github.com/iamsteadman/bambu-formatrules">
    <span class="octicon octicon-git-branch"></span>
    Fork it on GitHub
</a>
