Title: 开源生活实录.3.GTD之始
Date: 2022-08-22 22:42
Authors: ZoomQuiet
Category: MurMur
Tags: dama, logging, FLOSS
Summary: MurMur/ FLOSS lifestyle logging+3

## 时间知识

[TOC]

### background
> 书接上回

- [开源生活实录.0.从哪儿知道的?](/220817-flossstyle-0.html)
- [开源生活实录.1.LAMP之辉](/220817-flossstyle-1.html)
- [开源生活实录.2.GNU之魂](/220820-flossstyle-2.html)


当时能力起点:

- 大厂经历
- 过程改进经验
- 开源技术社区构建/运营经历
- 全栈技能基础
- 演讲/主持入门
- ...

### trace
> 回忆轨迹

从北京南下珠海, 其实也和社区有关;
上次是通过参与社区项目, 从而无意间通过面试, 获得机会;
这次, 则是通过社区朋友内推, 获得机会;
这位朋友就是 Albert Lee, 当初一起去由阿北面试,
他去了豆瓣成为第5位员工,
俺选择留在 SINA,
没几年, 他先去了 金山, 
然后, 推荐了俺, 就又这么混在了一起;

(PS: 在SINA 中和俺 PK 开发相同系统的 清风, 后来也去了豆瓣, 呆的时间更长,
而且成为著名 `北京吃喝玩乐组` 创始人, 经历丰富到不得不写本书来纪念,
进而变成创业项目冷启动关系社会资源, 
当然, 创业启动资金不是豆瓣资金, 而是 BTC 投资成功...)

不过, 来到珠海, 初印象最深的, 不是雷总, 而是中国的人事制度;
参考: [虚空间~不可接触之嗯哼 ~ DebugUself with DAMA ;-)](https://du.101.camp/2017-11/untouchable/)

入职一年后, 才真正捋清楚自己人事关系, 精密操作将档案艰难调入 金山 的集体户口;
虽然这和日常学习/工作没什么关系, 
但是, 想到毕业这么多年, 金山竟然才是第一家正式落户的企业, 很是感觉稳妥,
作事儿, 也就有更加长远的规划;

其中最长远的规划是敢于结婚了,
之前, 在大学里不敢考驾照和宣称不结婚, 
其实都是因为看不到未来可能的发展,
感觉自己能自由学习技术, 用手艺养活自己已经不易,
其它的不敢设想;

到了珠海, 金山软件, 一切好象都可以想象了;
结果, 头一年, 9月到岗, 当年 金山春节联欢晚会 总导演就注意到俺的活跃,
然后硬件就怀孕结婚,
给一众亲戚吓的...

不过, 工作/生活 稳定后, 社区也更加丰富;

原有计划只是将 ZPUG/珠三角Python用户组 带起来;
参考: [ZPyUG \- Woodpecker Wiki for CPUG](https://wiki.woodpecker.org.cn/moin/ZPyUG)

原本计划每个月组织一次,
后来发现珠三角地区各城市文化不相同,
那时去广州还得走长途汽车, 远程协商成本也高,
就变成不定期进行;

意外发现, 原先上海 ZCUG 创始人老潘也南下广州, 这下就有了熟人;
接着, 因为场地原因, 联系上 刘鑫 老师, 借用所在北大青鸟教室举行了两次 ZPUG 会课,
就把人给推荐到自己部门里, 彻底变成全职 **Pythoneer** 了 ;-)

当然, 在金山软件中, 也是大力使用开源技术,
比如, 给研发团队提供的项目管理平台, 就是基于 Trac 系统来定制的,
自然也给各技术部门作过宣传,
同时也根据 XP/极限编程 思想, 率先在部门进行站立会议等等制度;

也就引起 `式伟办公室` 的关注, 进而发现刚刚成立的 ECUG/Eerlang China User Group,
也就是后来创立 **7牛** 的许式伟, 
刚刚成立的金山研究室, 当时在探索云存储产品,
发现, 想建立大规模分布式系统, 当前世界上只有 Erlang 语言可以轻易作到,
带领部门一起探索时, 也就顺便创建了社区,
俺又有长期技术社区组织经验, 也就自然加入, 帮忙筹办当年叫 `Erlounge` 的年会;

前几期大会官网, 其实是用俺推荐的 t2t/[txt2tags](https://txt2tags.org/) 来快速撰写和发布的;

后来流行起来, 变成主流的 Markdown, 其实只是结构化文本中一个方案,
在 md 出现之前, 早已有很多优秀的方案在推行,
比如: **reStructuredText**/新结构化文本, Python 领域各种项目文档, 就是使用基于 rst 的 Shpinx 文档工具进行的;

俺知道 rST 是因为在查 Django 文档时, 
注意到 寻求静态化网站工具时, 发现 **rtfd**/[Read the Docs](https://readthedocs.org/) 文档服务,
是很多开源项目官方文档托管平台,
进而发现 [Sphinx documentation](https://www.sphinx-doc.org/en/master/)工具,
进一步知道 **reStructuredText**,
对比之前 MoinMoin 中内置的简易结构化文本,
感觉 rST 更加强大, 也更加复杂, 可平时用以快速记录/发布的, 
并不需要 rST 以 LaTex 为对标, 可以直接编译出精美图书这种能力,
所以, 才开始有目的的探寻这种工具是什么类型, 是否有其它更加简单的?

根据08年找到的一篇综述:
[文档工具 · Osmond.CN](http://floss.zoomquiet.top/data/20080709233551/index.html)

知道标签文本和结构化文本的差异,
也发现了 AsciiDoc/textile/Markdown/txt2tags/..
其中, txt2tags 是位巴西小哥创建的,
和其它结构化文本相比, t2t(txt2tags的缩写), 可以用一种格式, 自由输出到其它多种格式文本,
感觉很占便宜, 就先学习使用起来, 
进而尝试使用在所有场合;

比如私人 blog,
就选择了 [PyBlosxom - THE Python-Based Flatfile Blog Engine](https://pyblosxom.github.io/)
因为这是唯一解析 t2t 又是用 Python 开发的静态网站引擎;

[Zoom\.Quiet's PyBlosxom blogging](https://org.zoomquiet.io/pyblosxom/category-index.html)

- 早年统一使用 zoomquiet.org 来发布
- 后来 13年参加 Google I/O 大会时, 发现 Google 域名服务提前发布 .io 域名, 就迁移到 zoomquiet.io 了
- t2t 虽然好, 但是, 世界大势已经是 .md 为主,
- 也就将引擎迁移为 [Pelican](https://getpelican.com/)

类似这种出于自身需求, 不断探索/学习/贡献/...而自然进入的社区有很多;

比如:

- t2t 是贡献了简体文档翻译, 而列在官网 [txt2tags team](https://txt2tags.org/team/index.html)
- 探索个人桌面维基时, 找到了 TiddlyWiki, 也翻译了其中一个版本的简体界面翻译
    - 虽然没有列在官网
    - 却因为对 TiddlyWiki 熟悉, 从而成为 OpenResty 早期文档维护者之一
    - 进而和春哥熟悉, 进一步无意中将 锤子科技和 OpenResty 关联起来, 促成锤子第二次发布会门票捐助给了 OpenResty
    - 又因为这事儿, 又和负责对接此事儿的 iOpenResty 社区创始人 温铭 熟悉
    - 进一步参与了 APISIX 的创业, 社区宣传...
- 从 Erlang 到参与 ECUG 大会筹办
    - 从而认识 许式伟, 进而现在很多社区媒体资料, 都以社区联盟的方式, 免费使用 7牛 CDN 服务
    - 后来 老许 发现 Erlang 实在太另类, 自行创建 CErl 语言,但是, 完成之时, 发现和 Golang 基本一致
    - 于是义无反顾的投入 Golang 怀抱,并以 0.9 版本就完成了 7牛核心业务代码
    - 只是此时 ECUG Con. 已经办了5届不好改名, 于是建议, 修改定义就好
        - 从 Elrang China User Group
        - 变为 Effective Cloud User Group/ 实效云用户组
        - 缩写不变, 含义更加广泛, 完成兼容升级 ;-)
- 又从 Erlang 知道了函式语言这个全新领域, 顺着社区相相互链接, 接连学习探索了
    - Lisp ~ 所有开发语言之祖
    - Haskell ~ 学术型函式语言
    - Scheme ~ 入门级函式语言
    - Clojure ~ 运行在 JVM 上的函式语言
    - Elixir ~ Erlang 的现代化语言
    - ...一路上也分别在各个对应社区中认识了不少中国工程师

其实, 开源世界, 也并不只有技术,
进入金山是受命创立 `过程改进中心`,
从原先纯粹的工程师, 变成部门 leader 琐事增多,
同时又成家, 育儿;
等于是事业/爱好/家庭综合在一起, 
又都得高效完成;

开始对时间管理上心, 进一步发现 **GTD**/"Get Things Done" 思想, 
以及工具, 发现, 这也有对应推广社区;
从中, 认识了 陈一斌 , 那时他还在上学, 后来入职 iFanr 也变成全新咨询/投资社区的新入口;

特别是09年, 负责对接 **2009年哲思自由软件峰会**,
又一次见到 RMS 活人, 看到这个大胡子纯粹又快乐的状态,很是羡慕;

(现场录音:
[091017-pm-summit-REC013-RMS.ogg](http://0.zoomquiet.top/zeuux/091017-pm-summit-REC013-RMS.ogg)
)

当时给列席的广东省有关领导的开幕辞, 是这么写的:


> RMS 被全球程序员尊称为自由软件教皇，因为是他在 1984年独自发起 GNU运动,通过精心设计的GPL软件许可证体系，巧妙的利用版权法，定义出了能够永久保卫软件以下四个自由度的完整的哲学／法律／技术世界:

1. 出于任何目的，运行软件的自由。
2. 学习软件如何工作，以及为了满足自己的需要修改软件的自由。（显然，这个自由度的前提是能够访问软件的源代码）
3. 为了帮助你的邻居，将软件拷贝给他的自由。
4. 为了能够让整个社团受益，公开发行改进之后的软件的自由。（显然，这个自由度的前提是能够访问软件的源代码）

> 到今天,自由软件经历26年的发展，已经几乎涵盖所有的IT技术领域，从操作系统、编译器、到数据库、中间件、应用服务器、计算机语言、超级计算机、嵌入式系统等等;当下的热门技术和理念，比如：云计算、SaaS、Android系统、Chrome OS、开放源代码等等，也都与自由软件有着千丝万缕的联系; 由于自由软件通过精心设计的法律许可证,确保了开发者和用户同时都拥有运行、学习、修改和发行软件四种全方位的自由;从而保证了自由软件无限发展的可能性;近年兴起的开源运动在自由软件基础之上,创造性的弱化了"发行软件"的自由要求后,以一种开发/经营模式的姿态,快速抢占了不少专有软件的商业市场, 同时也保有了自由软件社区的活力;

> 中国在IT领域先天落后于国外一个时代,我们要想多/快/好/省的发展高新技术产业,就必须充分利用自由软件的巨量技术积累,学习开源运动的经营模式,利用法律和社区的力量来保卫我们的创新成果!而要想作到以上几点,首先就得深入理解自由软件本身;

> 在这一软件由自由软件引发的软件革命浪潮中, GNU/Linux 是最炫丽的明星,通过 Linux 内核包装了几千种自由以及商业软件形成了一大批各有特色的发行版,以其高度的可定制性,可扩展性,以及可适应性,快速进入了几乎所有行业;近年Top 500超级计算机排名中,大部分安装的都是定制后的 GNU/Linux 操作系统,已经很说明问题了;由于 GNU/Linux  是以一种松散的社区组织形式进行开发的,而各种发行版又是各个厂商自行组织力量进行集成和发行的,这其中有比较复杂的技术/以及法律问题; 要借力 GNU/Linux 的技术优势快速发展我们自己的产业, 就得深入GNU/Linux 的世界,理解其发源,发展,社区生态;

> 正是在丰富的使用GPL许可证发行的自由软件帮助下，互联网产业才得以发展起来，因为广大开发／运营商，可以免费使用高质量的自由软件来开发／发布／运营各种类型的网站／网络服务;

> 当前所有发展中国家都在积极组织和支持自由软件社区/企业,因为只有这样才可能绕过发达国家积累的软件技术壁垒,通过和全球自由软件开发者联合,共同分享知识/技术,在自由软件基础上发展吻合国情的软件产业,才是发达国家软件厂商无法压制的发展模式;

结合反复看的著名文章: [如何成为一名黑客](http://devrel.zoomquiet.top/data/20110617102755/index.html)
其实, 也就明白了自己值得积累的方向,
作为一名合格的 hacker 可以在社区中有以下贡献:

- 撰写代码
- 编写测试
- 组织文档
- 帮忙运营
- 宣传布道

自己性格比较喜新厌旧, 不过写作/沟通/组织/...还算有热情,
那么, 作为社区经理/布道师, 还是足以担当的;

当然, 那时, 还没有 Evangelist/布道师, 社区经理 概念,
但是, 不影响自己开始下意识的向这个方向努力...


### summary
> 小结

刚刚到珠海,可以说叕是一个全新开始,
也可以说, 只是一次空间变化;

开源技术社区, 随着参与的时间积累, 越来越多社区通过原先认识的人物, 产生了关联,
自己业余时间需要选入的社区也越来越多;

- ZPUG ~ Python 技术推广社区
- ECUG ~ Erlang 技术推广社区
    - 后来孵化出: [恶狼战役/erlbattle](https://github.com/ZoomQuiet/erlbattle) AI 对战游戏社区
- ZEUUX ~ 自由软件推广社区
- FDD/自由软件日 ~ Ubuntu 等自由软件推广社区, 每年尽力参与大学城中的活动, 现场分享 Python 等故事
- SLL/教育大发现社区 ~ 作为顾问参与各种活动/项目发起和设计
- Leo ~ 文学化编辑器, 作为长期老用户, 一直在分享各种系统中安装使用经验给作者
- Techparty ~ 珠三角技术沙龙, 09年创立, ZPUG 合并进入, 变成珠海主持人
- ...

如何合理安排, 即便是使用 GTD 等等工具, 也慢慢发现, 一个人其实, 真的不可能全部全情投入,
怎么办?

是的, 发挥组织的力量, 让社区可以自行发展才是正确的...

![map-think](http://0.zoomquiet.top/ZQCollection/map/zqbook-map-think.png)

这是到09年, 因为社区触发的各种城市/工具/事件/...图谱


### refer.
> 有关链接

- [albertlee (Albert Lee)](https://github.com/albertlee)
- [虚空间~不可接触之嗯哼 ~ DebugUself with DAMA ;-)](https://du.101.camp/2017-11/untouchable/)
- [ZPyUG \- Woodpecker Wiki for CPUG](https://wiki.woodpecker.org.cn/moin/ZPyUG)
- [ecug - ChinaErloungeII.](https://code.google.com/archive/p/ecug/wikis/ChinaErloungeII.wiki)
    - [Google Code Archive - ecug - ChinaErloungeII.wiki.](https://code.google.com/archive/p/ecug/wikis/ChinaErloungeII.wiki)
- [txt2tags](https://txt2tags.org/)
    - [txt2tags team](https://txt2tags.org/team/index.html)
    - [PyBlosxom - THE Python-Based Flatfile Blog Engine](https://pyblosxom.github.io/)
- [首页 | Read the Docs](https://readthedocs.org/)
- [reStructuredText — Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables)
- [Pelican – A Python Static Site Generator](https://getpelican.com/)
- [TiddlyWiki — a non\-linear personal web notebook](https://tiddlywiki.com/)
- [OpenResty® \- 中文官方站](https://openresty.org/cn/)
    - [Apache APISIX® \-\- Cloud\-Native API Gateway](https://apisix.apache.org/zh/)
- [陈一斌 \| 爱范儿](https://www.ifanr.com/author/yibie)
- [2009年哲思自由软件峰会－珠海站－金山公司 \- 哲思](http://www.zeuux.com/event/content/60/photo/)
    - [如何成为一名黑客](http://devrel.zoomquiet.top/data/20110617102755/index.html)



### logging
下一篇:  [开源生活实录.4.PKM到EKM](/220903-flossstyle-4.html)



- 220828 ZQ 发布
- 220822 ZQ 增补
- 220819 ZQ init.



