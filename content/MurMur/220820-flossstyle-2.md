Title: 开源生活实录.2.GNU之魂
Date: 2022-08-20 21:42
Authors: ZoomQuiet
Category: MurMur
Tags: dama, logging, FLOSS
Summary: MurMur/ FLOSS lifestyle logging+2

## 帝都升级

[TOC]

### background
> 书接上回

- [开源生活实录.0.从哪儿知道的?](/220817-flossstyle-0.html)
- [开源生活实录.1.LAMP之辉](/220817-flossstyle-1.html)

从上海到北京, 是完全意外的转进,
算是参与技术社区的福利, 通过学习产生问题,
通过提问认识高人, 又通过项目证明自己能力,
从而获得机会入职更高平台...

当时能力起点:

- HTML/CSS/Javascript 中级, 能完成简单组件, 安装复杂末年
- LAMP 组合技术初级, 知道如何从无到有完成一个简单 CMS 系统
- 个人项目管理中级, 能自主持续完成一个工程从探索到交付全过程
- Python 初级, 少量工具脚本经验
- Office 高级, Word 系列用了不下5个版本, 各种排版技能都摸过
- Lisp/Haskell/Smalltalk/.. 仅仅知道属于不同范式的开发语言
- ...

### trace
> 回忆轨迹

离开上海印象最深的, 不是和各种社会关系告别, 而是:

    信用卡的钱, 不还清是会算利息的...

有了信用卡后, 根据短信通知, 每个月只还最低还款额,
感觉占了便宜, 结果想清帐离开时, 才告之要还清以往所有欠款,
结果导致人到北京时, 身上只有2千元, 只好先借住中学同学家;

事实证明, 不经过社会毒打光靠自学, 很难高速成长的哈...

SINA 毕竟是大公司, 制度比较完备, 虽然没有食堂, 但是, 工资比上海高,
那时北京消费还没现在这么神奇, 稳定下来后, 生活节奏也就恢复成类似上海的;

原先老同学家在机场附近, SINA 大厦在北四环西, 
每天早上能开车送到北四环东, 晚上打车要40多, 公交只到22:00, 还得转车, 要一个多小时,
开始两个月很累, 后来部门经理所在滑雪论坛中认识一位姐姐, 出租自己单位分的单身房,
就在国安家属小区, 距离 SINA 大厦, 自行车就一刻钟, 还有食堂...

于是, 基本上:

- 工作日, 7点半起床, 8点左右到公司
    - 6点班后, 在周边吃点儿
    - 新闻联播开始时, 回到桌前开始折腾
    - 23:00 左右回到宿舍, 刷点美剧就睡
- 周末, 10点起床, 11点左右到公司
    - 磨蹭一会就到午饭时间了
    - 吃好, 回到桌前开始折腾
    - 23:00 左右回到宿舍, 刷点美剧就睡

当然, 开始参与社区管理后, 周末一般都花在社区活动/组织/参与/...之上了;

招募俺的 HD 直属领导是 `"波仔"`, 海归派, 对 FLOSS/自由,开源软件很理解,
对 HD 通过深刻定制 FreeBSD 系统来提高单机容易, 降低整体成本很支持,
而 HD 又是啄木鸟Python技术社区创始人, 手下一批小伙伴也是通过各种技术社区挖来的,
当时 邮件技术部 可能是 SINA 内部最 geek 的部门;

因为技术不够, 所以, 被分配到过程改进小组, 负责整理开发过程, 配套流程支持系统, 
逐步提高开发效能(放到今天, 可以认为是 "内源"管理委员会类似组织);

前后除了整理一系列开发规范并监察执行之外:

- 用 PHP 开发了 CVSHelper ~ CVS 仓库助手, 并因此获得年度新人奖
- 用 Python/CherryPy 框架, 开发 Frog/研发任务管理 原型, 败给 `清风` 同时用 JAVA 开发的版本, 因为他选择的一组框架(Hibernate全家桶)都很完备,有企业级应用先例
- 在 moinmoin 基础上, 开发了一系列小插件, 将普通 wiki 系统, 拓展为包含 BBS/看板/...各种能力的CMS平台
    - 具体可参考公开分享
    - 幻灯: [Wiki 与 MoinMoin 导览](http://s5.zoomquiet.top/050703-MoinMoin/index.html)
- 启动 SEO 工程, 用 Python 对每天日志进行可视化数据图表生成
- ...

不过, 最大的转变应该是从开源资源单向受益者变成了,有意识的主动贡献者;

其中最大的拐点是发生在一次文档探查中:

- 需要整理软件系统上线详细流程, 发现一篇 FreeBSD 社区的发布工程说明书, 大为震惊, 这简直太完备了
- 进一步探查, 才发现 FreeBSD 的 UNIX 文化源头有个意外分支: GNU 精神
- 然后就看到了 [GNU 工程的哲学 - GNU 工程 - 自由软件基金会](https://www.gnu.org/philosophy/philosophy.html)
- 当然, 当年并没有中文版本, 但是, GNU 的定义漫画是看的懂的:
    - GNU ~> GNU is Not UNIX
    - 唉? 这么淘气的嘛? 在一个术语的解释中包含自身, 导致这将是一个永远循环的解释进程
- 接着看完一系列 GPL 扫盲文档, 可以说, 瞬间变成了 `自由软件原教旨主义者`

对自己以往 "我自豪, 我用盗版" 的行为深沉懊悔...
开始行动:

- 业余时间, 慢慢将所有在 Windows NT 中使用的日常软件都切换为跨平台开源软件, 比如:
    - 浏览器 -> FireFox
    - 编辑器 -> Leo
    - 资源管理器 -> muCommander
    - ...
- 结果发现 [Windows软件在Linux上的等价/替代/模仿软件列表. (Official site of the table)](http://cathayan.org/equivalentsoft-zh-cn.html)
    - 进而关注到  [cathayan/Blog on 27th Floor](http://blog.cathayan.org/item/2356)
    - 又通过文章知道了 [完全用命令行工作](https://blog.youxu.info/2008/09/10/gtd-by-cli/)
    - 对应工具探索时又挖掘到: [王珢](http://woodpecker.up.zoomquiet.top/graspOnline/learn.tsinghua.edu.cn/homepage/2001315450/idx.html)
    - ...

哗, 世界一下子以非凡的线索打开;
以往收集这种关键网页的办法是利用 IE 专用集成网页格式 .mht,
但是, 本地目录形式管理越来越多的网页并不友好, 何况还得使用专用浏览器打开;
这个问题后来想用书签来解决, 可发现, 网站并不永久存在,
很多没多久就消失在互联网中;

所以, 挖掘 FireFox 的插件, 最终定位到一款神奇的作品: ScrapBook ,
可以将网页抓取到本地, 并在浏览器内部构建一个树形目录, 以便随时查阅;

进一步发现, 抓取到本地的网页其实就是一个个的目录, 每个目录的 index.html 就是原先网页,其它则是网页对应在线资源,
也就是说 Scrapbook 基于浏览器原有功能, 完成网页内容解析并排版后,
将其所有资源保存到本地, 并对应修改所有链接为本地相对路径, 从而可以近乎 100% 的从本地还原网页内容,
而不用每次都依赖网络来下载;

于是用 Python 编写了转换脚本, 将 Scrapbook 本地形成的索引数据(就是 XML, 巧了这不熟悉嘛)转换为标准 html 索引页,
然后, 就可以共享到自己的网站中了:

经过几次迭代后变成这样:

![scrapbook](https://ipic.zoomquiet.top/2022-08-21-scrapbook-pub-zoomquiet.jpg)

这样就可以将自己收集到的认为靠谱的网页原始资料随时共享出来;

没想到这一行为, 触发了首次互联网侵权事件:

- 因为平时工作要和其它部门沟通
- 为了在家无法访问公司内网时, 也可以查询到对应分机, 就将内部通讯录给 Scrapbook 了
- 结果,被有心人看到, 针对性电话广告进来, 安全部门追查, 才发布是从我的私人网站泄漏的
- 立即责令删除, 这才发现, 互联网并不都是开放/友好的, 
- 从此对内外资料有了个自学分离习惯


北京, 毕竟是中国互联网中心, 各种资源/大会/社区一直很多, 但是, 以往并没感觉自己有机会可以进入;

改变是从创立 [CPUG](https://wiki.woodpecker.org.cn/moin/CPUG) 开始的,
之前说过, HD 创立的 啄木鸟 Python 技术社区, 是以他私人注册的 woodpecker.org.cn 域名为核心建立起来的,
但是, 毕竟 HD 又担当 SINA 关键部门主管, 平时并没有太多时间参与社区活动,
确立周末利用 SINA 顶层会议室, 来进行线下技术分享活动的主要形式后,
基本上都是俺来定期组织,
几次后, 大家感觉 `啄木鸟` 这个名字和 Python 关联不大,
就提议学习 BLUG/北京 Linux 用户组, 创立专门社区, 来组织大家学习/实践/推广 Python 技术;

是的, 这个提议人, 就是赞助邮件列表服务的 exoweb.com 公司成员,
这家公司是外国人创立的, 创始人 `白熊` , 同时也是 BLUG 创始人,
后来在各种全球技术活动中, 都不时能见到这位 `白熊` 同志;

2005.7.30 [CPUG及BPUG 成立大会](https://wiki.woodpecker.org.cn/moin/BPUG/2005-07-30)
之后, 相继也成立了其它城市的 `*PUG` 社区,
不过, 只有北京的用户组, 可以维持每个月举行一次线下 `会课`(会议+课程) 活动;
在京期间, 俺前后组织了40+期会课, 
以此为线索串联起来各种社区软件/作品/活动/人物;

比如: [CPUG第六次.豆瓣发展现状](https://wiki.woodpecker.org.cn/moin/BPUG/2006-03-26)
就是阿北对豆瓣的一次宣传, 
也正是之前 05年9月, 一次会课中,大家才知道这个网站是全栈 Python 技术开发的,
立即注册体验, 几乎可以说豆瓣在中国的线下正式发布就是在 BPUG 会课中;
所以, 大家的 豆瓣ID 都很靠谱前;
比如, 俺就是总第30位注册豆瓣的成员, 可以从豆瓣帐号头像的 ID 序号证明:
https://img9.doubanio.com/icon/ul1000030-2.jpg

又比如, Python 核心编程第2版, 骗书事件:

- [《Python 核心编程》应属于社区翻译 - Nicholas_Ding - JavaEye技术网站](http://devrel.zoomquiet.top/data/20080704230201/index.html)
- 就是 宋吉广 参与会课期间提出社区翻译出版 Python 技术图书
- 但是, 完成后, 归为自己的翻译作品

当时因为举证困难, 咨询相关法律人士后, 不得不放弃上述;
但是, 过程中形成的在线图书协作流程/工具链/经验,
倒是变成社区知识,
进一步转化为后来其它原创图书,
比如:  [可爱的Python (2009)](https://book.douban.com/subject/3884108/)
图书工程在: [ObpLovelyPython \- Woodpecker Wiki for CPUG](https://wiki.woodpecker.org.cn/moin/ObpLovelyPython)

还有: [CPUG第四次 北京师范会课](https://wiki.woodpecker.org.cn/moin/BPUG/2005-11-18)
就是通过会课, 吸引来进行互联网成人教育研究的 庄秀丽 老师,
进而受邀去分享:

- 幻灯: [漫谈自由与开源+啄木鸟开源社区介绍](http://woodpecker.up.zoomquiet.top/classes/0511-FreedomDiscuss/FreedomCPUG/s5.html)
- 录音: [051120-FreedomDiscuss.mp3](http://org.up.zoomquiet.top/ztapes/wav4zoomq/051120-FreedomDiscuss.mp3)

又通过 庄秀丽 知道 毛向辉/Issca Mao, 主办的 CBC/中国Blog大会, 接触到开放内容/网络思想,
也进行过网络会议讨论,

比如, [WeKnow-050226-Isaac](http://woodpecker.up.zoomquiet.top/classes/WeKnow-050226-Isaac.mp3), 
进而后来作为社区顾问, 帮助庄老师建立 教育大发现社区/sociallearnlab.org ;

又从 Issac Mao 认识 `Keso` 大叔, 以及他在自己家定期举行的 5g 沙龙:
(因为地点固定在 现代远大园B区8-5g 房, 所以, 命名5g, 不是通讯协议的5g)

![060315bj5gparty](https://ipic.zoomquiet.top/2022-08-21-060315bj5gparty.jpg)

- 用高端 DC 抓拍的, 就是 keso
- PS: 背对镜头, 一头油发的, 是霍矩
- PPS: 在沙龙中, 认识 `叶子` , 参与首次开源数字杂志的创办
    - 或是说众筹, 出200元认了半页版面
    - 内容就是自己的ID 解析图谱
    - 大图查阅 [2006-0627-50ren-ZoomQuiet.600dpi.png](http://0.zoomquiet.top/CPyUG/zoomquiet-design-collection/2006-0627-50ren-ZoomQuiet.600dpi.png)


还有从会课中知道的 Ubuntu 6.10 release party
![release](https://ipic.zoomquiet.top/2022-08-21-061103UBUNTU-release-party.jpg)
(2006.11.2 中科院自动化研究所, 举行)

当然, 少不了见活老爹:
![guido](https://ipic.zoomquiet.top/2022-08-21-2007GDD-guido.jpg)

2007 年, GDD/Google Develop Day 北京场, 首次见到老爹, 

![guido](https://ipic.zoomquiet.top/2022-08-21-070601GDD-guido.jpg)
(当然, 是有合影的, 猜猜哪位是 大妈?

PS: CPUG logo 左边前排, 就是 `Limodou`)


当然, 最激动的, 还是见到 RMS 本尊:
[with RMS](https://ipic.zoomquiet.top/2019-09-10-080530bj-rms-zeuux.jpg)

进而才知道, 同事 `徐继哲/Bill Xu` 是资深 GNU 社区成员,
一直负责 RMS 在中国各种活动的对接,
这下, 又一个长期参与的社区又被触发出来, 这就是 ["哲思社区"](http://www.zeuux.org/);
是 `徐继哲` 创办的自由软件文化宣传社区, 
上线时, 俺从 CPUG 社区列表, 导出8000+订阅邮箱, 导入数据,
帮助完成社区的冷启动....



### summary
> 小结

平台真的很重要, 以及进入平台后, 保持学习/积极, 持续进步, 更加重要;

在北京, 基于一份儿稳定的工作, 以及当地丰富的社会资源, 
以 FLOSS/自由,开源技术社区成员身份, 慢慢形成三个主要线索:

- Python 技术推广, CPUG 社区系列
- 开源社区治理推广, 从 教育大发现社区开始
- FLOSS布道师, 从 ZEUUX 社区开始

每个方向, 都不断发现新课题/问题/任务/知识/技能/...,
都需要持续实践,
和更多的人联合/协作/共创/...

感觉时间一下子不够用了, 怎么办?

### refer.
> 有关链接

- [CherryPy — A Minimalist Python Web Framework](https://cherrypy.dev/)
- FreeBSD 发布工程
  - 历史版本: [FreeBSD Release Engineering](http://scm.zoomquiet.top/data/20050606105135/index.html)
  - 当前版本: [Legacy FreeBSD Release Engineering | FreeBSD Documentation Portal](https://docs.freebsd.org/en/articles/releng/#_footnotedef_2)
- [GNU 工程的哲学 - GNU 工程 - 自由软件基金会](https://www.gnu.org/philosophy/philosophy.html)
- [CPUG \- Woodpecker Wiki for CPUG](https://wiki.woodpecker.org.cn/moin/CPUG)
- ["哲思社区"](http://www.zeuux.org/)
    - [Bill Xu：Richard Stallman和自由软件运动！](http://devrel.zoomquiet.top/data/20060921215100/index.html)
    - [致徐继哲先生的道歉声明 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2010/08/an_apology_to_bill_xu.html)
    - [DM9:苦短衫的故事 — 蟒营™ 怂怼录](https://blog.101.camp/dm/190914-teestory/)
- [Yin Wang's Homepage](http://woodpecker.up.zoomquiet.top/graspOnline/learn.tsinghua.edu.cn/homepage/2001315450/idx.html)
- [Isaac Mao(毛向辉)](https://web.archive.org/web/20041230205624/http://www.isaacmao.com/2004/12/29/)
- [对牛乱弹琴 | Playin' with IT - 洪波的偏见 | keso.me](https://web.archive.org/web/20190830085640/http://blog.donews.com/keso/)
- [Leo's Home Page](https://leoeditor.com/)
- [muCommander - file manager](https://www.mucommander.com/)
- [ScrapBook :: Firefox Extension](http://www.xuldev.org/scrapbook/)
    - [ZoomQuiet.io -> collection {by gen4dot2htm.py vv.190718 at:190911 18:13:08,805091}](https://zoomquiet.io/collection.html)
- [Python源码剖析 - 陈儒 ](https://read.douban.com/ebook/1499455/?dcs=subject-rec&dcm=douban&dct=3948354)
- [可爱的Python (ZEUUX)](https://book.douban.com/subject/3884108/)
    - [清风₿Ξ](https://www.douban.com/people/1001560/?_i=10890128V3HIHB)
- [庄秀丽 硕士生导师](http://fe.bnu.edu.cn/pc/cms1info/resume/50/116)
    - [教育大发现社区教研环境参考方案 - 生物教学茶吧](https://sites.google.com/site/bioteahouse/memberpage/liubaofei/xue-xi-bi-ji/jiao-yu-da-fa-xian-she-qu-jiao-yan-huan-jing-can-kao-fang-an)
    - ...

### logging
下一篇:  [开源生活实录.3.GTD之始](/220822-flossstyle-3.html)



- 220820 ZQ 发布
- 220819 ZQ init.



