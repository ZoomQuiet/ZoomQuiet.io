Title: [大妈吐糟]Tower 之功能残念集
Date: 2015-06-04 19:42
Tags: IMHO,DAMA,disscuss
Slug: 150604-chaos-tower
Author: ZoomQuiet
Status: published

[TOC]
------

> [大妈吐糟]Tower 之功能残念集

# 背景

- 在遥远的过去, Tower 刚刚发布时,就注册试用过...无感
- 在某个社区掺合折腾时,被指定使用 Tower

# 过程

- 于是各种坑
- 于是找到了 `@mycolorway.com` 内部关系,抓住接口人批量反馈
- 然后,没有了然后
- 今天见到推送硬广: [「天涯若比邻」如何用 Tower 远程协作开发产品](http://mp.weixin.qq.com/s?__biz=MjM5NDY2NDM4Mw==&mid=234095089&idx=1&sn=158f84a3d329647ce6a470aa7ccf7abe&key=c468684b929d2be2db431d557f2a04cff3bbf4c4c6e4745da3e8bb4cdb32a1babf3ef1a2f9908ad3c63e48c930f7e35e&ascene=0&uin=MTg1NDU4NTY4MQ%3D%3D&devicetype=iMac+MacBookPro8%2C2+OSX+OSX+10.10.3+build(14D136)&version=11020012&pass_ticket=bLSHZyAYyQPXsSPxVnBLhpNx61u393uer5yckacn0%2ByWRINStKhBC0qoXpOSFlMp)
- 以及专辑: [Tower - 专题 - 简书](http://www.jianshu.com/collection/0f5b8cd75ccf)
- 实在无法保持沉默... 

俺的环境:

- MAC O X 10.10.2
- FireFox 36.0.4

# 糟点s

## 150331
~有两点无法忍的问题:

- 既然文档的起草可以选择 富文本和 markdown 格式
    + 为毛,其它各种场景中的评注/讨论/回复
    + 不能支持 markdown 呢?
- 文档当前是我们主要的协调/输出/产出 工件
    + 但是,竟然不支持多种排序
    + 也不支持分目录管理
    + 实在对文档加目录复杂的话,给 tag 也是个维度哪!
- 而且,既然有 文件空间,
    - 为何不能为 markdown 格式的文档提供图片自动上传到文件目录的支持?
    - 这样就不用四处折腾先发布图片再嵌入 markdown 文本了哪


> 另外，你在文档的标题上添加 #标签# 也能对文档进行分类管理。不过，确实目前还不能对文档进行排序。

嗯啍! 这个技巧非常好哪, got it ! 加入团队文档管理规约;
不过,这也引发另外一个不能忍:

- 在文档的各种视图中
- 无论列表还是封面形式文档的链接都不是规范的
- 而是包含了一定正文内容的,比如说:

> Info 鳮汤桶 # 现象 学员 1/3 一直处在桑心状态 # 分析 - 因为负基础,纯小白 - 没有自信 - 没有从开始获得正反馈 #
方案 - 学员自身也要求定期打鳮血 - 所以,在每日小报/163任务 辅助资料/列表中... - 都追加编程小故事 ## 鳮汤 ~
收集池,如果已经使用,请在头部注明在哪儿用过 - `150329 Week2 QA` Google 是两位创始人在4周里用 Python
完成的原型 - [说走咱就走啊，天上的星星参北斗啊：Python之中国自驾游线路优化](http://www.douban.com/note/491382194/)
- [漫谈编程语言 Python .](http://www.guokr.com/blog/432591/) - [可以用 Python
编程语言做哪些神奇好玩的事情？](http://www.zhihu.com/question/21395276) -
[人生苦短，快用python.](http://www.jianshu.com/p/ec35c27f01b9) ... Zoom.Quiet
5分钟前
    https://tower.im/projects/61627695a74b444aa975a601e50ef6e7/docs/37f965c5b7804ae4823b4c2430d5b010


这种链接,用浏览器工具,自动生成 md 链接是不可用的,
进一步的:

- 在文档的具体页面中
- 页面的 title 也是不完整的,比如

> #TASK# ... - Tower
    https://tower.im/projects/61627695a74b444aa975a601e50ef6e7/docs/290f336fc10b441fb51c5bd522eaf36d/

而明明此文档的标题是

    #TASK# OMOOC.py 学员预期管理

一点儿也不长

俺的建议是,既然包含了 md 格式的支持,
那么就应该从一个重度 md 用户的角度出发自,真正优化内部链接形式


PS:
如附件, 使用了你提醒的 标题 TAG 技巧后,
文档列表破行!


![屏幕快照 2015-03-31 17.10.03.png](http://upload-images.jianshu.io/upload_images/27562-65ad1211eb6c0e8d.png)



## 150401
如截屏

![屏幕快照 2015-04-01 20.45.18.png](http://upload-images.jianshu.io/upload_images/27562-4594aef5eeefaa0d.png)

经提醒,我们注意到 Tower 文档竟然有文档修订历史以及可视化对比的功能!

但是,异常期待有一个改进:

- 如附件截屏 视图中
- 如果能将修订变更的字数/行数直接显示在版本行中,对团队有更大的提示!
- 否则,我们得逐一点击,并上下拖拉,才能发现修订之处
- 注意!
    + 随着文档的大规模使用
    + 文档是能轻松突破300行,5屏以上的!
- 进一步的:
    + 不应该在对比视图中显示全文
    + 用颜色来标标识修订行为
    + 这明显是对 Word 修订模式的无脑复刻!
    + 我们是 Tower 文档,不是 Office 在线哪!

所以,俺建议:

- 文档 修改历史 界面中
- 每行后面追加 修订字数,变更行数
- 点击进入后,是 diff 格式,类似: [appended YC 7.8 · 4e5f200e -
GitCafe](https://gitcafe.com/wiki4zq/markdoc4zq/commit/4e5f200e2a4d2d493e1cf88c0403b63469081dd5)

再进一步的:

- 如果文档,能提供每个项目一个文档 git 仓库
- 来给高级团队通过 git 仓库进行分布式快速修订
- 类似 github-wiki 的交互流程
- 那就太赞了!

## 150402
~ 如截屏


![INFO  鳮汤桶   Tower.png](http://upload-images.jianshu.io/upload_images/27562-08b29209611e6df4.png)



- 现象: 团队中常用文档,稍微一积累,就超过3屏以上!
- 问题: 导致无法很快的跳转到合理的位置使用内容!
- 建议: 追加浮动 TOC !
    + 不用在 md 格式中嵌入 `[TOC]` 锚点
    + 直接在渲染引擎中追加!
    + 自动对 H1~3 的正文内容构建浮动的标题索引
    + 并追加跳到底部评注讨论区的索引
- 进一步的:
    + 文档创建/修订信息, 已经在相关子页面包含了
    + 就不应该在底部评注区详细列出
    + 应该进行相似修订记要的折叠处理




## 150403

今天进行多个文档编辑时,又发现一个问题:

- Tower 中编辑文档是弹出新页面:
    + 完成编辑后,点击,当前编辑页面消失,焦点回到哪个页面就是天知道了
- 这不科学!反人性!
    + 参考 简书/github/medium/.... 的编辑流程?!
    + 不能因为国人网站为了流量,拼命加开页面
    + Tower 也这么来哪!

## 150408

因为很多事务性文案,在 文档 中起草时,
其实都是在原先基础上增减的,
所以:

- 文档应该有 复制为 功能
- 或是提供模板功能也好
  + 类似 moinmoin 的特殊前缀文章视为模板,
  + 在创建新文章时,可以从模板列表中选择使用哪种模板
  + 这样有利于团队内部形成良好的文档一致性习惯

实话讲, Tower 现在文档所有引发的不适,都是因为和现有 类似 团队文档工具的体验差异引发的!

- gitbook 根治所有毛病!
- 建议内建 gitbook 引擎
- 给高级团队一个 git 仓库,自动响应 push 行为,编译发布内部 gitbook 图书!

很久以来, Tower 的链接设计是俺最无法理解的一个 非功能设计:

https://tower.im/projects/61627695a74b444aa975a601e50ef6e7/docs/6654630279f743a8972b6869cf9ea89d/

是的, 61627695a74b444aa975a601e50ef6e7 是我们项目名的 hash 值,另外的也看的出来,
但是,这样的 URI 对使用者而言是什么感觉呢?!
无视我们的存在哪,,,
请观察其它所有同类服务的 URI, 都是类似:

- [项目名].tower.im//docs/[关键字]-[短hash]
- 一般都在80个字符以内的,比如: https://techparty.hackpad.com/150310-Mini.0-c1xxk56HsTt

所以,请改进吧, 为了大家喜欢上 Tower
