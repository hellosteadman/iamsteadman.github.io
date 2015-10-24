#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Steadman'
SITENAME = u'code.steadman.io'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('My journal', 'http://journal.steadman.io/'),
    ('My dayjob', 'http://substrakt.com/'),
    ('My side project', 'https://poddle.io/')
)

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/iamsteadman/'),
    ('Twitter', 'https://twitter.com/iamsteadman/')
)

DEFAULT_PAGINATION = 10

# Categories
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'blog'

# URLs
CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tags/{slug}'
TAG_SAVE_AS = 'tags/{slug}/index.html'
ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
AUTHOR_URL = '@{slug}'
AUTHOR_SAVE_AS = '@{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

# Theme
THEME = 'themes/primer'

# Static files
STATIC_PATHS = ('images', 'extra/CNAME')
EXTRA_PATH_METADATA = {
    'extra/CNAME': {
        'path': 'CNAME'
    }
}

# Google Analytics
GOOGLE_ANALYTICS = 'UA-29554105-19'

# Plugins
PLUGIN_PATHS = ('plugins/',)
PLUGINS = (
    'category_template',
)
