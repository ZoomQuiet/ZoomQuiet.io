# for ZoomQuiet.github.io

in fact my logging is long time:

- try in livejournal/blogger etc. blog srv.
- and before 2004 base [nucleuscms](http://nucleuscms.org) publish as zqstudio.org
- from 2005 , fall in love [txt2tags](http://txt2tags.org/), base [PyBlosxom](http://pyblosxom.bluesock.org/) publish as [Zoom.Quiet's PyBlosxom blogging](http://blog.zoomquiet.org/pyblosxom/)

but...

Markdown is realy easy than t2t/rST,
and more and more site support .md not .t2t/.rst

esp. github is love .md



## re-start 2014

- keep http://blog.zoomquiet.org/pyblosxom/
- start new domain zoomquiet.io
- usgae zoomquiet.github.io
- CNAME as blog.zoomquiet.oi
- base [Pelican](http://getpelican.com/) the Pythonic Static Site Generator

continue [WyTiWyG](http://wiki.woodpecker.org.cn/moin/WyTiWyG) blogging...

## usage
How to update the site contents

main loop:

1. git clone for start
1. edit some .md in `content/`
1. `fab build` for test local
1. `fab pub4github` git add->ci->push in `output/`

loop 2~4


## repo. relation

https://github.com/ZoomQuiet/ZoomQuiet.io clone in local need embded another rep.

    +- LICENSE
    +- README.md
    +- _plugins
    +- _themes
    +- content
    +- output     as https://github.com/ZoomQuiet/ZoomQuiet.github.io
    +- fabfile.py
    `- pelicanconf.py


- because github only support Jekell srv.
- but github-pages can direct publish pure html static site
- so 


### writing

- fork https://github.com/ZoomQuiet/ZoomQuiet.io into local
- cd into content/
- the sub-dir means:

        content/
            +- _extra       扩展功能文件 e.g robots.txt
            +- _files       站内文件
            +- _images      站内图片
            +- IMHO       首字母大写的是分类目录 收集对应文章
            +- ...
            `- pages        类似 about 的导航栏文档

### 文章格式

- 标准 Markdown 格式
- 以 .md 为后缀
- 文件名不得使用中文/空格/符号
- 内容模板:

    Title: 中E可以混杂的标题
    Date: 2013-12-09
    Tags: people, shanghai
    Slug: sting-chen
    Author: Zoom.Quiet

- 其中:
    - `Date:` 如果没有将使用文件的系统时间
    - `Tags:` 使用逗号作间隔, 不宜过多,建议三个为界,以人物/行为/目标领域 为方向进行定义
        - 参考: [如何规划blog的标签（tag）和分类 - 心内求法 - 博客园](http://www.cnblogs.com/holbrook/archive/2012/11/05/2755268.html)
    - `Slug:` 是实际输出的页面文件名, 建议全部小写E文, 使用中划线, 不使用特殊符号


### deploy

支持本地调试! 使用 `fabric` 进行管理, 支持的命令:

    fab 
    Available commands:

        build       编译所有页面
        pub4github  向github 真实发布文章
        reserve     重编译所有页面再启动本地服务
        serve       启动本地服务 localhost:8000


### design

基于 [pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) 深度定制

- 配置: `pelicanconf.py`
- 样式: `_themes/pelican-bootstrap3/`
- 插件: `_plugins/`


# Changelog

- 140106 base https://gitcafe.com/CPyUG/weekly init. all

