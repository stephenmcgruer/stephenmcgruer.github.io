#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Stephen McGruer'

SITENAME = u'Stephen McGruer'
SITEURL = ''

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

MENUITEMS = [('Home', '/')]
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['images']

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 10

THEME = 'pelican-octopress-theme/'
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal', 'liquid_tags.youtube']

TWITTER_USER = 'stephenmcgruer'
GOOGLE_PLUS_USER = 'stephenmcgruer'
GOOGLE_PLUS_ONE = True
GOGOLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = False
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'False'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'

FEED_DOMAIN = None
FEED_ATOM = None

SEARCH_BOX = True
