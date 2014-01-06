#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
###############################################################
###############################################################   Site abt.
###############################################################
AUTHOR = u'Zoom.Quiet'
SITENAME = u''
SITEDESC = u'.io'
SITENOTE = u"官网"

SITEURL = 'http://blog.zoomquiet.io'
DISQUS_SITENAME = u"blogzoomquietio" #填入你的Shortname

MARKUP = ('md', 'rst',)#'rst', 'html', 
READERS = {
        'html': None,
}
#   TIMEZONE = 'Europe/Paris'
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
        'zh_CN': '%Y-%m-%d %H:%M',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
DEFAULT_DATE = 'fs' # use filesystem's mtime

#LOCALE = ('zh_CN.utf8',)
DEFAULT_LANG = u'zh_CN'
FILENAME_METADATA = '(?P<slug>.*)'
###############################################################
###############################################################   Plugins abt.
###############################################################
# Plugins 
PLUGINS=['_plugins.sitemap'
    , '_plugins.extract_toc'
    #, '_plugins.gzip_cache'
    #, u"pelican.plugins.disqus_static"
    ]
MD_EXTENSIONS = (['toc'])

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
###############################################################
###############################################################   Template abt.
###############################################################
THEME = "_themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'readable'

DEFAULT_PAGINATION = 1
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_CATEGORIES_ON_MENU = None      # 分类标签是否显示在导航
# Social widget -> China jiathis.com
ADDTHIS_PROFILE = None #True
    
#GITHUB_USER = "ZoomQuiet"
MENUITEMS = (('PyChina', 'http://pychina.org')
    #, ('Zoom.Quiet', 'http://zoomquiet.io')
    , ('OBP', 'http://obp.zoomquiet.io')
    )

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS= None

SOCIAL = (('GitHub', 'https://github.com/PyConChina')
        , ('CPyUG', 'https://gitcafe.com/CPyUG')
        , ('News', 'http://news.pychina.org')
        , ('Wiki', 'http://wiki.woodpecker.org.cn/moin/CPUG')
        , ('rss', SITEURL + '/' + FEED_ALL_ATOM)
        , ('weibo', 'http://weibo.com/pyconcn')
        , ('O.B.P', 'http://weibo.com/openbookproject')
        )
# Blogroll
LINKS =  None
###############################################################
###############################################################   Publish abt.
###############################################################
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = None #因为嵌套仓库的原因,不能清除发布目录!
DEFAULT_CATEGORY = u'Chaos'

TEMPLATE_PAGES = {
        "404.html": "404.html",
        }

STATIC_PATHS = ['_images', '_files'
    , '_extra/robots.txt'
    , '_extra/favicon.ico'
    , '_extra/README.md'
    , '_extra/CNAME'
    , '_extra/LICENSE'
    ]

EXTRA_PATH_METADATA = {'_extra/robots.txt': {'path': 'robots.txt'}
    , '_extra/favicon.ico': {'path': 'favicon.ico'}
    , '_extra/README.md': {'path': 'README.md'}
    , '_extra/CNAME': {'path': 'CNAME'}
    , '_extra/LICENSE': {'path': 'LICENSE'}
    }

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'
# disable author pages
#AUTHOR_SAVE_AS = ''
#AUTHORS_SAVE_AS = ''

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True




