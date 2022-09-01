Title: 开源生活实录.1.LAMP之辉
Date: 2022-08-19 18:42
Authors: ZoomQuiet
Category: MurMur
Tags: dama, logging, FLOSS
Summary: MurMur/ FLOSS lifestyle logging+1

## 魔都打怪

[TOC]

### background
> 书接上回

[开源生活实录.0.从哪儿知道的?](/220817-flossstyle-0.html)

从常州切换回软件行业, 
在老同学推荐下, 面试成功, 转战上海,

当时能力:

- HTML/CSS 初级能手写/工具 完成静态网页
- Flash 中级, 能组合图元响应点击或是其它数据完成动画网站
- ASP 中级, 能在 ISS 环境中接入 SQL Server 构建基础动态网站
- 项目管理初级, 知道用 Dreamweaver 内置组件功能, 将网络元素标准化, 在小组内部共享
- JAVA/Delhpi/Pascal/C/C++/...都是知道, 不会具体使用

### trace
> 回忆轨迹

有位同班同学, 毕业就准备结婚, 老婆是上海人, 第一时间进入上海一家软件公司,
很努力, 很快变成经理, 就拉了一把;

虽然祖藉是上海, 但是, 家里亲戚都没什么社会资源, 
也就到浦东租房时, 从爷爷那儿扛了架弹簧折叠床, 算是解决了基础问题.

原本是作为前端工程师入职的, 然后, 发现也能作后端开发,
慢慢的也就什么都开始干;

在上海期间, 为公司完成的主要工程应该有:

- 公司核心 ERP 产品的, XSL 皮肤系统
- 配套上海市交通局, 实时交通状态监察系统, 动态地图前端, 用 Flash 完成, 配合后台提供的 XML 接口
- 上海市政府党委办公室官网 CMS 系统, Windows NT+Apache+MySQL+PHP

其中, 党委官网是手工原创 CMS 系统,
其实, 就是对一套固定栏目的固定格式内容,分别提供对应网页编辑界面,
以便运营人员可以随时更新内容;
并没有后来标准 CMS 系统那么成熟的权限/角色/排版/插件/...子系统;

不过, 为了完成这个任务, 拓展出的 LAMP 技能, 
算是真正进入了 FLOSS 世界;

LAMP 就是当年提出最佳建站技术组合的简称:

- **L**inux ~ 一般是 Redhat 
- **A**apache ~ 作为web 服务器
- **M**ySQL ~ 作为数据库服务
- **P**HP ~ 作为应用开发

因为 ASP 涉及到 微软一系列系统/软件的商业版权要求,
只有政府大项目才用, 
一般普通动态应用网站, 基于 **LAMP** 足够,
当然, 后来这种组合也进行了拓展:

- LAMPs ~ 可以用 Perl/Python/.. 其它语言来开发
- LNMP ~ 用 Nginx+Python 组合, 是后来更加习惯的
- ...

知道这个组合概念, 是从 Redhat 光盘开始的,
大学毕业时, 通过 **上网冲浪** (那时对上网探查资料的别称),
知道 Linux 在流行, 但是, 并没什么渠道可以获得能方便安装的版本,
那时, 标准安装是 Slackware 15张2吋软盘进行依次安装, 复杂到不可想象;

毕业时, 和同学合资买了张 Redhat linux 4.2? 光盘,
但是, 并没什么机会安装使用, 最后带到上海,
在公司一台闲置的普通 PC 机上安装成功;
应该只有680M硬盘空间, MMX 芯片,
好在那时也没有什么大型软件可以在 linux 中安装,
配合公司专线上网不用拨号,
用了两个星期才断断续续安装成功;

那时, 宿舍离公司自行车要一小时, 所以, 基本作习是这样的:

- 工作日, 7点起床, 8点左右到公司
    - 5点半下班后, 在食堂或是周边吃点儿
    - 新闻联播开始时, 回到桌前开始折腾
    - 23:00 左右回到宿舍, 看看其它什么就睡
- 周末, 10点起床, 11点左右到公司
    - 磨蹭一会就到午饭时间了
    - 吃好, 回到桌前开始折腾
    - 23:00 左右回到宿舍, 看看其它什么就睡

也就是基本上每周有40个小时业余时间投入到 开源技术学习中,
为什么这么积极呢?

因为没有资料, 很多时候要自己先翻译出来官方对应文档, 再尝试,
失败后对应查资料尝试解决;

注意, 那时 Google 和其它搜索引擎刚刚发布, 都没有很好搜索效果;
特别是中文开发资料, 能去交流的只有少数几个技术论坛, BBS 是那时主要交流场景;
IRC + mailling-list, 是关键技术讨论空间;

那时, 还没有足够英文自信, 问技术问题也只敢去中文论坛,
再从中文技术论坛的友情链接找到其它相关的技术论坛...

就象蚂蚁一般一点点儿在互联网迷雾中摸索;

为什么学习 PHP 呢? 其实就是市场需要, 老同学, 接了单, 公司其它人不会,
就教唆俺一起学, 然后就可以独立接单够收入了;

结果, 一入坑, 才发现, 原来并不是一个语言的事儿, 
其实, 大家目标都是建立功能站, 而那时, 最有市场的其实就是 Web1.0 时代标准的信息发布站,
讲道理其实, 一个 Wordpress 就足够了, 
可惜那时 i18N 技术还不成熟, 想折腾出一个中文化完备, 而且有所有期待功能的企业官网并不那么简单;
类似的还有 Xoop/Drupal/... CMS 应用框架, 都在宣传自己是最灵活的框架;

不过, 在一个半封闭网络环境中, 想快速用软盘从其它机器下载复制过来有关组件再安装/编译,
太难了,
印象中, 因为自己工作内容, 一直和 XML/XSL 打交道,
所以, 先选择 Nucleus CMS 来构建了自己第一个私人网站: zqstudio.org ;
这个 CMS 系统神奇在关键配置/样式, 全使用 XML 来定义和管理;

不过, 那时, 还没有 blog 概念, 有了网站也不知道发布什么内容为好;
只是通过建立个人网站, 算是对 **LAMP** 技术栈完整构建发布一个功能网站有了全面了解;

也因此, 拓展了社会网络:

- 给一家户外运动社团, 帮忙构建了 BBS, 以便发布户外项目消息, 因此有了一定可控主机资源
- 给一些 cosplay 社团, 帮忙提供摄影, 以及月刊打样服务, 因此认识了一批绘画师, 其中 俪欢 老师现在都有联系
- ...

可以说, 开源技术自主学习, 
不仅带来了事业拓展, 也变成了单身青年在大城市中探索的信心;

只是, 那时, 还没有意识到 FLOSS/自由,开源软件文化的威力,
还是一名: "我自豪, 我用盗版软件" 的 `白嫖党`;

直到遇见 Python...

整体上线索关系是这样的:

- 0: 学PHP, 作网站
- 1: 知道 CMS 概念, 挖掘出一系列 CMS 系统
- 2: 然后所有 CMS 系统社区都在歌唱 Plone 才是 CMS 之神
- 3: 进一步发现 Plone 是基于 Zope 构建的
- 4: 又经过学习才知道 Zope 是 Python 开发的
- 5: 那么想用好 Plone 自然得先学会 Python 并掌握 Zope
- ...

当然, 这是事后以上帝视角整理后的逻辑,
当年, 中间也夹杂了各种旁路探索, 
比如当时无意中找到的网页: [程序设计语言介绍/2002.6.21](http://web.archive.org/web/20030205031354/http://cdtzx.51.net/pimage/programs.htm)
其中介绍的所有语言, 都去尝试学习使用过,
结果只有 Python 和那时自身兴趣有关联, 从而真正上手;

而这个上手过程并不简单,
比如, 记忆中人生第一个可运行的 Python 工具是:

天气预报网络自动抓取工具/getSHwunderground,
简单说是就从 https://www.wunderground.com/ 网站自动抓取上海地区的天气数据,
在 CLI/终端 上整理为中文, 汇报出来;

当时基于 Python 1.5, 在 windows NT 环境中开发,
成体系的建功立业资料, 只有一本:
[Python学习手册 (Mark Lutz) 第一版](https://book.douban.com/subject/3948354/)
而且, 人家示例代码都运行在 mac 环境中, 
其中要突破的坑, 现在想也就几个,
当年整整用了一个月的业余时间...

过程中, 可能最大的收获是认识了中国 Python 社区中关键的两位人物,

- Limodou, UliPad/UliWeb 创始人
- 老潘, CZUG社区/润普公司 创始人

就是在 CZUG 吵起来而认识的, 记忆中是个什么事儿呢?
俺在 CZUG 中讨论 Zope/Python 的学习, 感谢 CZUG 提供一个免费社区空间,

- 发现背后主持公司叫 `润普` , 感觉这是 Zope 的谐音,建议, `润璞` 更加好;
- Linodou 反对, 认为这种难以念出来的字对公司发展不好
- 俺就引用各种理论来反驳
- 老潘 不时出来维护气氛
- ...我们仨儿, 几乎占了每个月, CZUG 论坛上1/3 的流量
- 可以说不吵不相识

过程中, 老潘也认识了 zoomquiet 这个ID,
甚至于开放了部分网站权限,
也就将以往积累的前端技能, 为 CZUG 定制了几款皮肤, 比如其中一款:

[2004-0930-effeBDragon.png (899×431)](http://0.zoomquiet.top/CPyUG/zoomquiet-design-collection/2004-0930-effeBDragon.png)

其中那个龙标的 logo 设计稿:
[Zdragon-cloud](http://0.zoomquiet.top/CPyUG/zoomquiet-design-collection/2004-0930-Zdragon-cloud-exp.png)
就是用`盗版` Coredraw 完成的;

类似折腾其实, 发现在很多社区中,
其中多数社区现在早已从互联网中消失, 
当然, 其中的大人物, 依然活跃在世界各地;

从上海得以北漂北京的关键人事就是: [HD](https://wiki.woodpecker.org.cn/moin/HD),
当时, 也只知道是国内 Python 大佬,
曾经在移动公司短信网关上, 用Python 完成重要系统;

应该也是在 CZUG 中认识的,
HD 不怎么说教, 只是发布项目, 号召大家来尝试,
但是, 很积极回答具体技术问题;

首先在大家倡议下, 
俺主动承担新近社区: 啄木鸟社区的邮件列表构建任务,
在已经慢慢熟悉的 redhat 系统中,
在公司闲置 PC 机上, 安装了 Mailman 系统,
从各种 Python 相关 BBS 论坛版块中宣传,
很快就有 200+ 订阅,
每天讨论各种 Python 开发问题;
(后来此列表由 exoweb.com 公司赞助, 迁移为 python-chinese@lists.python.cn)

进一步, 又主动安装 moinmoin 维基系统,
通过公司网关解析, 使用临时域名发布出来,
供给大家积累议题/资料;

并进一步, 参与了其中一个通用模板组件的开发:
[Otter \- Woodpecker Wiki for CPUG](https://wiki.woodpecker.org.cn/moin/Otter)
就是用 Python 合理对 XML 模板进行解析以及修改;
算是进一步夯实了当时并不熟练的 Python 开发技能;

神奇的是, 经过一次线上会议答辩:

![OtTXMLengine](https://ipic.zoomquiet.top/2022-08-20-OtTXMLengine.gif)

配合用 Coredraw 绘制的解析过程图谱,
通过 QQ 语音给大家解说明白思想和代码;

没想到这次普通的社区项目沟通会议, 其实是 SINA 面试考察,
因此获得了职位, 得以进入大型 IT 公司去接触不同的世界.


### summary
> 小结

在上海几年, 无知者无畏, 完全好奇心驱动下, 
持续自学, 慢慢恢复自学能力,
通过 开源技术, 结识开源社区/人物/项目,
通过义务贡献, 参与具体工程,
无意中入得关键人物法眼,
在自身现实社会渠道之外, 闯出全新道路;

这一切是因为什么, 后来才慢慢明白, 
只是, 当时反复看的电影, 并没有将所有关联融合起来:

[操作系统革命/RevolutionOS](http://woodpecker.up.zoomquiet.top/media/020215-RevolutionOS.rmvb)


### refer.
> 有关链接

- [Nucleus Documentation v3.2](http://nucleuscms.org/docs/)
- [Plone - The Open Source CMS — Plone Documentation v5.2](https://docs.plone.org/intro/index.html#what-does-plone-mean-how-is-it-pronounced)
- [Zope documentation — Zope documentation 5.3 documentation](https://zope.readthedocs.io/en/latest/operation.html#special-access-user-accounts)
- [Zope指南 (豆瓣)](https://book.douban.com/subject/1096066/)
- [About "Learning Python, 1st Edition"](https://learning-python.com/about-lp1e.html)
- ...
- [程序设计语言介绍/2002.6.21](http://web.archive.org/web/20030205031354/http://cdtzx.51.net/pimage/programs.htm)
- ...
- [中文Zope用户组(CZUG) - Zoomq's ContentPanels](http://web.archive.org/web/20040605125007/http://www.czug.org/Members/Zoomq)
- [GNU Mailman](https://www.list.org/)

### logging

下一篇: [开源生活实录.2.GNU之魂](/220820-flossstyle-2.html)


- 220819 ZQ 发布
- 220818 ZQ 规划
- 220817 ZQ init.



