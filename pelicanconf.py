#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Steadman'
SITENAME = u'code.steadman.io'
SITEURL = 'http://code.steadman.io'

PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
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
