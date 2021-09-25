#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Norbert Stüken'
SITENAME = 'blog.nrbrt.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME_TEMPLATES_OVERRIDES = ['template_overrides']

PLUGINS = ['photos']

# Options for Photos, see https://github.com/pelican-plugins/photos
PHOTO_LIBRARY = "~/Nextcloud/inbox/photos"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_SQUARE_THUMB = False
PHOTO_RESIZE_JOBS = 5
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = SITENAME
PHOTO_WATERMARK_IMG = ''
