#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

###############################################################
###############################################################   Site abt.
###############################################################
AUTHOR = u'Zoom.Quiet'
AUTHOR_INFOS = True

SITENAME = u''
SITEDESC = u'ZoomQuiet.io'
SITENOTE = u".io"
SITETITLE = u'#是也乎#'
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

#   upgraded Pelican 3.3 must self open them
MD_EXTENSIONS = (['codehilite(css_class=highlight)'
    , 'extra', 'abbr', 'attr_list', 'def_list', 'fenced_code', 'smart_strong'
    , 'admonition', 'meta', 'tables', 'sane_lists'
    , 'toc'
    ])

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

TYPOGRIFY = True
###############################################################
###############################################################   Template abt.
###############################################################
THEME = "_themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'readable'

DEFAULT_PAGINATION = 3

DISPLAY_TAGS_ON_SIDEBAR = False
TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = None      # 分类标签是否显示在导航
# Social widget -> China jiathis.com
ADDTHIS_PROFILE = None #True
    
#GITHUB_USER = "ZoomQuiet"
MENUITEMS = (('PyChina', 'http://pychina.org')
    #, ('Zoom.Quiet', 'http://zoomquiet.io')
    , ('OBP', 'http://obp.zoomquiet.io')
    )

FEED_ALL_ATOM = 'feeds/all.atom.xml'
# ('rss', SITEURL + '/' + FEED_ALL_ATOM)
SOCIAL = (('旧文', 'http://blog.zoomquiet.org/pyblosxom/')
        , ('.io', 'http//ZoomQuiet.io')
        , ('GitHub', 'https://github.com/ZoomQuiet')
        , ('Wiki', 'http://wiki.woodpecker.org.cn/moin/ZoomQuiet')
        , ('O.B.P', 'http://code.google.com/p/openbookproject/')
        , ('Weekly', 'http://weekly.pychina.org/')
        , ('weibo', 'http://weibo.com/zoomquiet')
        )
# Blogroll
LINKS =  None
###############################################################
###############################################################   Publish abt.
###############################################################
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = u'Chaos'
#DELETE_OUTPUT_DIRECTORY = None #因为嵌套仓库的原因,不能清除发布目录!

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

# disable author pages
#AUTHOR_SAVE_AS = ''
#AUTHORS_SAVE_AS = ''






