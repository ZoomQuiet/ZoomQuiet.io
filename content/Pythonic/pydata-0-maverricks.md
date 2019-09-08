Title: pydata笔记:环境配置
Date: 2014-06-03
Tags: pandas,ipython,pydata,mavericks
Slug: pydata-0-mavericks


[TOC]

## 背景

![s27157694.jpg(JPEG 图像,300x300 像素)](http://img3.douban.com/lpic/s27157694.jpg)

[利用Python进行数据分析](http://book.douban.com/subject/25779298/)

是本好书...

为什么知道这书呢? 因为翻译 [|蠎周刊 |汇集全球蠎事儿 !-)](http://weekly.pychina.org/)

经常见到各种 Pandas 配合其它纯Python 模块折腾出来的大数据可视化分析作品/文章,
而且从 [Python科学计算 (豆瓣)](http://book.douban.com/subject/7175280/) 中很早
也知道了各种 Python 在数据分析方面的方便,
所以,一直想有机会能实战性的系统折腾一下...

这书当然注意到了,虽然不是 OBP 项目组织翻译的,
但是,好书就是好书,有点小贵,

最近有了台 GALAXY TAB3, 所以,能上 Kindle 了,于是,发现 z.cn 上电子书有了,
响应 @老赵的号召,立即收入!


## 探索
正如,Python 所有领域的自学,有一个稳定,随时有反馈的环境是最重要的...

但是,作者的话,真心不能都相信哪!

    ...如果你恰好使用 Python 3.2 大部分示例是可以完整运行的
    ...
    MAC OS X 环境推荐安装 epd_free-7.3-2-macosx-i386.dmg
    ...

于是...

### pyenv

先尝试 Python 3.2 环境:

- `$ pyenv install 3.2` 成功
- `$ pyenv virtualenv --distribute 3.2 32IPy`
- `$ pyenc local 32IPy2` 
- `$ pip install ipython`,成功
- `$ pip install pandas`, 失败

然后回到书中作者的 2.7.3 环境,重新尝试

- 一样败在 `$ pip install pandas`
- 宏大的 `Matplotlib` 手工安装成功了的哪....


### EPD free

好吧,看来数据分析的系列模块也不是那么简单可以安装的,
所以,

[Enthought Python Distribution Free](https://enthought.com/products/epd/free/)

嗯嗯嗯? 

![canopy-logo](https://enthought.com/static/img/canopy-logo.png)

什么东西,不是说 `EPD free` 嘛?

直接搜索:

- epd_free-7.3-2-macosx-i386.dmg
- 果断还有: [Index of /repo/free](https://enthought.com/repo/free/)

果断下载,安装...

各种不对味儿,原来自动在 `~/.bash_profile`

    # Setting PATH for EPD_free-7.3-2
    # The orginal version is saved in .bash_profile.pysave
    PATH="/Library/Frameworks/Python.framework/Versions/Current/bin:${PATH}"
    export PATH

而且是按照系统框架来安装到 `/Library/Frameworks/Python.framework` 的
可是, Mavericks 以后,没有默认Python 了哪,俺已经同时用 `brew` 管理系统 Python,
`pyenv` 管理开发 Python ,先不说体积:

    $ du -hs /Library/Frameworks/Python.framework/Versions
    425M    /Library/Frameworks/Python.framework/Versions


居然第一个案例就跑不起来!

`import pandas` 有报错...

### Canopy
回到官方下载: [Enthought Store](https://enthought.com/store/)

老老实实的下载推荐的 `canopy-1.4.0-osx-64.dmg`
体积也从 74M 爆涨为 `235Mb`

不过,是一派标准的 MAC 软件包了,非常流畅,也有GUI 的引导界面,

然后 `~/.bash_profile` 追加的是:

    # Added by Canopy installer on 2014-06-03
    # VIRTUAL_ENV_DISABLE_PROMPT can be set to '' to make bashprompt show that Canopy is active, otherwise 1
    VIRTUAL_ENV_DISABLE_PROMPT=1 source \ 
    /Users/zoomq/Library/Enthought/Canopy_64bit/User/bin/activate

那就简单了,使用标准的 `VirtualEnv` 来包装的话,就不用将系统Python 环境永久性的迁移为
`Canopy` 的了,

简单的 在 `~/.bashrc` 定义一个别称:

    # Added by Canopy installer on 2014-06-03
    alias canopy="source \
    /Users/zoomq/Library/Enthought/Canopy_64bit/User/bin/activate"

随时调用 `canopy` 就可以进入了..


## 结论

最终拥有了和书中有一致反应的环境:

![140604-pydata-canopy.png](http://zoomq.qiniudn.com/ZQCollection/snap/140604-pydata-canopy.png)

参考:

- [osx - How to uninstall Python 2.7 on a Mac OS X 10.6.4? - Stack Overflow](http://stackoverflow.com/questions/3819449/how-to-uninstall-python-2-7-on-a-mac-os-x-10-6-4)
    - sudo rm -rf /Library/Frameworks/Python.framework/Versions/2.7
    - sudo rm -rf "/Applications/Python 2.7"
    - remove the symbolic links in /usr/local/bin that point to this python version see ls -l /usr/local/bin

- [Installing Python on Mac OS X — The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/starting/install/osx/)
    - [Installing / Updating Python on OS X | Wolf Paulus](http://wolfpaulus.com/jounal/mac/installing_python_osx/)
    - [When I upgraded my Mac to OS X Mavericks, a lot of utilities (like Python, virtualenv, Xcode) broke, and it was pretty stressful trying to get it all set back up. Hopefully this guide can spare you some of that pain.Note: I'm by no means a Linux or Mac ex](https://gist.github.com/goldsmith/7163055)


Mavericks 对 Python 框架的调整,也的确有其原由的...

当然,好书要配合好代码,

及时 fork 一个自个儿可以折腾的: [OpenBookProjects/pydata-book](https://github.com/OpenBookProjects/pydata-book)

## Changelog

- 140603 完成环境探索,总结
- 140527 ["利用Python进行数据分析" Wes McKinney, 唐学韬 (Kindle电子书)](http://www.amazon.cn/gp/product/B00KD7Q7U2/ref=oh_d__o00_details_o00__i00?ie=UTF8&psc=1)
