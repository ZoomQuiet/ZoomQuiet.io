Title: ScrapBook 在 M1macOS 上恢复
Slug: 221213-scrapbook-revert
Date: 2022-12-13 21:42
Summary: ScrapBook/ 长期使用的私人知识仓库核心组件回归
Tags: DAMA,SCM,PKM,M1,macOS
Author: ZoomQuiet
Status: published


[TOC]

## Background

![neofetch](https://ipic.zoomquiet.top/2022-12-13-zshot%202022-12-14%2000.18.51.jpg)

[嫑升级 FireFox 到 56 以上 ~ DebugUself with DAMA ;-)](https://du.101.camp/2017-11/ff-no-upgrade/)


## Problem

之前通过不升级 FireFox 继续使用了一段时间,
但是,随着 FireFox 公司的折腾,一不小心就自动升级了;
好在找到了 **WaterFox** ,是的, 人家就是叫这个名字,
明确就是对着干的, 当然,为了生存 `水狐` 也不得不用了 Chromiun 内核,
导致无法兼容老的基于 `XPCOM + XUL` 插件;
好在社区给力,及时分离出一个 `Waterfox Classic` 版本专门干这事儿;

![Waterfox](https://ipic.zoomquiet.top/2022-12-13-scrapbook_revert-1.jpeg)

问题在 M1 macOS 从 12.x 升级到 13.0.1 后,  **WaterFox** 全面失效,
窗口无法打开;

![scrapbook_revert](https://ipic.zoomquiet.top/2022-12-13-scrapbook_revert-0.jpeg)

那么,俺通过 ScrapBook 从05年开始, 17年以来收集到的近8万个本地网页资料就无法按照以往的习惯快速使用了...

这是无法承受的.

## Trace

好在 ScrapBook, 虽然使用 XUL 技术构建,但是,对抓到本地的网页管理很简洁:

- XML 文件记录用户定义的树形关系,并指向具体的本地目录
- 所有网页以目录形式写入本地硬盘, index.html 为入口,其它原有资源修改访问地址后同目录保存

所以, 我可以自行开发类似 ScrapBook 的管理/查阅界面工具来恢复使用;
不过, 这就要一个不可控的时间;

那么, 还有什么方案可以在 M1 macOS 环境中恢复一个老版本的 `FireFox` 或是可安装 `ScrapBook` 的 `WaterFox` 呢?

既然 macOS 对软件安装有很多限制,那么通过 Linux 环境来恢复对应浏览器界面应该可以,
只不过, `ScrapBook` 的数据处理有两种方案:

- 放在 macOS 本地, 通过共享目录给虚拟机中的浏览器访问
    - 然后, 通过 `VNC` 之类远程桌面,在 macOS 桌面上使用本地其它 OS 中的浏览器访问
- 放在 macOS 本地, 通过 `shellFS` 挂载到其它 Linux 主机中提供给浏览器访问
    - 然后, 通过 `VNC` 之类远程桌面,在 macOS 桌面上使用远程浏览器访问历史网页

很明显, 后一种方案依赖其它主机, 这将导致俺在移动时, 无法恢复 `ScrapBook` 仓库的资料使用;

那么就用第一种

### Multipass
以往习惯的虚拟主机管理器是 `VirtualBox` ,
可以至今 M1 版本还是实验状态,尝试了一下根本无法合理安装起来一个 Ubuntu 系统;

对比了其它 macOS 中的虚拟主机控制方式; Docker 首先放弃,收费方案也略过;

发现 Ubuntu 官方推出的新方案支持 M1 环境,

这就是 Multipass, 一切看起来很好, 也快速安装好了一个 Ubuntu 22.04 服务器版本;
问题是, 可以进入 shell ,但是,无法访问互联网,
这也就意味着,无法安装新软件;

折腾了很久, 甚至于动用 ChatGPT 联调, 也不行;

### UTM
一开始尝试过,没安装成功,
再次尝试,找到对应视频, 才发现,用错了镜像,使用 arm 版本桌面镜像后,
顺利启动;
在 UTM 配置界面中,根据 `ifconfig` 选对 USB 外置网络连接后,

![UTM](https://ipic.zoomquiet.top/2022-12-13-zshot%202022-12-14%2000.29.38.jpg)

也能访问互联网, 并切换了国内镜像,
没想到,根据有关文档安装老版本 FireFox 时, 发现没有对应 arm 版本的包;
两样, 也没找到 `WaterFox` arm 版本的 Linux 安装包;

这就尴尬了,
忘记了 M1 的虚拟机,不可能安装其它芯片方案的系统;
这导致对应软件安装依然不简单...


## revert

终于醒悟过来后, 去 `WaterFox` 官方看了一下, 发现有升级,
顺利安装  `Waterfox Classic`  22.11 版本, 替代有问题的 22.10 版本

![Waterfox](https://ipic.zoomquiet.top/2022-12-13-scrapbook_revert-2.jpeg)

一切恢复;

不过,隐患依然存在,
想永远可以自由的以 `ScrapBook` 的形式继续使用自己积累的知识仓库,
还是要自立更生, 拥有自己完全控制的对应软件呢.

### PS:
> 为什么无法放弃 ScrapBook ?

因为已经形成了效能习惯:

- 看到合适网页,先用 ScrapBook 抓到本地, 这样即便原网页消失,资料也在硬盘中了
    - 抽空精读, 并标记重点, 然后, 组织到合理的分类树中
    - 需要时, 根据任务快速重组/增补对应知识点配置网页资料
- 同时, 通过自己编写的 Python 脚本,可以快速将各种分类的 SrapBook 资料分享到网络中
    - [ZoomQuiet.io -> collection {by gen4dot2htm.py vv.190718 at:190911 18:13:08,805091}](https://zoomquiet.io/collection.html)
    - 而且可以给每个网页追加自定页尾声明



## refer.

- [Apple M1 - 维基百科，自由的百科全书](https://zh.m.wikipedia.org/zh-hans/Apple_M1)
- [ScrapBook :: Firefox Extension](http://www.xuldev.org/scrapbook/)
- [How to install Multipass on macOS | Multipass documentation](https://multipass.run/docs/installing-on-macos)
- [How To Install Ubuntu 22.04 On M1 Mac || RUN Ubuntu Linux On ANY Mac W/ Apple Silicon - YouTube](https://www.youtube.com/watch?v=1WWj6qoWhJw)
    - [Installing a particular version of firefox on Linux.](https://gist.github.com/stephenharris/90bb468bf80e7f7b02e8b8afe694de4f)
- [Waterfox Classic | Waterfox Classic](https://classic.waterfox.net/)
- ...


## logging

- 221213 zoomquiet 终于解决
    - 230106 重新发布
- 221111 zoomquiet M1macOS 升级后再次无法使用
- 2017 zoomquiet 撞上 FireFox 放弃所有 XUL 扩展问题
- 2005 zoomquiet init. scrapbook in FireFox

