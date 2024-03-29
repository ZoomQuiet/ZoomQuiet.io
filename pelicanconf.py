#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
"""Problem Faced when integrating with Elegant Themes. - Surprise. · Archer Imagine 
    http://archerimagine.com/articles/pelican/integration-problem-with-elegant-theme.html
"""
###############################################################
###############################################################   Site abt.
###############################################################
AUTHOR = "Zoom.Quiet"
AUTHOR_INFOS = True

SITENAME = ""
SITEDESC = "ZoomQuiet.io"
SITENOTE = ".io"
SITETITLE = "是也乎(￣▽￣)"
SITEURL = "https://blog.zoomquiet.io"
# DISQUS_SITENAME = u"blogzoomquietio" #填入你的Shortname

MARKUP = (
    "md",
    "rst",
)  #'rst', 'html',
READERS = {
    "html": None,
}
#   TIMEZONE = 'Europe/Paris'
TIMEZONE = "Asia/Shanghai"
DATE_FORMATS = {
    "zh_CN": "%Y-%m-%d %H:%M",
}
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M"
DEFAULT_DATE = "fs"  # use filesystem's mtime

# LOCALE = ('zh_CN.utf8',)
DEFAULT_LANG = "zh_CN"
FILENAME_METADATA = "(?P<slug>.*)"
###############################################################
###############################################################   Plugins abt.
###############################################################
# Plugins
PLUGIN_PATHS = ["_plugins"]
PLUGINS = [
    "sitemap",
    "extract_toc",
    "neighbors",
    "render_math",
    # , '_plugins.gzip_cache'
    # , u"pelican.plugins.disqus_static"
]

#   upgraded Pelican 3.3 must self open them
# MD_EXTENSIONS = (['toc'])

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": "true"},
    },
    "output_format": "html5",
}

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {"linenos": "table"}

# TYPOGRIFY = True
###############################################################
###############################################################   Template abt.
###############################################################
THEME = "_themes/pelican-bootstrap3"
# THEME = "_themes/z0css"
# BOOTSTRAP_THEME = 'readable'
# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

DEFAULT_PAGINATION = 7

DISPLAY_TAGS_ON_SIDEBAR = False
TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = None  # 分类标签是否显示在导航
# Social widget -> China jiathis.com
ADDTHIS_PROFILE = None  # True

# GITHUB_USER = "ZoomQuiet"
MENUITEMS = (
    # ('PyChina', 'http://pychina.org')
    ("大妈", "http://zoomquiet.io"),
    # ("课程", "https://py.101.camp/"),
    ("油管", "https://www.youtube.com/@Chaos42DAMA"),
    # , ('友链', 'https://t.zsxq.com/iaIEQ3N')
    # , ('不折腾要屎行径', '/pages/about.html')
    ("友链", "/pages/friendly-links.html"),
    ("好物", "/pages/affiliate.html"),
    ("关于", "/pages/zoomquiet.html"),
    # , ('收集', 'https://zoomquiet.io/collection.html')
    # , ('OBP', 'https://zoomquiet.io/obp/index.html')
    # , ('design', '/pages/design.html')
)
DISPLAY_PAGES_ON_MENU = True

FEED_ALL_ATOM = "feeds/all.atom.xml"
# ('rss', SITEURL + '/' + FEED_ALL_ATOM)
SOCIAL = (
    ("Root", "https://ZoomQuiet.io"),
    ("GitHub", "https://github.com/ZoomQuiet/ZoomQuiet.io"),
    ("大妈的多重宇宙", "https://www.youtube.com/@Chaos42DAMA"),
    ("豆瓣", "https://www.douban.com/people/zoomq/"),
    ("蟒周刊", "http://weekly.pychina.org/"),
    ("锈周刊", "https://weekly.rs.101.so/"),
    # ('周看/电子报', 'https://zoomquiet.substack.com/'),
    # ('怼周报', 'https://du.101.camp/duw/')
    # , ('O.B.P', 'https://github.com/OpenBookProjects/wiki/blob/master/HowToBuildBookOnline.md'),
    # ('思否', 'https://segmentfault.com/u/zoomquiet'),
    # ('星球', 'https://t.zsxq.com/iaIEQ3N'),
    # ('知乎', 'https://www.zhihu.com/people/zoomquiet'),
    # , ('掘金', 'https://juejin.im/user/5aa4848951882577b45ea1fe')
    # ('极术', 'https://aijishu.com/u/zoomquiet'),
    # ('开源中国', 'https://my.oschina.net/zoomquiet')
    ("gitlab", "https://gitlab.com/ZoomQuiet"),
    # ('weibo', 'http://weibo.com/zoomquiet'),
    ("啄木鸟", "http://wiki.woodpecker.org.cn/moin/ZoomQuiet"),
    ("维基", "http://wiki.zoomquiet.io"),
    ("旧blog", "https://org.zoomquiet.io/pyblosxom/"),
    ("小红花Club", "https://xhh.club/"),
)
# Blogroll
LINKS = None
###############################################################
###############################################################   Publish abt.
###############################################################
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = "Chaos"
# DELETE_OUTPUT_DIRECTORY = None #因为嵌套仓库的原因,不能清除发布目录!

TEMPLATE_PAGES = {
    "404.html": "404.html",
}

STATIC_PATHS = [
    "_images",
    "_files",
    "_extra/robots.txt",
    "_extra/favicon.ico",
    "_extra/README.log",
    "_extra/LICENSE",
    "_extra/CNAME",
    "_extra/.nojekyll",
]

EXTRA_PATH_METADATA = {
    "_extra/robots.txt": {"path": "robots.txt"},
    "_extra/favicon.ico": {"path": "favicon.ico"},
    "_extra/LICENSE": {"path": "LICENSE"},
    "_extra/README.log": {"path": "README.md"},
    "_extra/CNAME": {"path": "CNAME"},
    "_extra/.nojekyll": {"path": ".nojekyll"},
}

# disable author pages
# AUTHOR_SAVE_AS = ''
# AUTHORS_SAVE_AS = ''
