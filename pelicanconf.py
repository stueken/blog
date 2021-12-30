#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from dotenv import dotenv_values

# Create a dict with the values from .env file
ENV = dotenv_values('.env')

# Basic settings
# --------------
PATH = 'content'
PLUGINS = ['photos']
SITENAME = 'blog.nrbrt.com'
SITEURL = ''
STATIC_PATHS = ['images', 'theme']  # relative to PATH

# Integrates several typographical improvements into the generated HTML
TYPOGRIFY = True

CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True

# URL settings
# ------------
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
AUTHOR_URL = 'author/{slug}'
# AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHOR_SAVE_AS = ''
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
# TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_SAVE_AS = ''

# Time and Date
# -------------
TIMEZONE = 'Europe/Berlin'
DEFAULT_DATE_FORMAT = '%a, %-d %b %y'
LOCALE = ('en_US', 'de_DE')

# Template pages
# --------------
# 'authors' and 'tags' are not needed yet
DIRECT_TEMPLATES = ['index', 'categories', 'archives']

# Metadata
# --------
AUTHOR = 'Norbert Stüken'

# Feed settings
# -------------
# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pagination
# ----------
DEFAULT_PAGINATION = 10

# Translations
# ------------
DEFAULT_LANG = 'en'

# Ordering content
# ----------------

# Themes
# ------
THEME = 'notmyidea'
THEME_TEMPLATES_OVERRIDES = ['template_overrides']
# CSS_FILE = 'wide.css'
SITESUBTITLE = 'A personal blog'
# TODO should be the site repository, create open source repo
# GITHUB_URL = 'https://github.com/stueken'

# Blogroll
LINKS = (
    # ('Pelican', 'https://getpelican.com/'),
    # ('Python.org', 'https://www.python.org/'),
    # ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
    # ('You can modify those links in your config file', '#'),
)

# Social widget
# TODO other social sites to add?
SOCIAL = (
    # ('You can add links in your config file', '#'),
    # ('Another social link', '#'),
    ('GitHub', 'http://github.com/stueken'),
)
# LINKS_WIDGET_NAME = 'Blogs I follow'
# SOCIAL_WIDGET_NAME = 'Connect'

# Plugin settings
# ---------------

# TODO Reconfigure
# Options for Photos, see https://github.com/pelican-plugins/photos
PHOTO_LIBRARY = ENV['PHOTO_LIBRARY']
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_SQUARE_THUMB = False
PHOTO_RESIZE_JOBS = 5
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = SITENAME
PHOTO_WATERMARK_IMG = ''
