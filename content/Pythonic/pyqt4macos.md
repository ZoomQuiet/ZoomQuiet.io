Title: PyQt4 之消失在 Sierra
Date: 2017-08-08
Tags: mac,pyqt,howto,sierra
Slug: pyqt4macos


[TOC]

### 背景

最近在折腾 Qt , 因为在 mac 中开发运行在 win10 中,
用 PyQt 是必然选择哪.

只是项目是老坑, 所以,没用 Qt5 技术桟, 还是 Qt4

## 嗯哼

- 这天要折腾 QR 码识别了
- 运行 `brew install zbar`
- 然后,各种问题就爆发了,特别是:
    + `libjpeg.8.dylib` 加载不到
    + PyQt4 镜像丢失
    + ...
- 重新安装 pyqt 时才发现只有 5.1 系列的 Qt/PyQt 可以安装了...

## 原来

参考:[cartr/homebrew\-qt4: Homebrew tap for Qt4 and dependent formulae on Sierra](https://github.com/cartr/homebrew-qt4)

+ [Build on macOS Sierra 10\.12 without pyqt4? · Issue \#2001 · spesmilo/electrum](https://github.com/spesmilo/electrum/issues/2001)
+ [How to install QT4, Poppler, and Cairo on MacOS Sierra 10\.12](https://gist.github.com/robdvr/271e34785c8a43b1e093d2ee8e612aee)
+ [osx \- How can i install PyQT4 for Python 2\.7? \- Stack Overflow](https://stackoverflow.com/questions/36615952/how-can-i-install-pyqt4-for-python-2-7)

要想继续嗯哼 PyQt4:

    brew tap cartr/qt4
    brew tap-pin cartr/qt4
    brew install qt@4
    brew install cartr/qt4/pyqt@4

然后继续的:

    ~/.pyenv/versions/uC2710/lib/python2.7/site-packages༽
    ༄  ll PyQt4
    lrwxr-xr-x  1 zoomq  staff  66  8  8 21:50 PyQt4 -> /usr/local/Cellar/pyqt@4/4.12_1/lib/python2.7/site-packages/PyQt4/

是的, 要在 pyenv 中使用 brew 安装的 pyqt 得:

- 在对应版本环境的 site-packages 中使用 `ln -s` 关联到系统环境的库
- 就 Qt 而言要链接两个东西:
    + `sip.so -> /usr/local/Cellar/sip/4.19.3_1/lib/python2.7/site-packages/sip.so`
    + `PyQt4 -> /usr/local/Cellar/pyqt@4/4.12_1/lib/python2.7/site-packages/PyQt4/`
 
PS:

同理: OpenCV 也一样:

- 通过 brew 一致安全稳定的自动化编译安装到系统环境中
- 然后, 手工通过链接形式加载到对应 pyenv 版本环境中

所以, macOS 本质是 UNIX 系统,
用 linux 的环境配置思路是好的,
但是,又为了易用, macOS 也进行了各种妥协, 好在程序猿界总是能第一时间给出对应的嗯哼

只是不通过 google 简直了,不知道何时才能从弥散回来的文章中知道嗯哼...

> 请上苍保祐能翻墙的人民吧...

## 更新

- 170809 blogging
- 170808 inti.
