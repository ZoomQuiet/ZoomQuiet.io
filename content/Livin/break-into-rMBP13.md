Title: rMBP 坠入纪
Date: 2016-06-28
Tags: MAC,rMBP,DAMA
Slug: break-into-rMBP13


[TOC]


# 崩
160625, 一个平常的早晨, 俺的世界崩溃了一大坨...
5年前老婆大人开恩准购的: 高配版, 8G, 512G+256G SSD 的MBP 15吋 无法开机!

# 溃
立即去当地 APPLE 维修中心,从机械硬盘启动,使用内置硬盘工具检验 SSD 不通过,
现场重新格式化安装, 但是中心没有 10.11 的安装镜像,只能先安装上 10.7.3 的.
回来,一边回忆,一边想整理这5年, 都如何配置出吻合自个儿口味的 MAC 环境的!?

但是, 下午, 相同情景, 再次灰屏,无法启动!
知道没那么简单了....果然,再次去, 发现是长期使用 60W 的电源来驱动 80W 的机器,导致显卡 SSD 都有问题,必须更换主板…

# 新
但是! 电脑是一切工作中心环境哪, 没有一个随时可以投入工作的移动环境,
简直好象就是离开了地球一样!

好在老婆大人受不了俺天塌地陷的表情,一个心软, 
俺就冲到 澳门 刚刚开启的 APPLE STORE 扛了台全新
rMBP 13吋,16G 内存, 512G SSD ;-)
OS X 10.11 的.

# 配
然后, 开始漫长而艰难的重新配置.

- 为毛?! 因为俺没用 TimeMachine 哪…
- 实在是当初没有合适的移动硬盘, 在家里 FreeBSD 的电脑上远程进行 TimeMachine 备份又太慢.
- 加之, 积累有关键数据的 `rsync` 脚本, 可以自动备份所有关键数据;
- 进一步的, BMP 的皮实是出了名的, TimeMachine 占用空间也是出了名的...

一切的一切,导致,重新开始配置时,才发现有多少事儿要折腾!
参考: [我的工具箱][1]

是的, 用15年以上, 来迭代的将自个儿的电脑操作, 融合到一系列工具中, 并训练成了肌肉记忆,
一台全新的优秀的 rMBP 对俺,几乎无法使用.

## 习惯
 回想一下俺日常每天每时每刻都在使用的习惯操作

- `sshvpnJP` 快速和 日本 的主机建立 SSH 隧道, 专供 Chrome 进行 gmail 以及其它科学网络使用
- `cmd+Space` 切换输入法, 使用 Rime 的 `鼠须管` 加载从 win98SE 上移植过来的 `BXM`
- subl 中 Shift+Ctrl+上下箭头 可以进行纵向的块选择
- FireFox 中 right click 的上下文菜单,应该只有俺需要的
- FireFox 使用树状结构的 TAB 来管理批量标签页面
- 有自动根据当前时间调节色温的 Docker 软件
- 有驻留 Dock 的日历软件,点击就可以看到
- 有习惯的双窗口文件管理器
- …

好吧…事实上在 MAC 中的所有操作都进行过精心的配置!

那么,先冷静的规划一下,恢复的顺序和操作以免前后矛盾;

所谓的配置,其实分:

- 系统配置
- 软件安装
- 软件定制
- shell 定制

从逻辑和先后依赖而言,就应该从基础配置到具体配置来,用越来越多的工具来协助自己完成配置;

## 过程
简单的回顾一下关键又崩溃的恢复过程

### 数据
因为有 2T 的 WD 火线移动硬盘, 所以, 基本上所有数据都有备份,恢复过程中发现缺少的只有:

- Leo 的默认  workbook.leo 是链接到其它文档的, 但是,用 rsync 时,没有跟随链接,具体指向哪儿忘记了
- FIreFox 有大量的扩展以及扩展本身的配置
	- 但是,杯具的是, FireFox 的配置/扩展/书签 等等用户数据备份一直没有统一的渠道
		- 要不是用插件完成 比如 `FEBE`
		- 要不对具体的系统文件目录进行备份
		- 要不用专用软件进行
		- 要不是用内置的 box 之流第三方服务进行
	- 一年前 mozilla 终于提出了自运营的云空间,本来以为都能自动备份下来的,,,结果是俺 Naive 了...
	- 重新安装后, 用原先的身份口令无法登录,看页面明显是中国的火狐公司使用了另外一套云空间,而且没有同步原先海外用户认证
	- 好吧, 更加奇葩的是, FireFox 从大陆和官方下载的 MAC 中文版安装包含根本不同!
		- 大陆的内置了很多类似 好123 的导航页面和服务....
		- 恶心的我…
		- 大陆版 Firefox\_latest\_mac\_47.0.dmg 90Mb\_
		- 官方版 Firefox 47.0.dmg 84Mb

其它, 下载/工作/文档/图片, 都用 `rsync` 非常精细的备份在移动硬盘中,
也是用 `rsync` 一次就可以同步回来;
所以, 512G 硬盘, 实际 499G 空间,
新机到手只用了 18G , OS X 10.11.3 系统以及赠送的 iWorks 系列软件,才占这么少! 良心!

只是运行完数据同步后, 只有 `160G` 可用了....

### 系统

首先, 关闭 Spotlight, 因为没有什么用,将整个儿硬盘设定为隐私就好.
然后, 立即在键盘中,将 `caps` 设定为 `control` 这样和  HHKB Lite 的键位感觉就一致了.

根据 [ZqBXM/mac at master · ZoomQuiet/ZqBXM]()(https://github.com/ZoomQuiet/ZqBXM/tree/master/mac) 将 Squirrel 安装恢复出来, 首先恢复输入法.

安装 `muCommander` 进入熟悉的双窗口文件管理器:

- 杯具的是,这货依赖 JAVA
- 首先要下载 70M 的 javaforosx.dmg
- 然后才能运行, 更加神奇的是:
	- 2013 年就已经停止维护了
	- 最高版本 0.9 无法使用
	- 只能先安装 0.85 使用几天后, 再安装 0.9 就又好了...
- 当前和 TotalCommander 不同,  muCommander 实在是非常轻型的管理器
- 只是有几个特性刚好吻合我的习惯:
	- 可以精细的定制样式, 指定程序猿字体, theme
	- 能快速记录/调节 目录书签
	- `alt+1` 给出所有上级目录
	- `alt+2` 给出最近操作的目录列表
	- `alt+4` 给出所有书签目录列表
	- `alt+5` 给出所有有效驱动器列表
	- `cltr+l` 用 finder 打开当前目录
	- `alt+F6` 对选定文件进行批量重定名
	- `F5` 将选定文件复制到另外一个窗口目录
	- `F6` 将选定文件移动到另外一个窗口目录
	- `F7` 创建目录
	- …
在 muCommander 就可以高速整理当前目录, 吻合记忆结构了.

### 浏览器
安装当前不用说, 为什么要先安装浏览器, 而不是其它必须软件?!
因为, 其它所有配置/软件信息 ,都用 FireFox 的插件 ScrapBook 管理的,
必须恢复私人本地资料库, 才好在以往收集的文档指引下逐一恢复软件配置.

杯具的是, 更多资料都在 GDriver 中, 而进入, 需要翻越, 可翻越依赖浏览器插, 可 Chrome 的插件都在人家的市场中, 嗯哼, Chrome Store 也在墙外.

是也乎,(￣▽￣)

只好, 先从 baidu 搜索到老版本, `Proxy_SwitchySharp.crx` 拖到扩展页面中,先勉强用起来.
幸好, 因为太常用,也关键, gmail 帐号口令是记下来的, 登录上, 瞬间, chrome 的一切都回来了!

FireFox 就没有这么幸运了...只能人工, 一个个回忆/搜索/安装/配置回来...

用了差不多半天,才将 FireFox 恢复到比较顺手:

- DownThemAll 高速/分块 下载器
- Greasemonkey 神奇的开挂平台
- `CoLT`  Copy Link Text and Location  可定制的链接复制管理器,可以一键从页面/链接 生成 markdown/rst/html 等等形式的链接, 是文档写作关键支撑工具
- `Enjoy Reading`+`Tranquility` 是云化了的 `Readablity` 的替代, 可以将页面净化为只有主要内容
- 以便用 `ScrapBook` 抓取为本地页面, 然后用目录树的形式来管理, 离线查阅/标记自学
	- 参考: [ZoomQuiet.io collection mapping {by gen4dot2htm.py v11.10.27 at:160217 11:09:36,660754}]()(http://zoomquiet.io/collection.html)
	- 配合自动脚本, 可以随时将积累了 10+年以上, 20Gb, 5+万页网页分享出来
	- 嗯哼,是的, 通过 7牛CDN ;-)
- `It's All Text!` 可以用快捷键召唤出任何指定的本地编辑软件,来编辑网页 textarea, 并自动复制回编辑器编辑的内容! 简直是在线文档/issue/wiki 的维护必须工具! 是的大家都在用网页编辑器, 俺可以用 Sublime Text 进行狂速的本地编辑!
- `NoSquint Plus` 可以记忆域名的具体缩放比例, rMBP 的分辨率非常大, 但是,默认显示网页时,又总是放大的过大,需要记忆最合适的比例,自动的!
- `Wired-Marker` 能对在线页面进行批注, 是对 ScrapBook 的补充
- `uBlock Origin` 智能关闭所有 JS 的业务脚本
- `Adblock Plus` 智能关闭所有广告 
- `Right Encoding` 高速指定网页编码
- `Tree Style Tab`+`Tab Mix Plus` 用树状目录,层级管理有内容关联的标签页面,简直是海量并发挖掘和学习必须的!
- [Menu Wizard]()(https://addons.mozilla.org/zh-CN/firefox/addon/s3menu-wizard/?src=userprofile) 以上扩展,已经向上下文 right click 菜单追加了上百项选项了!
	- 必须可以实时精简! 菜单精灵,就是这样一种神器,只看自己需要的菜单!
	- 而且作者是名 乌克兰 程序猿,失业在家就靠几项优秀的 FF 插件的捐助来养家, 每年都得捐助几次,,,,
	- 因为, 实在太好用了!!!! 

但是,依然丢失了积累超过10年的书签…好在其中至少80% 也都失效了....


等等,还有 Chrome 对应的扩展呢:

- Greasemonkey 神奇的开挂平台,在 Chrome 上是Tampermonkey
- 为什么你们就是不能加个空格呢？ 嗯哼!
- uBlock Origin / Adblock Plus同 FF 
- Proxy SwitchyOmega 嗯哼!
- Octotree 为了快速游览 github 仓库代码
- `Create Link` `CoLT`  Copy Link Text and Location 的部分替代
- Choosy 嗯哼,,,将 链接用指定 应用打开
- `Boomerang for Gmail` 神奇的邮件管理增强, 是 GDT 的必须品


### Leo with Qt
 文学化编辑环境 [LiterateProgramming - Woodpecker Wiki for CPUG][5] 

俺用 Leo 来进行所有的软件开发,图书翻译…更加要命的是所有注册口令的管理.
是的没用伟大的 1Password,,, 也是历史原因:

- 开始用 Leo 管理私人口令时,可能还没有 1P 这公司呢....
- 1P 要銭的…
- Leo 中已经积累了上千帐号的口令了...

不过,  Leo 的历史也很长,第一个版本发布在 1996 年! 以前都是基于 Tk 的, 中文问题很多, 
老爷子自学了 Qt, 在 2013 年全面迁移到 Qt 了, 漂亮了很多,但是,安装就麻烦了点儿.

参考:

- [About X11 and OS X][6]
- [XQuartz][7]

具体的:

- 安装 `XQuartz-2.7.9.dmg`
- 然后用 brew 安装 qt
- 最后进入具体的python 环境, 比如说 pyenv 管理的版本 python 
- 用 pip 安装 `PyQt4` 就好

然后, Leo 只是一堆 Py 脚本下载下来,
修订一下别名指向就好:

	# \~/.bashrc for running Leo
	alias leolanch="python /opt/bin/leo/launchLeo.py \>\> /dev/null 2\>&1 &"

### Dock
是的,人生第一个 APPLE 软件就是为了 Dock 才突破心障的, 然后就开始了 App Store 的无尽挖掘..

当前习惯的组合:

- Bartender 2 收纳各种图标
- `Battery Health`+`coconutBattery` 关注电池健康
- `Colossus` 国人作品,系统状态报告,重要的是实时网速,以及当前 ip
- `Day-O` 用 `TinyCal` 替代, 进行快速日历查阅
- `Spectacle` 进行窗口管理
- `Noizio` 工作白噪音, 因为 iOS 上买了,桌面也就顺手入了
- `Flux` 自动色温调节, 保护视力
- `Caffeine` 嗯哼...
- `Choosy`  从 Chrome 将链接在 FireFox 打开 这样就完成了, 用 google 搜索, 用 FireFox 的插件收集结果页面到本地长尾研究.

### App Store+Brew
通过官方 Store 安装, 的好处是不用自行本地备份 app 的安装文件,
恢复系统时可以从已购应用分类中快速指定, 重新自动安装.

当前习惯使用的应用集:

- 系统工具:
	- DrCleaner 内存清理
	- AppCleaner 软件清理
	- Alfred 效能工具, 虽然购买了专业版, 但是, 工作流并没有用起来
- 开发工具:
	- `Sublime Text` 嚓, 插件仓库简直无法自拔
		+ 大坑,仅仅配置 md 编辑就要有一个固定的顺序,才能获得过的去的编辑体验...
	- `iTerm` 每天用的那叫个频繁, 和 subl 配置成一样的 theme….
	- `Dash` 又一款不得不买的 程序猿 必备软件
	- `TeamViewer` 打死不用 windows, 但是,一定要用也通过远程管理控制!
	- `Tincta` 编辑器, 支持正则表达式 替换的
	- git/svn/hg 什么的通过 brew 安装的就不在这儿提及了...
- 空间工具:
	- 360云盘/百度云盘 没办法的标配置
	- Evernote 用来快速收集 微信中的聊天记录
	- Dropbox 纯粹用来情怀曾经的美好
	- Xccello 伪装成桌面的 Trello
- 文档工具:
	- OOo 不得不用的 Office 兼容软件
	- Ulysses 嗯哼, 比 subl 还要性感的跨平台创作环境
	- 1Checker 自学 E文写作工具
	- XtraFinder 杯具而神奇的注入式 Finder 增强工具
	- FileZilla 最好用的 FTP 桌面工具
	- androidfiletransfer 嗯哼
	- calibre 电子书转换工具
- SNS 工具:
	- 微信/QQ/Telegram 一个不能少
	- Ali 旺旺 有时和店家沟通,必须
	- Skye
- 阅读观看
	- `Xee³` 看图
	- Skitch 标定图
	- MediaInfo 照片 Meta 信息
	- CHM View 嗯哼
	- Simple Comic 嗯哼
	- Movist/VLC/MPlayerX/MPV 嗯哼
	- Skim 看 PD
	- …

### Dev.
开发环境哪…

是另外一个故事了, 也是血淋淋的, 简直不忍心回顾了

# 总结
经过72小时,近乎 不眠不休的配置,总算将主要的环境配置好了,
其它的随用随安装就好…

就算每5年才可能来这么一次, 再也不想了!
以往, 只有 win-\>Linux 时差不多也要这么折腾几天, 
Linux-\>Mac 时,几乎,没有什么感觉;
可是 MAC 的硬件切换,怎么就这么痛?!

回想,一定, 主要的折腾是系统和软件的个性配置, 星星点点, 基本都是微小的痛点,
在长期探寻中,找到了合适的方案, 以及操作快捷键, 然后肌肉记忆了下来,
具体如何配置的, 又没有记录, 或是自动化恢复方案, 然后就只能重新从肌肉记忆反推配置...

所以, 一定要长期/坚持/持续/理性 的备份!

- 杯具总是随时可能发生的
- 面向灾难恢复的备份才是可用的
- 最快时间恢复原有最好状态的备份才是好的

综上, MAC 本来就内置了最好的备份机制: `TimeMachine`

## TM
 一定要用! 一定要用! 一定要用! 

- 一个专用设备, 官方的 时间胶囊, 进行无线备份
- 或是大容量高速移动硬盘进行有线备份,只是:
	- 一定要雷线! 一定要雷线! 一定要雷线!
- 当前,有条件的,能上 AirPort Time Capsule 就上


只是, 一直担心,没有演练过 TimeMachine 的系统恢复哪, 总是对这机制不怎么放心,
怎么破!?

# Changelog

- 160703 增补,因为有人说,都是远古工具陈列馆了,不得不将最近引入工具箱的记述上
- 160701 补全
- 160628 发布
- 160627 随笔
- 160626 开始

[1]:	http://s5rst.qiniucdn.com/131113-MyTools/index.html
[5]:	http://wiki.woodpecker.org.cn/moin/LiterateProgramming
[6]:	http://support.apple.com/kb/HT5293
[7]:	http://xquartz.macosforge.org/landing/