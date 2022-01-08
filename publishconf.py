#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


# Basic settings
# --------------
# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = ENV['SITEURL']
# TODO True will rebuild everything and genereate wrongly aligned photos!
DELETE_OUTPUT_DIRECTORY = False

# URL settings
# ------------
RELATIVE_URLS = False

# Feed settings
# -------------
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# Themes
# ------

# Following items are often useful when publishing
# TODO Add comments
#DISQUS_SITENAME = ""
