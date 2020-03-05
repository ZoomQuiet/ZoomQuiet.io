Title: jump into SSD with Yoesmite
Date: 2015-04-09
Tags: MAC,Leo,Pyenv,ZQ
Slug: jump-into-ssd


[TOC]

# 为毛
不解释, 人家都免费给你升级了哪!

# 新梗
~ 嗯哼,各种关键记要,不进行解释了...

## npm

    $ brew install npm
    ==> Downloading https://homebrew.bintray.com/bottles/node-0.12.2_1.yosemite.bottle.tar.gz
    ######################################################################## 100.0%
    ==> Pouring node-0.12.2_1.yosemite.bottle.tar.gz
    ==> Caveats
    If you update npm itself, do NOT use the npm update command.
    The upstream-recommended way to update npm is:
      npm install -g npm@latest

Bash completion has been installed to:
  /usr/local/etc/bash_completion.d


`是也乎:` 后来也全部升级为 **nvm** 了

## subl
~ [sublime-text - 如何在mac中用命令行时用sublime打开文件 - SegmentFault](https://segmentfault.com/q/1010000002397241)

> sudo ln -s "/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl" /usr/bin/subl

## /User

    $ sudo mv /Users /Users_SSD
    $ sudo ln -s /Volumes/Macintosh\ HD/Users/ Users

### AMD-Action:authenticate:SP
~ 为了复用原先的配置,结果引发了这个大问题!



参考: [Grh.am - Pesky "AMD-Action:authenticate:SP" and its Fix](https://grh.am/2015/amd-action-authenticate/)

最后还是小心的对应折腾了一下:

- 将 `Users/Shared` 中的全部内容 `ditto` 到 SSD 中
- 其它的目录,逐一 `ln -s` 过去

这样才好:

    /Users༽
    ༆  ls -1l
    Guest -> ../Users_SSD/Guest/
    Shared
    zoomq -> /Volumes/MacintoshHD/Users/zoomq/
    ...


## XCode 


    /Volumes/Macintosh\ HD/Applications/Xcode.app/
    $ xcode-select --switch /Applications/Xcode.app


## svn


    $ brew install subversion
    ==> Installing dependencies for subversion: openssl, apr-util, readline, sqlite, scons
    ==> Installing subversion dependency: openssl
    ==> Downloading https://www.openssl.org/source/openssl-1.0.2a.tar.gz
    Already downloaded: /Library/Caches/Homebrew/openssl-1.0.2a-1.tar.gz
    ==> perl ./Configure --prefix=/opt/bin/homebrew/Cellar/openssl/1.0.2a-1 --openssldir=/Volumes/Macintosh HD
    ==> make depend
    ==> make
    ==> make test
    ==> make install MANDIR=/opt/bin/homebrew/Cellar/openssl/1.0.2a-1/share/man MANSUFFIX=ssl
    installing CA.sh
    usage: cp [-R [-H | -L | -P]] [-fi | -n] [-apvX] source_file target_file
           cp [-R [-H | -L | -P]] [-fi | -n] [-apvX] source_file ... target_directory
    make[1]: *** [install] Error 64
    make: *** [install_sw] Error 1

READ THIS: https://git.io/brew-troubleshooting

These open issues may also help:
openssl: apply yosemite certificate fix (https://github.com/Homebrew/homebrew/pull/38495)
problems with cert verification by openssl on 10.10.3 (https://github.com/Homebrew/homebrew/issues/38491)
Installing Elixir fails due to OpenSSL errors. (https://github.com/Homebrew/homebrew/issues/33218)
problem with Python 2.7.9 and OpenSSL 1.0.2 (https://github.com/Homebrew/homebrew/issues/38226)


- 参考: [Apache Subversion Binary Packages](http://subversion.apache.org/packages.html#osx)
- Flink/Homebrew 都安装不能
- 只好使用: [WANdisco](http://www.wandisco.com/subversion/download#osx)
  + Subversion-Client-1.8.10_10.10.x
  + 安装成功

# 老梗


## 输入法

## brew

## Leo


The sip-dir for Python is /Volumes/Macintosh HD/Users/zoomq/share/sip.

Python modules have been installed and Homebrew's site-packages is not
in your Python sys.path, so you will not be able to import the modules
this formula installed. If you plan to develop with these modules,
please run:

      mkdir -p /Users/zoomq/Library/Python/2.7/lib/python/site-packages
      echo 'import site; site.addsitedir("/Volumes/Macintosh HD/Users/zoomq/lib/python2.7/site-packages")' >> /Users/zoomq/Library/Python/2.7/lib/python/site-packages/homebrew.pth
    ==> Summary
    🍺  /opt/bin/homebrew/Cellar/sip/4.16.5: 10 files, 864K, built in 5 seconds


    $ brew install pyqt
    ==> Installing pyqt dependency: qt
    ==> Downloading https://download.qt.io/official_releases/qt/4.8/4.8.6/qt-everywhere-opensource-src-4.8.6.tgz


    $ brew install pyqt
    ==> Downloading https://downloads.sf.net/project/pyqt/PyQt4/PyQt-4.11.3/PyQt-mac-gpl-4.11.3.tar.gz
    Already downloaded: /Library/Caches/Homebrew/pyqt-4.11.3.tar.gz
    ==> python configure.py --confirm-license --bindir=/opt/bin/homebrew/Cellar/pyqt/4.11.3/bin --destdir=/opt

    Error: /Volumes/Macintosh HD/Users/zoomq/opt/qt/bin/qmake failed to create a
    makefile. Make sure you have a working Qt qmake on your PATH or use the -q
    argument to explicitly specify a working Qt qmake.
    Determining the layout of your Qt installation...

    READ THIS: https://git.io/brew-troubleshooting

    /System/Library/Frameworks/Ruby.framework/Versions/2.0/usr/lib/ruby/2.0.0/net/http.rb:878:in `initialize': Failed to connect to: https://api.github.com/search/issues?q=pyqt+repo:Homebrew/homebrew+in:title+state:open&per_page=100 (GitHub::Error)
    getaddrinfo: nodename nor servname provided, or not known

    $ brew search qmake
    No formula found for "qmake".
    Searching pull requests...
    Closed pull requests:
    qmake gets installed by QT (https://github.com/Homebrew/homebrew/pull/31336)
    Added patch for XCode4 support for qmake. (https://github.com/Homebrew/homebrew/pull/10475)
    PyQT5.rb Specify qt5 version of qmake. (https://github.com/Homebrew/homebrew/pull/27059)
    PyQt: patch to fix handling of qmake inline comments (https://github.com/Homebrew/homebrew/pull/25225)
    qscintilla2: define 10.9 qmake make spec for lib and python module (https://github.com/Homebrew/homebrew/pull/25882)


- 先安装 [XQuartz](http://xquartz.macosforge.org/landing/)
- 重启

再:


    $ brew install pyqt
    ==> Installing pyqt dependency: qt
    ==> Downloading https://download.qt.io/official_releases/qt/4.8/4.8.6/qt-everywhere-opensource-src-4.8.6.t
    Already downloaded: /Library/Caches/Homebrew/qt-4.8.6.tar.gz
    ==> Downloading https://raw.githubusercontent.com/DomT4/scripts/440e3cafde5bf6ec6f50cd28fa5bf89c280f1b53/H
    Already downloaded: /Library/Caches/Homebrew/qt--patch-57246a33460246118a1fab7460c79f2077d3a929.diff
    ==> Patching
    patching file src/gui/dialogs/qcolordialog_mac.mm
    patching file src/gui/dialogs/qfiledialog_mac.mm
    patching file src/gui/dialogs/qfontdialog_mac.mm
    patching file src/gui/kernel/qapplication_mac.mm
    patching file src/gui/kernel/qcocoaapplication_mac.mm
    patching file src/gui/kernel/qcocoaapplicationdelegate_mac.mm
    Hunk #4 succeeded at 295 (offset -13 lines).
    Hunk #5 succeeded at 342 (offset -13 lines).
    patching file src/gui/kernel/qcocoaapplicationdelegate_mac_p.h
    patching file src/gui/kernel/qcocoamenuloader_mac.mm
    patching file src/gui/kernel/qcocoasharedwindowmethods_mac_p.h
    patching file src/gui/kernel/qeventdispatcher_mac.mm
    patching file src/gui/kernel/qt_cocoa_helpers_mac.mm
    patching file src/gui/kernel/qwidget_mac.mm
    patching file src/gui/styles/qmacstyle_mac.mm
    patching file src/gui/util/qsystemtrayicon_mac.mm
    patching file src/gui/widgets/qcocoamenu_mac.mm
    patching file src/gui/widgets/qmenu_mac.mm
    ==> ./configure -prefix /opt/bin/homebrew/Cellar/qt/4.8.6 -system-zlib -qt-libtiff -qt-libpng -qt-libjpeg
    ==> make


    $ which qmake
    /Volumes/Macintosh HD/Users/zoomq/bin/qmake


    $ /opt/bin/homebrew/Cellar/qt/4.8.6/bin/qmake -v
    QMake version 2.01a
    Using Qt version 4.8.6 in /opt/bin/homebrew/Cellar/qt/4.8.6/lib

    $ qmake -v
    QMake version 2.01a
    Using Qt version 4.8.6 in /opt/bin/homebrew/Cellar/qt/4.8.6/lib


哈哈!!!上百M 的怪物哪...


### 手编 Qt 
- [Developing PyQt4 Applications in Mac OS X | Core Dump](http://amjith.blogspot.com/2010/09/developing-pyqt4-applications-in-mac-os.html)

## 150416 try again

删除 /opt/bin/homebrew 的非常安装


    $ brew install qt sip pyqt
    ==> Downloading https://homebrew.bintray.com/bottles/qt-4.8.6.yosemite.bottle.6.tar.gz
    ######################################################################## 100.0%
    ==> Pouring qt-4.8.6.yosemite.bottle.6.tar.gz
    ==> Caveats
    We agreed to the Qt opensource license for you.
    If this is unacceptable you should uninstall.

    .app bundles were installed.
    Run `brew linkapps qt` to symlink these to /Applications.
    ==> Summary
    🍺  /usr/local/Cellar/qt/4.8.6: 2790 files, 122M


...


    ==> ./configure --prefix=/usr/local/Cellar/python/2.7.9 --enable-ipv6 --datarootdir=/usr/local/Cellar/pyth
    ==> make
    ==> make install PYTHONAPPSDIR=/usr/local/Cellar/python/2.7.9
    ==> make frameworkinstallextras PYTHONAPPSDIR=/usr/local/Cellar/python/2.7.9/share/python
    ==> Downloading https://pypi.python.org/packages/source/s/setuptools/setuptools-15.0.tar.gz
    ######################################################################## 100.0%
    ==> Downloading https://pypi.python.org/packages/source/p/pip/pip-6.1.0.tar.gz
    ######################################################################## 100.0%
    ==> Caveats
    Pip and setuptools have been installed. To update them
      pip install --upgrade pip setuptools

    You can install Python packages with
      pip install <package>

    They will install into the site-package directory
      /usr/local/lib/python2.7/site-packages

    See: https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Homebrew-and-Python.md

    .app bundles were installed.
    Run `brew linkapps python` to symlink these to /Applications.

    ...

    ==> Pouring sip-4.16.5.yosemite.bottle.1.tar.gz
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    AttributeError: 'module' object has no attribute 'getusersitepackages'
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    AttributeError: 'module' object has no attribute 'getusersitepackages'
    ==> Caveats
    The sip-dir for Python is /usr/local/share/sip.

    Python modules have been installed and Homebrew's site-packages is not
    in your Python sys.path, so you will not be able to import the modules
    this formula installed. If you plan to develop with these modules,
    please run:
      mkdir -p
      echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> homebrew.pth
    ==> Summary
    🍺  /usr/local/Cellar/sip/4.16.5: 10 files, 864K

    ...

    ==> Pouring pyqt-4.11.3.yosemite.bottle.tar.gz
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    AttributeError: 'module' object has no attribute 'getusersitepackages'
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    AttributeError: 'module' object has no attribute 'getusersitepackages'
    ==> Caveats
    Phonon support is broken.

    Python modules have been installed and Homebrew's site-packages is not
    in your Python sys.path, so you will not be able to import the modules
    this formula installed. If you plan to develop with these modules,
    please run:
      mkdir -p
      echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> homebrew.pth
    ==> Summary
    🍺  /usr/local/Cellar/pyqt/4.11.3: 560 files, 19M



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

- 160419 增补后来的折腾
- 140616 再次精简,算是发布
- 140505 快速简述完成
- 140110 起意,总结

