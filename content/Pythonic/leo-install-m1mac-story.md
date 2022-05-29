Title: M1macOS 下 Leo 复活故事
Date: 2022-05-28
Tags: python,howto,leo,install
Slug: leo-install-m1mac-story


[TOC]


## Background
> 背景

Leo 是文学化编辑环境, 由 EKR/令老爷子 单人为主长期维护的优秀开发/编撰/思考/...环境;
从 05 年上手以来, 一直在各种场景中欢快的使用,
历经 WindownsNT/Ubuntu/MAC 到现在的 macOS 12.* ,
可以说, 依托 Python 的跨平台属性, 一直能相对平滑的迁移;

比如: [Leo 5.2 theme custom](https://blog.zoomquiet.io/leo5theme.html)

事实上官方文档中: [Installing Leo — Leo 6\.6\.2 documentation](http://leoeditor.com/installing.html#installing-leo-on-macos-10-7-lion-and-later) ~ Installing Leo on MacOs 10.7 (Lion) 部分其实就是俺的笔记转化而成的.



为解决本地开发测试, 并尽可能复用运行时到相似的工程中, 以往选择的管理工具是 [pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)

参考:[Modern Python Environments \- dependency and workspace management \| TestDriven\.io](https://testdriven.io/blog/python-environments/)

![Modern Python Environments](https://ipic.zoomquiet.top/2022-05-29-PyEnvironments-vs.jpg)

以往形成的习惯是:

- 用 PyENV 安装不同版本 Python 运行时, 毕竟不同工程部署在不同目标主机中, 对 Python 版本依赖不同
- 基于 PyENV 的自动绑定机制, 在对应目录中通过指令 `pyenv local [指定运行时别名]` 
    + 就可以记忆绑定关系, 之后嘦进入相关目录, 将自动完成运行时切换
    + 不必须象其它工具要人工明确运行激活指令
- 进入对应环境后, 使用 pip 进行标准模块依赖管理

整体上可以达成效果:

- 本地和生产环境能部署相同 PyENV 环境
- 支持不同版本 Python 运行时
- 支持不同项目有自己的模块依赖树, 和其它工程隔离
- 支持不同工程, 如果领域接近, 可以绑定其它项目的 PyENV 环境, 节省相同模块的反复安装
- ...即: Python 运行时版本/项目目录/工程依赖 三者能相对独立配置/管理
    + 而且, 值得强调的是, 对于配置好的环境, cd 进入时, 自动完成切换
    + 同时, 所有定制运行环境, 统一安装在指定目录中, 和工程目录无关, 不必专门进行 git 忽略配置


## Troubles
> 问题

不过, 在今年初升级硬件为芯片为 M1max 全新 MBP 后, 就一直有问题:

参考: [如何安定进入 M1maxMBP / 是也乎\(￣▽￣\) / ZoomQuiet\.io](https://blog.zoomquiet.io/211114m1max-re-inti-mbp)

虽然当时幸运的使用官方迁移工具, 将几乎 94.2% 的环境和数据都自动迁移成功;
由于底层芯片不同, 以往 Python 本地运行时环境虽然能用,
但是, 无法进一步安装新版本 Python 运行时, 以及升级 Leo 到最新版本...

具体的:

- 原先在 Intel 芯片中安装/配置好的 PyENV 环境可以运行
    + 但是, 无法安装新版本 Python 环境
    + 也无法正常使用对应环境中的 pip 安装新模块
- 原先在 Intel 芯片中安装/配置好的 miniconda 环境可以运行
    + 但是, `conda info` 报错
- ..感觉只有一组很小的 snap 可以使用, 已经不是两个完备可控的 Python 运行时管理环境了



## Goal
> 目标

恢复本地 Python 环境的控制:

- 可以自如安装多种版本 Python 运行时
- 可以针对不同工程绑定不同模块依赖树, 当然, 也可以复用相同的
- 可以安装运行最新 Leo 版本
    + 当前可用是 5.9-b2
    + 官方已经是 6.6.2 了


## Tracing
> 探索

当前环境:

![screenfetch](https://ipic.zoomquiet.top/2022-05-29-220529-screenfetch.jpg)

### 尝试 PyENV

- 先在 `~/.bash_profile` 中注释掉所有 PyENV 相关的配置,
- 将 `~/.pyenv` 移动为 `~/_pyenv`
- 根据官方指引: [pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv) 重新安装
    + 而且事先根据 [Home · pyenv/pyenv Wiki](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) 的建议
    + 重新安装了 Python 编译依赖

一切正常, 其实依赖通过 brew 安装的 python@3.9 完成自举

    Python 3.9.8 (main, Nov 10 2021, 03:55:42)
    [Clang 13.0.0 (clang-1300.0.29.3)] on darwin

可惜, 尝试通过 `pyenv install` 指令来安装其它版本 Python 环境,
都撞到编译失败, 反复探索, 网上给的招儿都用过, 还是无法解决.

### 尝试 miniconda
> 怀疑 PyENV 准备的编译脚本都是针对 Intel 背景的

所以, 重新将目光投向 Anaconda, 要知道这个项目已经不仅仅可以管理 Python 环境, 而且其它各种运行时环境都可以管理, 包含 rust/haskell/... 都可以通过 conda 指令一致性部署, 
而且事先经过不同平台的针对性预编译, 不用在本地折腾, 直接下载, 展开就可用;

而且, 进入 conda 运行时环境后, 可以继续用 conda 指令安装相关模块, 也可以用 pip 来从 PyPI 下载安装...

唯一不如 PyENV 的就是 conda 环境, 必须手工激活, 无法自动绑定;

之前 miniconda 是手工安装的, 现在已经有全新 arm 版本 brew 环境了,
参考: [在 M1 芯片 Mac 上使用 Homebrew \- 少数派](https://sspai.com/post/63935#!)


标准安装:

    abrew install miniconda

因为进行了多 homebrew 环境配置:

- ibrew 指向旧系统迁移过来的 Intel 版本 homebrew
- abrew 指向全新安装的 ARM 版本 homebrew


然后, 就可以探查当前支持那些 Python 版本了:

    $ conda search "^Python$"
    Loading channels: done
    # Name                       Version           Build  Channel
    python                        3.8.11      hbdb9e5c_5  pkgs/main
    python                        3.8.13      hbdb9e5c_0  pkgs/main
    python                         3.9.6      hc70090a_5  pkgs/main
    python                         3.9.7      hc70090a_1  pkgs/main
    python                        3.9.11      hbdb9e5c_1  pkgs/main
    python                        3.9.11      hbdb9e5c_2  pkgs/main
    python                        3.9.12      hbdb9e5c_0  pkgs/main
    python                        3.10.0      hbdb9e5c_1  pkgs/main
    python                        3.10.0      hbdb9e5c_2  pkgs/main
    python                        3.10.0      hbdb9e5c_3  pkgs/main
    python                        3.10.0      hbdb9e5c_5  pkgs/main
    python                        3.10.3      hbdb9e5c_5  pkgs/main
    python                        3.10.4      hbdb9e5c_0  pkgs/main


安装一个 Leo 专用的环境:

    $ conde create -n leo3811 python=3.8.11 


通过指令进入:

    $ conda activate leo3811


通过事先安装 `pip_search` 可以搜索出配置的PyPI 镜像是否包含 Leo:

![pip_search](https://ipic.zoomquiet.top/2022-05-29-zshot%202022-05-28%2000.07.02.jpg)

通过 pip 安装 Leo:

    $ pip install leo

![PyQt](https://ipic.zoomquiet.top/2022-05-29-zshot%202022-05-28%2000.07.22.jpg)

过程中, 可以观察到很多编译错误, 
但是, 安装脚本足够聪明, 可以逐一版本降低来尝试最终兼容;
安装完成后, 尝试运行:

```
$ leo
leoQt.py: can not fully import PyQt5.
Traceback (most recent call last):

  File "/opt/homebrew/Caskroom/miniconda/base/envs/leo3811/lib/python3.8/site-packages/leo/core/leoQt.py", line 55, in <module>
    from PyQt5 import QtCore

ModuleNotFoundError: No module named 'PyQt5.sip'


Traceback (most recent call last):
  File "/opt/homebrew/Caskroom/miniconda/base/envs/leo3811/bin/leo", line 5, in <module>
    from leo.core.runLeo import run
  File "/opt/homebrew/Caskroom/miniconda/base/envs/leo3811/lib/python3.8/site-packages/leo/core/runLeo.py", line 27, in <module>
    leoGlobals.app = leoApp.LeoApp()
  File "/opt/homebrew/Caskroom/miniconda/base/envs/leo3811/lib/python3.8/site-packages/leo/core/leoApp.py", line 334, in __init__
    import leo.core.leoFrame as leoFrame
  File "/opt/homebrew/Caskroom/miniconda/base/envs/leo3811/lib/python3.8/site-packages/leo/core/leoFrame.py", line 13, in <module>
    import leo.core.leoColorizer as leoColorizer
  File "/opt/homebrew/Caskroom/miniconda/base/envs/leo3811/lib/python3.8/site-packages/leo/core/leoColorizer.py", line 18, in <module>
    from leo.core.leoQt import Qsci, QtGui, QtWidgets
  File "/opt/homebrew/Caskroom/miniconda/base/envs/leo3811/lib/python3.8/site-packages/leo/core/leoQt.py", line 88, in <module>
    qt_version = QtCore.QT_VERSION_STR
NameError: name 'QtCore' is not defined
```

没招, 问 Leo 官方 mailling-list: https://groups.google.com/d/msgid/leo-editor

不久, tbp100.tp@gmail.com 建议:

> this looks like a problem with Qt or PyQt, not leo per se. possibilities:

- try to install PyQt6 on its own (without the rest of leo);
- try to install an earlier version of PyQt6, if you can figure out which ones are available;
- try installing PyQt5 instead of PyQt6 (Leo can use either one); 
- install python 3.9 and see whether PyQt6 or PyQt5 will install without errors.


### PyQt
> 想起来 Qt 是个神奇的东西...

之前进行桌面开发时, PyQt 就不能简单安装, 对应搜索


国内用户首先要配置 conda 源:

    $ conda config --set show_channel_urls yes

生成 `~/.condarc` 文件后对应修改, 比如俺当前是:

    auto_activate_base: true
    report_errors: true
    show_channel_urls: true
    channels:
      - defaults
    default_channels:
      - http://mirrors.aliyun.com/anaconda/pkgs/main
      - http://mirrors.aliyun.com/anaconda/pkgs/r
      - http://mirrors.aliyun.com/anaconda/pkgs/msys2
      - https://repo.anaconda.com/pkgs/main
      - https://repo.anaconda.com/pkgs/r
      - https://repo.anaconda.com/pkgs/msys2
    custom_channels:
      conda-forge: http://mirrors.aliyun.com/anaconda/cloud
      msys2: http://mirrors.aliyun.com/anaconda/cloud
      bioconda: http://mirrors.aliyun.com/anaconda/cloud
      menpo: http://mirrors.aliyun.com/anaconda/cloud
      pytorch: http://mirrors.aliyun.com/anaconda/cloud
      simpleitk: http://mirrors.aliyun.com/anaconda/cloud



```
  conda create -n leo3911 python=3.9.11
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /opt/homebrew/Caskroom/miniconda/base/envs/leo3911

  added / updated specs:
    - python=3.9.11


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    python-3.9.11              |       hbdb9e5c_2        10.1 MB  defaults
    ------------------------------------------------------------
                                           Total:        10.1 MB

The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/osx-arm64::ca-certificates-2022.4.26-hca03da5_0
  certifi            anaconda/pkgs/main/noarch::certifi-2020.6.20-pyhd3eb1b0_3
  libcxx             pkgs/main/osx-arm64::libcxx-12.0.0-hf6beb65_1
  libffi             pkgs/main/osx-arm64::libffi-3.4.2-hc377ac9_2
  ncurses            pkgs/main/osx-arm64::ncurses-6.3-h1a28f6b_2
  openssl            pkgs/main/osx-arm64::openssl-1.1.1o-h1a28f6b_0
  pip                pkgs/main/osx-arm64::pip-21.2.4-py39hca03da5_0
  python             pkgs/main/osx-arm64::python-3.9.11-hbdb9e5c_2
  readline           pkgs/main/osx-arm64::readline-8.1.2-h1a28f6b_1
  setuptools         pkgs/main/osx-arm64::setuptools-61.2.0-py39hca03da5_0
  sqlite             pkgs/main/osx-arm64::sqlite-3.38.3-h1058600_0
  tk                 pkgs/main/osx-arm64::tk-8.6.11-hb8d0fd4_1
  tzdata             anaconda/pkgs/main/noarch::tzdata-2022a-hda174b7_0
  wheel              anaconda/pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  xz                 pkgs/main/osx-arm64::xz-5.2.5-h1a28f6b_1
  zlib               pkgs/main/osx-arm64::zlib-1.2.12-h5a0b063_2


Proceed ([y]/n)?


Downloading and Extracting Packages
python-3.9.11        | 10.1 MB   | ##################################################################################################################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate leo3911
#
# To deactivate an active environment, use
#
#     $ conda deactivate

```

检验安装成果:


```

$  conda env list
# conda environments:
#
base                  *  /opt/homebrew/Caskroom/miniconda/base
leo3811                  /opt/homebrew/Caskroom/miniconda/base/envs/leo3811
leo3911                  /opt/homebrew/Caskroom/miniconda/base/envs/leo3911
```



```
$ conda install PyQt
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /opt/homebrew/Caskroom/miniconda/base/envs/leo3811

  added / updated specs:
    - pyqt


The following NEW packages will be INSTALLED:

  adwaita-icon-theme pkgs/main/osx-arm64::adwaita-icon-theme-40.1.1-hca03da5_1
  atk-1.0            pkgs/main/osx-arm64::atk-1.0-2.36.0-h7fe96df_0
  cairo              pkgs/main/osx-arm64::cairo-1.16.0-h0ab239c_1
  dbus               pkgs/main/osx-arm64::dbus-1.13.18-h8280c03_0
  epoxy              pkgs/main/osx-arm64::epoxy-1.5.4-h1a28f6b_2
  expat              pkgs/main/osx-arm64::expat-2.4.4-hc377ac9_0
  fontconfig         pkgs/main/osx-arm64::fontconfig-2.13.1-h1f4a5ec_0
  freetype           pkgs/main/osx-arm64::freetype-2.11.0-h1192e45_0
  fribidi            pkgs/main/osx-arm64::fribidi-1.0.10-h1a28f6b_0
  gdk-pixbuf         pkgs/main/osx-arm64::gdk-pixbuf-2.42.6-h74ef11a_4
  gettext            pkgs/main/osx-arm64::gettext-0.21.0-h826f4ad_0
  giflib             pkgs/main/osx-arm64::giflib-5.2.1-h1a28f6b_0
  glib               pkgs/main/osx-arm64::glib-2.69.1-h98b2900_1
  gobject-introspec~ pkgs/main/osx-arm64::gobject-introspection-1.68.0-py38h3459c9f_3
  graphite2          pkgs/main/osx-arm64::graphite2-1.3.14-h0e5e14a_0
  gtk3               pkgs/main/osx-arm64::gtk3-3.24.21-h321fa23_1
  harfbuzz           pkgs/main/osx-arm64::harfbuzz-2.8.1-hffeda63_0
  hicolor-icon-theme pkgs/main/osx-arm64::hicolor-icon-theme-0.17-hca03da5_2
  icu                pkgs/main/osx-arm64::icu-68.1-hc377ac9_0
  jpeg               pkgs/main/osx-arm64::jpeg-9e-h1a28f6b_0
  krb5               pkgs/main/osx-arm64::krb5-1.19.2-h3b8d789_0
  libedit            pkgs/main/osx-arm64::libedit-3.1.20210910-h1a28f6b_0
  libevent           pkgs/main/osx-arm64::libevent-2.1.12-hf27765b_0
  libiconv           pkgs/main/osx-arm64::libiconv-1.16-h1a28f6b_2
  libpng             pkgs/main/osx-arm64::libpng-1.6.37-hb8d0fd4_0
  libpq              pkgs/main/osx-arm64::libpq-12.9-h65cfe13_1
  librsvg            pkgs/main/osx-arm64::librsvg-2.50.7-h90a7944_0
  libtiff            pkgs/main/osx-arm64::libtiff-4.2.0-h01837e1_1
  libwebp            pkgs/main/osx-arm64::libwebp-1.2.2-h68602c7_0
  libwebp-base       pkgs/main/osx-arm64::libwebp-base-1.2.2-h1a28f6b_0
  libxml2            pkgs/main/osx-arm64::libxml2-2.9.14-h8c5e841_0
  libxslt            pkgs/main/osx-arm64::libxslt-1.1.34-h9833966_0
  llvm-openmp        pkgs/main/osx-arm64::llvm-openmp-12.0.0-haf9daa7_1
  lz4-c              pkgs/main/osx-arm64::lz4-c-1.9.3-hc377ac9_0
  ninja              pkgs/main/osx-arm64::ninja-1.10.2-hca03da5_5
  ninja-base         pkgs/main/osx-arm64::ninja-base-1.10.2-h525c30c_5
  nspr               pkgs/main/osx-arm64::nspr-4.33-hc377ac9_0
  nss                pkgs/main/osx-arm64::nss-3.74-h142855e_0
  pango              pkgs/main/osx-arm64::pango-1.48.7-h79d33a7_0
  pcre               pkgs/main/osx-arm64::pcre-8.45-hc377ac9_0
  pixman             pkgs/main/osx-arm64::pixman-0.40.0-h1a28f6b_0
  pyqt               pkgs/main/osx-arm64::pyqt-5.15.2-py38he8f2410_0
  qt                 pkgs/main/osx-arm64::qt-5.15.2-h4e944ae_2
  zstd               pkgs/main/osx-arm64::zstd-1.5.2-h8574219_0


Proceed ([y]/n)?
```


> $ pip install leo


![PyQtWebEngine](https://ipic.zoomquiet.top/2022-05-29-zshot%202022-05-29%2021.41.02.jpg)

也有安装失败, 持续自动降级现象...


最终成功安装了:

- Successfully built lazy-object-proxy wrapt tornado
- Installing collected packages: zipp, wrapt, typing-extensions, traitlets, pytz, pyrsistent, MarkupSafe, lazy-object-proxy, dialite, attrs, webruntime, tornado, tomli, sphinxcontrib-serializinghtml, sphinxcontrib-qthelp, sphinxcontrib-jsmath, sphinxcontrib-htmlhelp, sphinxcontrib-devhelp, sphinxcontrib-applehelp, snowballstemmer, pscript, platformdirs, mccabe, jupyter-core, jsonschema, Jinja2, isort, importlib-metadata, imagesize, fastjsonschema, docutils, dill, babel, astroid, alabaster, sphinx, six, pylint, pyflakes, nbformat, future, flexx, leo
- Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.1 alabaster-0.7.12 astroid-2.11.5 attrs-21.4.0 babel-2.10.1 dialite-0.5.3 dill-0.3.5.1 docutils-0.17.1 fastjsonschema-2.15.3 flexx-0.8.4 future-0.18.2 imagesize-1.3.0 importlib-metadata-4.11.4 isort-5.10.1 jsonschema-4.5.1 jupyter-core-4.10.0 lazy-object-proxy-1.7.1 leo-5.9 mccabe-0.7.0 nbformat-5.4.0 platformdirs-2.5.2 pscript-0.7.7 pyflakes-2.4.0 pylint-2.13.9 pyrsistent-0.18.1 pytz-2022.1 six-1.16.0 snowballstemmer-2.2.0 sphinx-4.5.0 sphinxcontrib-applehelp-1.0.2 sphinxcontrib-devhelp-1.0.2 sphinxcontrib-htmlhelp-2.0.0 sphinxcontrib-jsmath-1.0.1 sphinxcontrib-qthelp-1.0.3 sphinxcontrib-serializinghtml-1.1.5 tomli-2.0.1 tornado-6.1 traitlets-5.2.1.post0 typing-extensions-4.2.0 webruntime-0.5.8 wrapt-1.14.1 zipp-3.8.0

但是, 运行时报出神奇错误:


    $ leo
    Sorry, "python" cannot be run on this version of macOS. Qt requires macOS 11.1.0 or later, you have macOS 10.16.0.




### 混合安装:
> 果断 M1 环境中当前还是 brew 体系最靠谱

参考: [MacBook Pro m1版本怎么安装python 的pyqt5？ \- 知乎](https://www.zhihu.com/question/437075754/answer/1993415429)

- 先用 `abrew install pyqt@5` 完成针对 ARM 环境的 Qt 安装
- 然后将对应安装好的 lib 手工复制到对应 conda 环境中
    + 比如, 重新创建专用环境
    + `conda create  -n leo3912 python=3.9.12`
- 则, 手工复制的是:
    + `/opt/homebrew/Cellar/pyqt@5/5.15.6/lib/python3.9/site-packages/` 中所有目录
    + 到 `/opt/homebrew/Caskroom/miniconda/base/envs/leo3912/lib/python3.9/site-packages/`

包含:

    PyQt3D-5.15.5.dist-info
    PyQt5
    PyQt5-5.15.6.dist-info
    PyQt5_sip-12.9.0-py3.9.egg-info
    PyQtChart-5.15.5.dist-info
    PyQtDataVisualization-5.15.5.dist-info
    PyQtNetworkAuth-5.15.5.dist-info
    PyQtPurchasing-5.15.5.dist-info


从官方 [Latest](https://github.com/leo-editor/leo-editor/releases/latest) 链接中下载最新原代码包, 部署到 `/opt/bin`

然后, 在对应环境中调用:

```
(conda: leo3912)
$ python /opt/bin/leo/launchLeo.py

setting leoID from os.getenv('USER'): 'zoomq'
PYLINTHOME is now '/Users/zoomq/Library/Caches/pylint' but obsolescent '/Users/zoomq/.pylint.d' is found; you can safely remove the latter
duplicate, (not conflicting) key bindings in myLeoSettings.leo
all    Alt+) move-past-close
all    Alt+) move-past-close
duplicate, (not conflicting) key bindings in myLeoSettings.leo
all    Alt+} forward-paragraph
all    Alt+} forward-paragraph-extend-selection
duplicate, (not conflicting) key bindings in myLeoSettings.leo
all    Ctrl+( add-comments
all    Ctrl+( add-comments
duplicate, (not conflicting) key bindings in myLeoSettings.leo
all    Ctrl+) delete-comments
all    Ctrl+) delete-comments
all    Ctrl+) delete-comments
duplicate, (not conflicting) key bindings in myLeoSettings.leo
all    Ctrl+{ promote
all    Ctrl+{ promote
duplicate, (not conflicting) key bindings in myLeoSettings.leo
all    Ctrl+} demote
all    Ctrl+} demote
Leo 6.6.2
Python 3.9.12, PyQt version 5.15.3
darwin
expand_css_constants Unresolved @constants
[
    '@bookmarks_base_decoration',
    '@bookmarks_children_family',
    '@bookmarks_base_border',
    '@bookmarks_base_family',
    '@checkbox-font-family',
    '@dialog-font-family',
    '@dialog-font-weight',
    '@status-font-family',
    '@dialog-font-style',
    '@dialog-font-size'
]
qt.qpa.fonts: Populating font family aliases took 163 ms. Replace uses of missing font family "Monoid Retina" with one that exists to avoid this cost.
not found: '@auto 4py3ch.md'
not found: '@auto 4py4ch.md'
not found: '@auto 4py5ch.md'
not found: '@auto 4py6ch.md'
not found: '@auto 4pyend.md'
not found: /Users/zoomq/Sites/101.camp/utility/announcer/tasks.py
not found: /Users/zoomq/Sites/101.camp/utility/pol/camp.yaml
not found: /Users/zoomq/Sites/101.camp/utility/pol/st.py
not found: /Users/zoomq/Sites/101.camp/utility/pol/tasks.py
not found: /Users/zoomq/Sites/101.camp/utility/pow/tasks.py
not found: /Users/zoomq/Sites/101.camp/_course/101camp1py/pow/tasks.py
expand_css_constants Unresolved @constants
[
    '@bookmarks_base_decoration',
    '@bookmarks_children_family',
    '@bookmarks_base_border',
    '@bookmarks_base_family',
    '@checkbox-font-family',
    '@dialog-font-family',
    '@dialog-font-weight',
    '@status-font-family',
    '@dialog-font-style',
    '@dialog-font-size'
]
expand_css_constants Unresolved @constants
[
    '@bookmarks_base_decoration',
    '@bookmarks_children_family',
    '@bookmarks_base_border',
    '@bookmarks_base_family',
    '@checkbox-font-family',
    '@dialog-font-family',
    '@dialog-font-weight',
    '@status-font-family',
    '@dialog-font-style',
    '@dialog-font-size'
]
wrote /Users/zoomq/.leo/leo.session
wrote recent file: /Users/zoomq/.leo/.leoRecentFiles.txt

```


![Leo 6.6.2](https://ipic.zoomquiet.top/2022-05-29-zshot%202022-05-29%2022.10.10-1.jpg)

可以正常启动后, 将指令包装为一个别名:

`~/.bash_profile` 中追加:

    alias leo6lanch="python /opt/bin/leo/launchLeo.py >> /dev/null 2>&1 &"


日常在终端中就两步调用:

    $ conda activate leo3912
    $ leo6lanch



#### PS:

如果以上安装 leo 后, 直接在 conda 环境中运行, 将发现:


```
$  leo
Traceback (most recent call last):
  File "/opt/homebrew/Caskroom/miniconda/base/envs/leo3912/bin/leo", line 8, in <module>
    sys.exit(run())
  File "/opt/homebrew/Caskroom/miniconda/base/envs/leo3912/lib/python3.9/site-packages/leo/core/runLeo.py", line 72, in run
    g.app.loadManager.load(fileName, pymacs)
  File "/opt/homebrew/Caskroom/miniconda/base/envs/leo3912/lib/python3.9/site-packages/leo/core/leoApp.py", line 2252, in load
    t1 = time.clock()
AttributeError: module 'time' has no attribute 'clock'

```

经过代码探查发现, `time.clock()` 已经在 Py3.8 之后废弃,
也就是说, Leo 最新版本中一定不包含这种函式,
即, pip 安装过程中为了兼容, 自动降级到某个老版本中了...
经过探查:

/opt/homebrew/Caskroom/miniconda/base/envs/leo3912/lib/python3.9/site-packages/leo/core/leoVersion.py

果断写着 `5.9-b2` , 是19年的版本;



## Summary
> 小结

看起来复杂, 其实只是探查了各种可能性后, 才知道如何可以合理的在 M1 芯片的 macOS 环境中安装 Leo:

- 基于 arm 版本 homebrew 安装 `PyQt@5`
- 基于 miniconda 的 Py3.9 环境安装其它依赖
- 基于 官方源代码中的 `launchLeo.py` 来启动

具体关键指令:

- abrew install PyQt@5
- abrew install miniconda
    + 注意, 正式使用前, 要运行: `conda init bash`
    + 参考: [Deep dive: conda init and activate — conda 4\.13\.0\.post1\+0adcd595 documentation](https://docs.conda.io/projects/conda/en/latest/dev-guide/deep-dive-activation.html)

应该可以在 `~/.bash_profile` 中找到以下类似配置:

    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    __conda_setup="$('/opt/homebrew/Caskroom/miniconda/base/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
    else
        if [ -f "/opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh" ]; then
            . "/opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh"
        else
            export PATH="/opt/homebrew/Caskroom/miniconda/base/bin:$PATH"
        fi
    fi
    unset __conda_setup
    # <<< conda initialize <<<
- 用 conda info 检验当前环境是否正常
- 然后, 创建 Leo 专用环境:
    + conda create  -n leo3912 python=3.9.12
    + 注意, 当前 brew 环境中默认安装的是 `python@3.9` 环境, 所以, 对应 conda 环境也应该是 3.9 以上的
- 手工将 PyQt 包从 brew 环境中复制到 conda 对应环境中, 例如:
    + `/opt/homebrew/Cellar/pyqt@5/5.15.6/lib/python3.9/site-packages/` 中所有目录
    + 到 `/opt/homebrew/Caskroom/miniconda/base/envs/leo3912/lib/python3.9/site-packages/`
- 手工从 github 中下载部署最新 Leo 源代码
- 然后, 从 conda 环境中调用 `launchLeo.py` 即可
- 可以正常启动后, 将指令包装为一个别名:

`~/.bash_profile` 中追加:

    alias leo6lanch="python /opt/bin/leo/launchLeo.py >> /dev/null 2>&1 &"


日常在终端中就两步调用:

    $ conda activate leo3912
    $ leo6lanch


## logging

- 220529 整理为文章
- 220528 miniconda 成功
- 220527 决定重来
- 220506 再尝试, 未果
- 220401 尝试, 未果
- 211113 触发, 存疑








