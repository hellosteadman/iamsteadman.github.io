Title: Category Template
Date: 2015-10-24
Category: Projects
Tags: pelican, python
Summary: A Pelican plugin for creating category-specific article and listing templates

This site uses [Pelican](http://blog.getpelican.com/) to generate a blog from
static files, maintained in a Github repo. (It's configured in s slightly
unusual way so as to remove the `.html` extension from the URLs). It's hosted on
Github Pages.

I wanted each of my categories to have a specific title and description, and the
only way I thought I could do this was by creating category-specific templates,
similar to how WordPress works (and using the same kind of fallbacks we have
for locating templates in Django).

The plugin mechanism for Pelican is quite simple to get to grips with, and is
based on signals (in much the same way as WordPress plugins are based on
'actions' and 'filters'). Specifying a template for a specific article isn't too
hard, as there's a signal that the plugin can receive, to change the template
for a specific article (falling back to the original template if the
category-specific one can't be found).

We do that like this:

```python
if content.category:
    template = 'category/%s/article' % content.category.slug

    try:
        article_generator.get_template(template)
    except PelicanTemplateNotFound:
        pass # No category-specific templates exists
    else:
        content.template = template # Use the category-specific template found
```

The problem with the listing pages (/blog/, /projects/ etc) is that Pelican
doesn't have a signal to specifically handle the output of this type of page (or
at least, I couldn't find one that fit).

So I had to monkeypatch the `generate_categories` method of the
`ArticlesGenerator` class, which is the file that outputs all the HTML for
articles and their listings pages. It will only use the 'articles' template,
and there's no way to override that behaviour in a hookable way.

Hence the monkeypatching, which is problematic of course because, if this
function gets refactored, this plugin won't work any more. but for now, it's a
working solution.

The issue I had with monkeypatching is that I wasn't familiar with doing that
with instance methods (functions in a class, rather than standalone ones just
sitting in a module), but a quick bit of Google fu got me what I needed.

I hook into the `generator_init` signal, then replace the built-in
`ArticlesGenerator.generate_categories` method with my own, by passing the
new method and the old class to the `types.MethodType` function. So my new
monkeypatched version of the method looks like this:

```python
def generate_categories(instance, writer):
    for cat, articles in instance.categories:
        try:
            # Use the category-specific template if it exists
            category_template = instance.get_template(
                'category/%s/index' % cat.slug
            )
        except PelicanTemplateNotFound:
            # Fallback to the 'category' template if it doesn't
            category_template = instance.get_template('category')

        # The rest is the same function as originally in Pelican
        articles.sort(key = attrgetter('date'), reverse = True)
        ...
```

What I might do next, time permitting is contribute a signal to the Prelican
project that this plugin can hook into, so no more monkeypatching.

<a class="btn" href="https://github.com/iamsteadman/pelican-category-template">
    <span class="octicon octicon-git-branch"></span>
    Fork it on GitHub
</a>
