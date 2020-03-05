Title: from Lion jump into Mavericks
Date: 2013-12-30
Tags: MAC,Leo,Pyenv,ZQ
Slug: jump-into-mavericks


[TOC]

# 为毛
得承认是被 老池的文章忽悠到了, 
而且, 10.9 免费了, 进一步的通过OS 提高了电池/内存的使用效率,
最关键的,在 [无责任报道~ECUG2013Con](http://techparty.org/events/2013/12/29/et-ecugcon-sz/) 中提及过的,
有好基友,已经折腾过,明确从 10.7 直升没有问题!

于是一个月黑风高的晚上...

# 回顾

宏观上没有想象的复杂,因为真心作到了零配置!
几乎所有非第三方的配置,都继承了下来不用折腾!

唯三的折腾:

1. Python 环境
2. Qt 环境
3. sshfs


严正推荐:

[Mavericksでbrew upgradeしたらハマった話](file:///Users/zoomq/mnt/%E5%BF%AB%E7%9B%98/zScrapBook/ZqFLOSS/data/20131230190257/index.html)

等等日文的相关纪要非常实在,直觉,顺序合理,值得,多参考.


## Python + Qt for Leo

大家知道俺是 [文学化编程](http://wiki.woodpecker.org.cn/moin/LiterateProgramming)
的拥趸,
所以,一直使用 [Leo](http://wiki.woodpecker.org.cn/moin/LeoEnvironment)
作为主要编程环境的,

10.9 以后 Python 不内置安装了,
Qt 当然从来也没有内置过.
所以,

### Python

当然,系统的用 `brew install python` 了,

而其它各种项目开发时,就要综合使用

#### Pyenv+VirtualEnv

Pyenv 是这样一种神器:

  完全的面向shell
  通过环境变量的自动配置
  形成复合Python版本共存

VirtualEnv 有 Pyenv 的插件
所以,可以利用已安装好的环境,快速复制出项目专用的,
结果,引发了滥用,特别舒服的那种:

```bash
$ pyenv versions
* system (set by /Users/zoomq/.pyenv/version)
  2.7.3
  2.7.5
  2.7.6
  273SAE
  275lbTC
  275pelican
  276SphinxOBP
  276chaos
  276uliweb
  3.2
  3.3.2
  32IPy
  ipynotebook
  pypy-2.2.1
  pypy221chaos

```

主要遇到的问题是:

    ==> Installing python3
    ==> Downloading http://python.org/ftp/python/3.3.3/Python-3.3.3.tar.bz2
    ######################################################################## 100.0%
    ==> ./configure --prefix=/usr/local/Cellar/python3/3.3.3 --enable-ipv6 --datarootdir=/usr/local/Cellar/python3/3.3.3/share --datadir=/usr/lo
    ==> make
    ==> make install PYTHONAPPSDIR=/usr/local/Cellar/python3/3.3.3
    ==> make frameworkinstallextras PYTHONAPPSDIR=/usr/local/Cellar/python3/3.3.3/share/python3
    Error in sitecustomize; set PYTHONVERBOSE for traceback:
    ValueError: list.remove(x): x not in list
    Error in sitecustomize; set PYTHONVERBOSE for traceback:
    ValueError: list.remove(x): x not in list
    Error in sitecustomize; set PYTHONVERBOSE for traceback:
    ValueError: list.remove(x): x not in list
    Error in sitecustomize; set PYTHONVERBOSE for traceback:
    ValueError: list.remove(x): x not in list
    Error in sitecustomize; set PYTHONVERBOSE for traceback:
    ValueError: list.remove(x): x not in list
    Error in sitecustomize; set PYTHONVERBOSE for traceback:
    ValueError: list.remove(x): x not in list
    Error in sitecustomize; set PYTHONVERBOSE for traceback:
    ValueError: list.remove(x): x not in list
    Error in sitecustomize; set PYTHONVERBOSE for traceback:
    ValueError: list.remove(x): x not in list
    Error in sitecustomize; set PYTHONVERBOSE for traceback:
    ValueError: list.remove(x): x not in list
    Error in sitecustomize; set PYTHONVERBOSE for traceback:
    ValueError: list.remove(x): x not in list


指定具体版本,尝试,直到可以顺利安装出可用的就好.

严正表扬一下 'Yamashita, Yuu`

- [How to config pyenv's pip ? · Issue #95 · yyuu/pyenv](https://github.com/yyuu/pyenv/issues/95#issuecomment-31392999)
- 绝对认真的回答了俺的提问,虽然不了了之,但是,一个常用工具的作者,可以如此关注一个不是问题的问题,实在太勤勉了,必须学习!


### Qt for Leo

参考:

- [About X11 and OS X](http://support.apple.com/kb/HT5293)
- [XQuartz](http://xquartz.macosforge.org/landing/)

以及:

```bash
$ brew install pyqt
==> Downloading http://downloads.sf.net/project/pyqt/PyQt4/PyQt-4.10.3/PyQt-mac-gpl-4.10.3.tar.gz
Already downloaded: /Library/Caches/Homebrew/pyqt-4.10.3.tar.gz
==> Patching
patching file configure.py
==> /usr/local/opt/python/bin/python2 configure.py --confirm-license --bindir=/usr/local/Cellar/pyqt/4.10.3/bin --destdir=/usr/local/Cellar/
Error: Unable to find the qmake configuration file
/usr/local/Cellar/qt/4.8.5/mkspecs/unsupported/macx-clang-libc++/qmake.conf.
Use the QMAKESPEC environment variable to specify the correct platform.
Determining the layout of your Qt installation...

READ THIS: https://github.com/Homebrew/homebrew/wiki/troubleshooting
```

多多 Google 吧,很标准的环境驱动, Qt 官方提供了的,

然后, Leo 只是一堆 Py 脚本下载下来,
修订一下别名指向就好:


```bash
# ~/.bashrc for running Leo
alias leolanch="python /opt/bin/leo/launchLeo.py >> /dev/null 2>&1 &"
```

## 伟光大的 sshfs


    $ brew link fuse4x
    Linking /usr/local/Cellar/fuse4x/0.9.2... Warning: Could not link fuse4x. Unlinking...

    Error: Could not symlink file: /usr/local/Cellar/fuse4x/0.9.2/lib/pkgconfig/fuse.pc
    Target /usr/local/lib/pkgconfig/fuse.pc already exists. You may need to delete it.
    To force the link and overwrite all other conflicting files, do:
      brew link --overwrite formula_name

    To list all files that would be deleted:
      brew link --overwrite --dry-run formula_name

    zoomq @ MBP111216ZQ in /usr/local/lib
    $ brew link --overwrite fuse4x
    Linking /usr/local/Cellar/fuse4x/0.9.2... 7 symlinks created


    $ brew install osxfuse
    ==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/osxfuse-2.6.2.mavericks.bottle.tar.gz
    ==> Pouring osxfuse-2.6.2.mavericks.bottle.tar.gz
    ==> Caveats
    If upgrading from a previous version of osxfuse, the previous kernel extension
    will need to be unloaded before installing the new version. First, check that
    no FUSE-based file systems are running:

      mount -t osxfusefs

    Unmount all FUSE file systems and then unload the kernel extension:

      sudo kextunload -b com.github.osxfuse.filesystems.osxfusefs

    The new osxfuse file system bundle needs to be installed by the root user:

      sudo /bin/cp -RfX /usr/local/Cellar/osxfuse/2.6.2/Library/Filesystems/osxfusefs.fs /Library/Filesystems
      sudo chmod +s /Library/Filesystems/osxfusefs.fs/Support/load_osxfusefs
    ==> Summary
    🍺  /usr/local/Cellar/osxfuse/2.6.2: 84 files, 5.0M


具体哪个管用,俺也没整明白,
反正,怎么折腾,
都是可以正当加载上 `Plan` 的内核库,
然后就可以对家庭服务器的所有硬盘,远程加载为本地目录了..



# Changelog

- 140616 再次精简,算是发布
- 140505 快速简述完成
- 140110 起意,总结
