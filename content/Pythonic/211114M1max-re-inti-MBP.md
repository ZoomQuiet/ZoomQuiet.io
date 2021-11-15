Title: 如何安定进入 M1maxMBP 
Date: 2021-11-14 22:42
Tags: MAC,M1,SCM,Howto
Slug: 211114M1max-re-inti-MBP

[TOC]

## background

13年入的 MBP 坑,
当时 17吋 顶配, 在 MACAO 实体店拿的;
16年初突然不可用, 
(后来检查才发现, 是长期使用功率不匹配的电源才反复导致主板出问题)
急忙去 MACAO 新授权店拿了 13吋高配(i7,4核,16G内存,512G硬盘);
因为是主力开发/日常用机,
就没敢一直升级系统, 10.X 系列一直用下来;

到今年下半年, 明显撑不住了:

- OBS 录制 720P 以上视频, 撑不住10分钟就崩溃
- 腾讯会议本地录制, 30分钟的内容要转换20分钟
- ffmpeg 进行视频处理, 几乎都是 0.42 倍率在进行
- docker 容器一启动就要等待3分钟
- ...

如此种种已经开始干挠日常工作/学习/创作/...

怎么办?
磕金/升级呗...

> 忍了一年...

去年 M1 芯片 Air 一出来就想买的,
但是, 大家都说 M1 还不成熟, 各种软件都要等待兼容...

就忍着, 一直到10月, 一下子有了 M1pre/max,
性能又翻倍了,
立即入手: 14吋, M1max 10核, 64G 内存, 1T 硬盘;

等了快三周, 终于到手, 如何开始安定迁入?


## goal
> 最短, 最平滑, 进入, 折腾最少

日常依赖其实并不多主要就几块儿:

- 终端相关:
    + iTerm2 为界面
    + bash v4.4.12 配合 bash_it 定制日常环境
    + PyENV 管理多种 Python 运行时
        - conda 管理 Leo 安装运行时
    + RVM 管理多种 Ruby 运行时
    + NVM 管理多种 Node 运行时
    + ASDF 管理多种 Elixir 运行时
    + ...以及各种 AliYun/Heroku/AWS/...依赖CLI 管理工具
    + 特别是 HomeBrew, 管理了超过200种 UNIX 实用工具
- 浏览器相关:
    + WaterFox 安装使用传统 Firefox 插件, 以便查阅积累超过15年, **30+万**网页的本地资源库 ~ 基于 Scrapbook 收集管理, 但是 Firefox 56.0 版本之后不再支持原有插件体系, 只能迁移到 `水狐` 继续
    + Vivaldi 进行日常工作管理, 因为内置 `树状标签管理` 又兼容 Chrome 扩展而且没有 Google 广告
    + Brave 进行日常探索学习, 也兼容 Chrome 扩展
    + Edge 进行日常资源管理, 比如团队仓库/公众号/云资源/...兼容部分 Chrome 扩展
    + Chrome 进行日常 Google 系工具使用, 核心就是 gmail
    + Chromium 进行日常系统测试, 专门用以走查 web 系统功能
    + 以上浏览器都需要关键拓展来确保日常最基础可用:
        - SwitchyOmega ~ 快速代理切换工具, 以便使用不同网络来访问有关资源
        - The Great Suspender Original ~ 自动将不活跃标签内存回收
        - Create Link ~ 快速形成 Markdown 格式网地址文本
        - Choosy ~ 快速将网址丢入其它浏览器/应用中加载
        - ...
    + ...以及部分终端中无头浏览器辅助进行爬虫开发
- 开发相关:
    + XCode ~ 获得基本编译支持
    + Sublime Text 3 ~ 获得快速编辑支持
    + VScode ~ 获得综合开发支持
    + DBeaver ~ 获得数据库管理界面
    + Docker+VirtualBox ~ 虚拟主机支持
    + ...以及其它42+以上开发支持工具
- 媒体相关:
    + IINA+VLC 看视频
    + GIMP+Inkscape 进行图片处理
    + screenflow 进行视频编辑
    + ...以及其它42+以上媒体处理工具
- 系统相关:
    + muCommander ~ 日常双窗口资源管理, 通过快捷键提高文件管理效率, JAVA 实现可运行在所有系统中, 当年从 WindowsNT 平台开始就习惯了有关操作
    + Display Menu ~ 快速调节不同显示器分辨率
    + Lunar+Flux ~ 快速调节所有显示器亮度/对比度/...
    + aText ~ 快速管理自定义常用短语
    + iPic ~ 快速上传图片到图床, 获得 markdown 格式图片引用文本
    + Spectacle ~ 窗口布局快捷键支持工具, 可以高效安排多窗口排列
    + Bartender ~ 从2就开始付费使用, 现在已经到 v4, 可以将 menu bar 中应用图标管理, 折叠到子菜单中...
    + Caffeine ~ 便捷激活 mac 系统不休眠
    + ...以及其它42+以上系统增强工具
- 办公相关:
    + iWork ~ mac 味儿 Office
    + OpenOffice ~ linux 味儿 Office
    + WPS ~ 国产味儿 office
    + XMind+Freemind ~ 思维导图支持
    + yED+PlantUML ~ 流程图/架构图/... UML 味图谱支持
    + Axure+蓝湖 ~ 产品设计支持
    + 微信/企业微信/QQ/Lark/zoom.us/Slack/... ~ 工作协同用工具栈
    + ...以及其它42+以上团队协作支持工具

以及所有涉及正版软件的许可证升级/配置/采购/...

还有以往形成各种工程簇, 在本地不同目录入口中, 形成的对应快速`软链接` ...



## quickly
以上所有, 都人工进行重新配置的话, 目测至少得一个月, 才能陆续到位,
毕竟是以往多年尝试/配置/选择的成果;

如何简洁完成呢?

(周5收到, 周1 就应该全面完成迁移, 以便投入日常工作)


快速尝试了几个姿势:

- 人工配置, 光是安装 iTemer2 进行基本配置:
    + 字体
    + 颜色
    + ...etc, 就用了一小时
    + 那么多常用工具逐一配置到可用, 绝对无法简单完成
- Time Machine ~ 常规推荐操作:
    + 以往专门配置了个 1T SSD 移动硬盘来进行备份
    + 先用 4小时, 完成最新一次备份, 涉及40G 数据的更新
    + 然后, 使用 `迁移助理` ~ 死活无法发现这个非法 `时间机器` ?
    + 也可能, 用 10.X 系统备份的数据, 无法识别为 12.X 系统兼容时间备份
- rsync ~ 之前从 Windows -> Linux -> MAC 的异种系统迁移过程中立过大功
    + 用1小时, 将所有工作数据备份到另外移动硬盘中
    + 再开始尝试同步时, 想到这只能完成数据迁移, 最耗时的应用配置并没有涉及...
- 冷静一下, 搜索官方文档, 才发现:
    + [将内容迁移到一台新的 Mac 上 - Apple 支持 (中国)](https://support.apple.com/zh-cn/HT204350)
    + `迁移助理` 这一实用工具有三种迁移姿势:
        - 从另一台 Mac 或是 Time Machine 备份中转送数据
        - 从一个 Window 机器获得数据
        - 发送数据到另一台 Mac
    + 老rMBP 保有所有正常使用环境和应用, 新 M1MBP 是目标机
    + 都打开 `迁移助理` 
        - 老rMBP 选择 `To another Mac`
        - 新 M1MBP 选择 `From a Mac`
        - 并明确对传送的帐号如何处理, 俺选择->**创建新帐号**
        - 然后点 `继续` 完成安全配对后, 即开始 `点对点` 传输
        - 当然, 要先确保在同一个网络中
    + 看起来可行, 开始:   

![p2p](https://ipic.zoomquiet.top/2021-11-15-ScreenShot2021-11-15%2009.55.38.jpg)

嗯嗯嗯...嘦10小时等一晩上就好,

![80万文件](https://ipic.zoomquiet.top/2021-11-14-ScreenShot2021-11-14%2023.32.28.jpg)


果然:


༄  sudo du -hs *

    111M    Shared
    265G    zoomq
    4.2G    zoomquiet


༄  who i am

    zoomq    ttys004      2021-11-14 18:58


手工尝试时, 创建用户是 `zoomquiet` 仅仅完成 iCloud 主要数据同步,
而 `zoomq` 是从 linux 时代, 使用超过 15 年的帐号,

经过一夜自动转送, 合理同步了超过 450G 数据:

![450+G](https://ipic.zoomquiet.top/2021-11-14-ScreenShot2021-11-14%2023.37.06.jpg)


进入系统后发现, 基本所有习惯操作都可用, 只有少数几个要对应配置:

- 关键的 WaterFox 无法打开 Scrapbook 收集的本地网页, 以及控制界面
    + 搜索后, 尝试安装对应 `Waterfox Classic 2021.10` 版本
    + 替代原先使用的 `Waterfox Classic 2019.12`
    + 只是, 专门为 M1 芯片开发的 `Waterfox.G4.0.2.1.ARM` 却也已经放弃了 FireFox 经典 XUL 扩展体系, 无法安装 Scrapbook 插件
- Python 经常崩溃, 搜索后, 手工重建有关 openssl 两个核心模块的链接即可修复
- HomeBrew 要对应升级, 发现有大量失败, 要求先升级 XCode
    + 正常升级
    + 并:
        - $ sudo xcode-select --install
        - $ sudo xcodebuild -license accept 
    + 再来, 也就都流畅完成了


![12G](https://ipic.zoomquiet.top/2021-11-14-ScreenShot2021-11-15%2000.11.27.jpg)

甚至于, 原先在 老 rMBP 每次安装要编译半小时的 ffmpeg 也无缝自动完成升级:


![10核 ffmpeg](https://ipic.zoomquiet.top/2021-11-14-ScreenShot2021-11-14%2020.53.00.jpg)

这一下子就有 `10核降重任` 感觉了 ;-)



## murmur
> 记要关键增补指令过程...



> homebrew


`$ brew update`


    ...
    Error:
      homebrew-core is a shallow clone.
      homebrew-cask is a shallow clone.
    To `brew update`, first run:
      git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow
      git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask fetch --unshallow

> These commands may take a few minutes to run due to the large size of the repositories.
This restriction has been made on GitHub's request because updating shallow
clones is an extremely expensive operation due to the tree layout and traffic of
Homebrew/homebrew-core and Homebrew/homebrew-cask. We don't do this for you
automatically to avoid repeatedly performing an expensive unshallow operation in
CI systems (which should instead be fixed to not use shallow clones). Sorry for
the inconvenience!


> ༄  git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow

    remote: Enumerating objects: 346864, done.
    remote: Counting objects: 100% (346859/346859), done.
    remote: Compressing objects: 100% (151509/151509), done.
    remote: Total 338208 (delta 196986), reused 324905 (delta 183898), pack-reused 0
    接收对象中: 100% (338208/338208), 93.70 MiB | 5.90 MiB/s, 完成.
    处理 delta 中: 100% (196986/196986), 完成 7813 个本地对象.
    来自 github.com:Homebrew/homebrew-core
       ef5c358418d..5c8ec008df4  master     -> origin/master



> ༄  git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask fetch --unshallow

    remote: Enumerating objects: 28649, done.
    remote: Counting objects: 100% (25990/25990), done.
    remote: Compressing objects: 100% (8663/8663), done.
    remote: Total 20358 (delta 14980), reused 17036 (delta 11692), pack-reused 0
    接收对象中: 100% (20358/20358), 6.42 MiB | 6.31 MiB/s, 完成.
    处理 delta 中: 100% (14980/14980), 完成 1655 个本地对象.
    来自 github.com:Homebrew/homebrew-cask
       6faccf1ee4..134f0d09b2  master     -> origin/master


根据 `brew doctor` 诊断建议, 进行依赖安装时:

> ༄  brew install aom assimp bdw-gc brotli c-ares dav1d dbus double-conversion frei0r giflib guile jemalloc leptonica libarchive libb2 libbluray libev libproxy libpthread-stubs libsamplerate libsndfile libsodium libsoxr libvidstab libx11 libxau libxcb libxdmcp libxext libxrender luajit-openresty lz4 mpdecimal mujs nghttp2 opencore-amr openjdk openjdk@8 openjpeg opusfile pybind11 rav1e rubberband speex srt tesseract uchardet vapoursynth xorgproto zeromq zimg zstd


有大量报错:


...

    Error: python@3.9: the bottle needs the Apple Command Line Tools to be installed.
      You can install them, if desired, with:
        xcode-select --install

    You can try to install from source with:
      brew install --build-from-source python@3.9
    Please note building from source is unsupported. You will encounter build
    failures with some formulae. If you experience any issues please create pull
    requests instead of asking for help on Homebrew's GitHub, Twitter or any other
    official channels.

    ...

    Error: gcc: the bottle needs the Apple Command Line Tools to be installed.
      You can install them, if desired, with:
        xcode-select --install

    You can try to install from source with:
      brew install --build-from-source gcc
    Please note building from source is unsupported. You will encounter build
    failures with some formulae. If you experience any issues please create pull
    requests instead of asking for help on Homebrew's GitHub, Twitter or any other
    official channels.
    Error: gcc: the bottle needs the Apple Command Line Tools to be installed.
      You can install them, if desired, with:
        xcode-select --install

    You can try to install from source with:
      brew install --build-from-source gcc
    Please note building from source is unsupported. You will encounter build
    failures with some formulae. If you experience any issues please create pull
    requests instead of asking for help on Homebrew's GitHub, Twitter or any other
    official channels.



完成 XCode 升级后再来, 就一切顺利了 ;-)



以及推荐:

[exelban/stats: macOS system monitor in your menu bar](https://github.com/exelban/stats)

免费监察一堆传感器数值:
![stats](https://ipic.zoomquiet.top/2021-11-14-ScreenShot2021-11-14%2022.51.27.jpg)



## timekeeping


- 1.0h 尝试手工恢复
- 1.0h 尝试 timemechine 恢复
- 0.5h 探索其它可能
- 1.0h 尝试 迁移助手
- 8.0h 点对点 传输 450+G 数据+应用
- 1.0h 尝试恢复 WaterFox 职能
- 1.5h 尝试恢复关键工具许可证
- 1.0h 尝试解决 Python 问题
- 1.5h 记要/发布
- ...

![终于基本可用](https://ipic.zoomquiet.top/2021-11-14-ScreenShot2021-11-14%2023.31.28.jpg)



## refer.


- [5\. Using Python on a Mac — Python 3\.10\.0 documentation](https://docs.python.org/3/using/mac.html)
    - [My application crashed with invali… \| Apple Developer Forums](https://developer.apple.com/forums/thread/119429)
    - [fix missing openssl files in catalina](https://gist.github.com/llbbl/c54f44d028d014514d5d837f64e60bac)
    - [macOS Catalina: Python Quit unexpectedly error \- Stack Overflow](https://stackoverflow.com/questions/59888499/macos-catalina-python-quit-unexpectedly-error)
    - ...



# logging

- 211114 找到办法, 快速完成迁移
- 211113 init.
