Title: rst2s5 小折腾
Date: 2014-05-07
Tags: MAC,S5,rst2s5,ZQ
Slug: rst2s5-upgraded

[TOC]


# 背景

[rst2s5 ~ 好用的S5生成宏 @ 2010-09-18 23:23 - Zoom.Quiet's PyBlosxom blogging](http://blog.zoomquiet.org/pyblosxom/2010/09/index.html)

所以 2011 以后所有发布的幻灯都是 rest2s5 生成的了:

[s5.zoomquiet.io](http://s5.zoomquiet.io/)

# 问题

忽然发现生成的代码颜色很奇怪,在黑色背景中,很多元素几乎看不见

# 分析

4年前的生成脚本,和最新 pygments 接口不匹配了,,,

# 解决

参考:

- [Using Pygments in ReST documents — Pygments](http://pygments.org/docs/rstdirective/)
- [Using rst for presentations](http://morgangoose.com/blog/2010/09/12/using-rst-for-presentations/)
- [rst2s5 with syntax highlighting](http://hackmap.blogspot.com/2009/10/rst2s5-with-syntax-highlighting.html)
- [python - Where can I find a gallery of Pygments CSS files - Super User](http://superuser.com/questions/374509/where-can-i-find-a-gallery-of-pygments-css-files)

对比:

- [rst2s5.py](http://matt-good.net/files/software-dev-with-trac/rst2s5)
- [rst-directive.py](http://bpgeo.googlecode.com/svn/trunk/rst2s5_template/rst-directive.py)

发现就是样式的声明问题:
于是就追加了一个参数: `style="monokai"`

    :::python
    # ...
    formatter = get_formatter_by_name('html'
    , noclasses=True
    , style="monokai"
    )

搞掂!

另外,也随手变更了一下注册的 `directive` ~ 指令:

    :::python
    # Register the directive with docutils.
    #rst.directives.register_directive('code-block', code_block)
    #rst.roles.register_local_role('code-block', code_role)
    rst.directives.register_directive('sourcecode', code_block)
    rst.roles.register_local_role('sourcecode', code_role)

这样俺在 Leo 中写:

![140507-rst2s5-source.png](http://zoomq.qiniudn.com/ZQCollection/snap/140507-rst2s5-source.png)


就可以一键生成为幻灯中的:

![140507-rst2s5-slide.png](http://zoomq.qiniudn.com/ZQCollection/snap/140507-rst2s5-slide.png)


