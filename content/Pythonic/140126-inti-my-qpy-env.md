Title: 如何自在的折腾QPy
Date: 2014-01-26 12:42
Tags: howto, qpy, pythonic, ssh, 
Slug: init-my-qpy-env
Author: Zoom.Quiet


[TOC]

## 背景

QPython 知道有两年了,是看 [Head First Python(中文版) (豆瓣)](http://book.douban.com/subject/10561367/) 时,发现竟然有 
[SL4A](http://code.google.com/p/android-scripting/)

这种神器! Google 果断是业界良心哪,
可惜: 从[Downloads](http://code.google.com/p/android-scripting/downloads/list)
可以看出 ,已经停止有一年多了,目测是 Guido 叔离开后, Python 的地位在 Google 
一落千丈就没有人折腾了.

好在旧浪两位同事, River和CF 掿起了 SL4A 的旗帜,
变成了一系列准衶器:

- [QPython - Python for Android - Google Play 上的 Andr​​oid 应用](https://play.google.com/store/apps/details?id=com.hipipal.qpyplus)
- [QPython 3 - Python3 on Android - Google Play 上的 Andr​​oid 应用](https://play.google.com/store/apps/details?id=com.hipipal.qpy3)
- [QPython Player for Android - Google Play 上的 Andr​​oid 应用](https://play.google.com/store/apps/details?id=com.hipipal.qpy)
- [QEdit - Code Editor in Pocket - Google Play 上的 Andr​​oid 应用](https://play.google.com/store/apps/details?id=com.hipipal.texteditor)

目标直指所谓的内什么,,,

而且,目测已经有国家高等教育项目中,
直接使用了 `QPython` 来作教学环境!

所以,果断要跟上用起来,,,

参考:

- [App Annie 的应用商店数据|Amazon排行榜中国 - Education - 2014年1月27日](http://www.appannie.com/apps/amazon-appstore/top/china/education/)
- [让Python在Android系统上飞一会儿:第一节 在手机上...](http://www.douban.com/group/topic/17095466/)


## 目标
哪,俺是 Pythoneer ,不是 JAVA 党,
更加是 `IDE 去死去死团` 的骨灰成员.

很辛苦的攒銭搞到了 
[FILCO Majestouch MINILA](http://news.mynavi.jp/news/2013/02/07/051/index.html)
青轴!
绝对不要回到 `一指禅` 的时代哪!!!

所以,俺要用 QPython 就是用来快速进行实用mini 应用的,
而且, 期待的开发流程, 应该完全类似现在的 web server 开发流程:

1. 本地用喜爱的编辑环境进行代码撰写 ([Sublime Text 2](http://www.sublimetext.com), [Leo](http://leoeditor.com/), etc.)
1. 一键上传手机,并自动运行
1. 在手机上真实操作,同时有远程日志可以实时观察,确认问题

以上循环


## 环境准入

对了,以下记述充斥了各种非科普性描述,
为了误入的小伙伴不被意外恶心到,得交待一下适合继续阅读的条件:

1. 42 个月, Linux/Unix 系统使用~注意!是使用不是管理体验;不然各种标准的命令行操作要死人的,,
1. 42 周的, 编程体验,不许什么語言,就是 JS 也成,起码要有一丝码感,,,
1. 42 次的, 蕃茄工作时间 的经历,至少知道什么是" [心流](http://book.douban.com/reading/12671922/)"般的专注!
1. 42 天的, 相关资料通读,相关社区的加入/旁听,,,一定要摸清楚相关主要开发人员的沟通习惯 ;-)
1. 42 小时, 的周边环境整备,熟悉工作系统以及配置好顺手的工具(git/apt/yum/brew ...)
1. 42 分钟, 当前的空闲时间,能够专注以下描述,不会片面的抽取文字就来吼俺 `图样图森破` 什么的..
1. 42 秒, 明确以上条件 `42%` 吻合,即可继续 ;-)

### 硬件
手机: 电信协议 三星 Note2 N7108ZMDMF1:

- Android 4.1.1 JRO03C
- 刷的是 MIUI-3.3.15 野生版
- CPU 四核 1.6GHz
- 内存 2G
- 存储 16G

主机: MBP 12下半年版 

- OS X 10.9.1
- Core i7 2.2GHz
- 8G 内存
- 500G 机械硬盘

湿件: 30++++++++++岁老程序猿

- 180,180,180,,,
- ASP,Basic,C,C++,Clojure,Erlang,Forth,Factor,Go,Haskell,JS,JAVA,Lisp,Node,PHP,Python,Pascal,XSLT,REBOL,Rust,,,少量经验
- 精通26字母, Cnglish 熟练


## 探索

根据策划的流程,在原作者的帮助下,进行了高强度的折腾,
经过连续 27 小时探索,基本爽了起来:

### 上传
Android 呢,就是 Linux 哪,当然应该用 `scp` 安全上传了!

目测,要依次解决:

1. 手机上的 `SSH` 守护在哪儿,怎么启动
1. 脚本应该上传到哪儿 QPython 才能识别?



#### SSH
搜索就有:

- [Android tips](http://gailly.net/android/android-tips.html)
- [10 Android Apps for Linux Server Admins - ConnectBot, QuickSSHd, SwiFTP, AndFTP, Wyse PocketCloud - Reviews - LinuxPlanet](http://www.linuxplanet.com/linuxplanet/reviews/7301/1)
- [SSHDroid(SSH Server for Android)通过PC或命令连接android - bugeasy - 开源中国社区](http://my.oschina.net/winHerson/blog/84716)

经过快速的尝试,
明确 `SSHDroid` 最简洁可用,
那就上:

![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140127-qpy-sshdroid.jpg)

- 安装,配置都没有什么可说的
- 只是,非专业版,只能用口令登录,先忍着
- 扩展一点点儿从 [Hello, QPython! « one-time blog](http://onetimeblog.logdown.com/posts/2014/01/23/first-program-in-qpython) 来的代码,成 `hollo.py`

```
import androidhelper
droid = androidhelper.Android()
droid.makeToast(u'Hello, Username!是也乎 ;-)')
```

上传到哪儿呢?!

快速翻找一下,明确几个关键路径:

- `SSHDroid`起始可写根:

  - `/data/data/berserker.android.apps.sshdroid/home/`
  - 即: `cd ~` 回到的目录

- QPython 环境分:

  - 只读执行文件起点 `/data/data/com.hipipal.qpyplus/files/bin/`
  - 可写资源起点以及目录意义:

```
/storage/sdcard0/com.hipipal.qpyplus/
    +- cache         
    +- lib        各Python版本的库安装入口 
    +- projects   俺的QPy 项目入口
    +- scripts    俺的QPy 脚本入口
```


#### BusyBox

等等! SSH 上来后,各种不适应,这什么 shell 环境哪,连 `less`, `tail`, `vi` 都没有
好意思说自个儿是 `Linux` 嘛?!

搜索才知道,这货叫 `ash`

- 躲在 `/system/bin/sh` 基本上什么也不会作
- 所以,程序猿有 [BusyBox](http://www.busybox.net/)
- 一安装,批量将大堆习惯的工具,灌到 `system/xbin/`

![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140126-qpy-busybox-tail.jpg)


这样,才能远程观察, QPython 项目目录中,
若隐若现的 `.run.log` 明显发生什么问题,
快速增补一行:

    :::python
    # -*- coding: utf-8 -*-
    import androidhelper
    droid = androidhelper.Android()
    droid.makeToast(u'Hello, Username!是也乎 ;-)')


就能运行成功,跳出最简单的发布公告框了!

![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140126-qpy-hollo.jpg)



### 运行

好了,进入下一个阶段: `怎么让 QPyhon 如系统命令一样在 ash 环境中调用我们的脚本?`

目测,要依次解决:

1. ash 环境变量是否兼容 QPython?
1. ash 环境变量如果不兼容 QPython 怎么配置?

将刚刚测试明确可用的脚本从 shell 环境中调用一下:

    :::bash
    # cd /storage/sdcard0/com.hipipal.qpyplus/projects/chaos/ 
    # /data/data/com.hipipal.qpyplus/files/bin/python hollo.py

    Could not find platform independent libraries <prefix>
    Consider setting $PYTHONHOME to <prefix>[:<exec_prefix>]
    ImportError: No module named site

果断没有那么简单, 检查一下系统环境:

    :::shell
    _=/system/xbin/env
    RANDOM=25396
    ANDROID_DATA=/data
    BOOTCLASSPATH=/system/framework/core.jar:/system/framework/core-junit.jar:/system/framework/bouncycastle.jar:/system/framework/ext.jar:/system/framework/framework.jar:/system/framework/framework2.jar:/system/framework/android.policy.jar:/system/framework/services.jar:/system/framework/apache-xml.jar:/system/framework/sec_edm.jar:/system/framework/seccamera.jar
    PATH=/data/data/berserker.android.apps.sshdroid/dropbear:/usr/bin:/usr/sbin:/bin:/sbin:/system/sbin:/system/bin:/system/xbin:/system/xbin/bb:/data/local/bin
    ANDROID_ROOT=/system
    USER=root
    LOGNAME=root
    ANDROID_PROPERTY_WORKSPACE=9,66560
    EXTERNAL_STORAGE=/storage/sdcard0
    ANDROID_ASSETS=/system/app
    SHELL=/system/bin/sh
    TERM=vt100
    SSH_TTY=/dev/pts/1
    SSH_CONNECTION=::ffff:192.168.0.103 64228 ::ffff:192.168.0.100 22
    HOME=/data/data/berserker.android.apps.sshdroid/home
    ANDROID_BOOTLOGO=1


跟 Python 没一毛钱关系,怪不得跑不了;
吼了俩位爷,才知道: [QPython Hackers](http://wiki.qpython.org/hacker/)
果断是依赖大堆系统环境变量的,
以往能在桌面运行起来,
也是通过 `大JAVA` 的相关接口,临时声明的!

那就好办了,照此办理:
[gen_qpy_env.py](https://gist.github.com/ZoomQuiet/8642464)

`注意:` 这货一定要加载到 QPython 中,用脚本形式来跑,
如果也是从后台 shell 环境中跑,是获得不了主要关键参数的!

![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140126-qpy-gen-profile.jpg)


然后!? 肿么,让 shell 环境每次都能自动加载上这堆配置?

综合,搜索来的相关说明:

- [[转]linux虚拟内核文件系统介绍 - shy.ang - 博客园](http://www.cnblogs.com/shyang--TechBlogs/archive/2011/10/27/2226664.html)
- [Mount Android System Partition With Read/Rrite Access](http://www.xdracco.net/mount-android-system-partition-with-readwrite-access/)
- [Android tips](http://gailly.net/android/android-tips.html) 

经过尝试,明确这么来:

    :::bash
    # mount -o remount,rw /dev/block/mtdblock3 /system
    # ln -s /storage/sdcard0/com.hipipal.qpyplus/projects/qpy_profile /etc/profile
    # mount -o remount,ro /dev/block/mtdblock3 /system


再关闭,重启 `SSHDroid` 后,远程登入,测试:

![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140126-qpy-this-zen.png)


然后,远程人工从 shell 调用

    :::shell
    # cd /storage/sdcard0/com.hipipal.qpyplus/projects/chaos/ 
    # /data/data/com.hipipal.qpyplus/files/bin/python hollo.py


手机无论在什么桌面,都能跳出来俺的 `hollo.py` 运行结果:

![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140126-qpy-console-hollo.jpg)


然后,本地,习惯性的,就可以用 [tmux](http://tmux.sourceforge.net/) 同时
观察/管理本地以及远程的开发/测试/运行情况了:

![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140127-qpy-tumx.png)


#### BETA乱入
作者看俺这么努力的折腾从内部机密放送俺最新开发版本,兴奋的安装上:

![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140127-qpy-new-version.jpg)

然后,再运行...

    :::shell
    Traceback (most recent call last):
      File "/storage/sdcard0/com.hipipal.qpyplus/projects/chaos/hollo.py", line 3, in <module>
        droid = androidhelper.Android()
      File "tubelib/sl4a.py", line 34, in __init__
        self.conn = socket.create_connection(addr)
      File "/home/river/android-sdk/workplace/python-for-android/build/python-install/lib/python2.7/socket.py", line 571, in create_connection
    socket.error: [Errno 111] Connection refused


`/home/river/android-sdk/workplace` 囧rz...

什么东西?! 怎么超出来原作的本地目录了?!

再问,才知道:

- `AP_HANDSHAKE=5873cf77-e70b-4887-a8b2-28b7db3c408e`
- 类似 `AP_` 前缀的系列环境变量是随发行版,每次不同的,
- 必须匹配上,否则,系统找不到,就只能使用缓存的不知哪儿的路径了...

所以,必须:

- 从项目中打开脚本:
![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140127-qpy-env-proj.jpg)

- 从 QEditor 中运行
![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140127-qpy-env-run.jpg)

- 在 console 中生成:
![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140127-qpy-env-gen-again.jpg)


#### QPython头声明
参考: [Programming Guide](http://wiki.qpython.org/doc/program_guide/#qpython-header)

脚本第一行的不同声明,将由 QPython 智能识别给予不同的运行环境,一定要理解:

- `#qpy:console` , 是指运行环境为 QPython 的命令行环境
- `#qpy:2` 是指运行环境为 QPython 2 的命令行环境
- `#qpy:3` 是指运行环境为 QPython 3 的命令行环境
- 没有 `#qpy:*` 的是指基于 [SL4A](http://kylelk.github.io/html-examples/androidhelper.html) 的GUI 依赖环境
- 2014 追加支持的

    #qpy:webapp:<app title>
    #qpy:fullscreen
    #qpy://localhost:8080
    """
    Launching the web service on localhost:8080 
    without android titlebar (fullscreen)
    """



### 自动
好了,进入最后一个阶段: `怎么让所有的上传->配置->运行->日志收集 全部自动化一键完成?`

目测,要依次解决:

1. 自动上传?!(怎么通过公匙的部署,来达到无口令远程登录手机?)
1. 自动运行手机端的脚本?!
1. 自动收集日志?

问题一,参考:

- [python - How to get Fabric to automatically (instead of user-interactively) interact with shell commands? Combine with pexpect? - Stack Overflow](http://stackoverflow.com/questions/8291380/how-to-get-fabric-to-automatically-instead-of-user-interactively-interact-with/10007635#10007635)
- [Fexpect adds answering to prompts to fabric with use of pexpect](http://ilogue.com/jasper/blog/fexpect--dealing-with-prompts-in-fabric-with-pexpect/)
- [pexpect - Noah.org](http://www.noah.org/wiki/pexpect)

总之,对口令,没有什么好办法,大家都是通过获取反馈,匹配期待,自动输入...

只是,这样折腾,很扯蛋! 用口令登录的安全隐患怎么强调都不过份!

何况,通过 RSA/DSA 密匙对加密,公匙部署,自动双向加密,
安定,稳定,方便的用了多少年?!

没理由在 Android 这儿栽了哪!
果断的: 

- 先将本地公匙用口令登录的方式推上手机
- 然后,[sshdroid-cracked.apk](http://0.zoomquiet.top/CPyUG/QPython/apk/berserker.android.apps.sshdroid-cracked-signed.apk)
- 然后,就没有然后了 ;-)

只是,唯一的问题:
- 因为 SSH 服务端切换了, 导致 SSH 认证冲突,要清除对应的配置行
- 每次都要全部清除,或是人工清除?
- 不用这么 Naive ,参考:[SSH Warning: the RSA host key for differs from the key for the IP address - zhangp专栏](http://floss.qiniudn.com/data/20130327153058/index.html)

一行解决:

    :::sh
    $ sed -i -e '36d' ~/.ssh/known_hosts



#### [Fabric](http://docs.fabfile.org/en/1.5/index.html#usage-documentation)
非 `C/S` 结构的脚本化自动部署工具!

嘦在本地安装好[Fabric](http://docs.fabfile.org/en/1.5/index.html#usage-documentation)
再在本地工程目录中放一个 `fabfile.py`, 就可以:


    :::shell
    $ fab ?

    Warning: Command(s) not found:
        ?

    Available commands:

        env         print Android sys. env
        genenv      gen qpy need env into: /storage/sdcard0/com.hipipal.qpyplus/projects/qpy_profile
        pushproj    scp all .py into Android QPython projects dir
        qpy         main develop tools, auto upload and running in Android
        qpy_run_it  fab qpy_run_it:script=MY.py
        uname       print Android sys. info.


日常,无论折腾多少个项目,都可以统一部署此脚本到目录中,
[Fabric for QPython auto upload/running script/collect log etc... from local through SSH](https://gist.github.com/ZoomQuiet/8645207)

只要定制一两只参数, 平时的开发流程就变成了:

1. 本地用喜爱的编辑环境进行代码撰写 ([Sublime Text 2](http://www.sublimetext.com), [Leo](http://leoeditor.com/), etc.)
1. `fab qpy:script=当前调试的主脚本.py` 一键上传手机,并自动运行
1. 在手机上真实操作,明确效果


#### 日志

目测同最初设想的理想开发流程相比:

    :::text
    1. 本地用喜爱的编辑环境进行代码撰写
    2. 一键上传手机,并自动运行
    3. 在手机上真实操作,同时有远程日志可以实时观察,确认问题


只差一个运行日志的实时观察了哪,,,

本来想着很简洁的:

- [tmux](http://tmux.sourceforge.net/) 再多开个窗口
- `tail -f /PATH/2/MY/QPY/PROJECT/.run.log` 就完事儿的哪!

结果,不得不提交个 Issue:

[.run.log is odd · Issue #2 · qpython-android/QPython.org](https://github.com/qpython-android/QPython.org/issues/2)


## 结论

虽然, 最后集中成了一份儿 
[fabfile.py](https://gist.github.com/ZoomQuiet/8645207)
脚本,但是涉及的工具还是很多的,
所以, 整体上,最终可用的组合关系是:

    [[Android in mobile]]
        +- /etc/profile -> ln -s
        |                  V
        |                  V
        |    /storage/sdcard0/com.hipipal.qpyplus/projects/qpy_profil
        |                  ^
        |                  ^
        +- QPython -> gen_qpy_env.py
        |    .../projects/MyProject
        |             ^
        |             ^
        |             ^
        `- SSHDriod + id_rsa.pub
                  ^
                  ^   scp,and run()
                  ^
            /-> base fabfile.py
            |
        +- Fabric
        +- pip
        +- Python
        |
    [[MBP in local]]
    all in same wifi net domain



### TODO
然后, 有个比较顺心的 QPython 折腾环境了,
就可以进一步的折腾各种想玩/能玩能玩的了!


### pip
没有 pip 的世界是艰难的世界,所以,,,

[Installation — pip 1.5.2 documentation](http://www.pip-installer.org/en/latest/installing.html)


    :::bash
    # python get-pip.py
    Traceback (most recent call last):
      File "get-pip.py", line 21343, in <module>
        import bz2
    ImportError: No module named bz2


那么回到老方式, `setuptools->easy_install pip->pip`
[setuptools 2.1 : Python Package Index](https://pypi.python.org/pypi/setuptools#installation-instructions)

    :::bash
    # python ez_setup.py
    Downloading https://pypi.python.org/packages/source/s/setuptools/setuptools-2.1.tar.gz
    Extracting in /storage/sdcard0/com.hipipal.qpyplus/cache/tmpCpG6N8
    Now working in /storage/sdcard0/com.hipipal.qpyplus/cache/tmpCpG6N8/setuptools-2.1
    Installing Setuptools
    Traceback (most recent call last):
      File "setup.py", line 28, in <module>
        from setuptools.command.test import test as _test
      File "/storage/sdcard0/com.hipipal.qpyplus/cache/tmpCpG6N8/setuptools-2.1/setuptools/command/test.py", line 6, in <module>
        from unittest import TestLoader, main
    ImportError: No module named unittest
    Something went wrong during the installation.
    See the error message above.


好吧,只能先放下了, 
但是,没有 pip 怎么安装上 [Mercurial](http://mercurial.selenic.com/) 呢?

有了 [Hg](http://mercurial.selenic.com/) 才真正海阔天空了呢...


### RESTful "OneRing"

不知道大家记得 [OneRing](http://code.google.com/p/onering-desktop/wiki/OneRing)
卟?!

豆瓣首席架构师/布道官/CTO 洪教授 亲手玩的项目:

    :::text
    跨平台的桌面应用开发库,
    使用HTML5+CSS3制作用户界面,
    用Javascript编写交互逻辑,
    同时提供用写web后端的技术编写后台逻辑!



但素,现在有了 QPython 完全可以0成本山寨一个移动版的 MyRing 了哪:

呼应各种本地的 [RESTful](http://floss.qiniudn.com/data/20110818160723/index.html)
请求,总是要有一个内置的web 服务的,

当然上 
[Bottle](http://bottlepy.org/)
了,只有一个文件的越级微框架,不用安装,随项目目录发布就好.

    :::python
    #qpy:console
    from bottle import route, run, template

    @route('/hello/<name>')
    def index(name):
        return template('<b>Hello {{name}}</b>!', name=name)

    run(host='localhost', port=8080)


因为是要守护在后台长期运行的,所以用 `#qpy:console` 标定

可惜:

![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140126-qpy-bottle-error.jpg)

原来:

![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140126-qpy-install-wsgi.jpg)

然后:

![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140126-qpy-bottle-running.jpg)

没有然后:

![snap4qpy](http://0.zoomquiet.top/CPyUG/QPython/snap/140126-qpy-bottle-hello.jpg)


哈哈! 一切如愿!


## 专题体例:
QPy 的大妈们曰了:  每个专题应该包括 

    Introduction, 
    getting start(include sample better), 
    packages, 
    videos (searched result from youtube or directly video link )


好吧,慢慢来,,,下次专注 Bottle 结合 QPython 实现可用随身小工具.

## 时间帐单:

简单回顾一下整个从完全小白到折腾出当前扫盲文章的时间投入:

+ 1H: 动心,所有相关资料收集,概览
+ 2H: SSH 登录成功, 不用口令,未果
+ 2H: env 确认问题,解决问题
+ 1H: BusyBox 熟悉手机上的shell 环境
+ 8H: Fabric 打通, 还是env 问题,以及版本变化后要重新生成 env 配置
+ 4H: 整理为文章

`18H` 总计可统计的大块时间, 其它基本有几乎相同的沟通时间,用在
通过 微信/邮件/github 等等方式沟通


## Changelog

- 171011 ZQ 迁移到 .io 私人域名中
    + 官方文档-> [Welcome to read the QPython guide\! — QPython 0\.9 documentation](http://www.qpython.org/document.html)
- 140127 ZQ 增补所有细节
- 140126 ZQ 创建

