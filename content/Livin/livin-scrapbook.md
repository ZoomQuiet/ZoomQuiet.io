Title: ScrapBook 生存指南
Date: 2014-02-26
Tags: RTFD,qiniu,triggered
Slug: livin-scrapbook

[TOC]


`7.7G    ZqFLOSS` 复制改进后,为毛多了?!


    zoomq @ MBP111216ZQ in ~/KuaiPan/zScrapBook
    $ du -hs *
    4.0K    7niu-devrel.json
    4.0K    7niu-floss.json
    4.0K    7niu-skm.json
    5.5G    ZqDevRel
    6.4G    ZqFLOSS
    3.5G    ZqSKM
     9.5M    scraotools_ZqDevRel.pkl
     14M    scraotools_ZqFLOSS.pkl
    1.6M    scraotools_ZqSKM.pkl


## 背景
很久以前, 俺和大家一样,收集整理网络资源的习惯组织方式是:

- 目录 (htm 抓网页)
- 刻光盘

然后,发觉目录/内容超过两屏后基本什么也找不到了,
当然,后来使用了 google 的桌面搜索,
当然,那时还是 M$ 时代,

不过,在这个折腾的过程中,也明确了:

- 资料的收集要配合自个儿的知识框架
- 搜索也必须知道搜索什么,而中文的岐义/复义/多义 太多,基本不可用作搜索关键词
- pdf/word/ppt 之类的专用格式文档基本是废的,无法快速使用

所以,后来上了 FireFox 后,用上了 ScrapBook 这一杀手级扩展,
资料的收集过程变成:

1. 浏览过程中,自然的挖掘,随手抓取到临时分类中
1. 快速精读一遍,用内置高亮工具,标注重点
1. 合理移动到对应的分类中
1. 使用时,直接进入对应分类,或是用标题关键词搜索出来

ScrapBook 是结合了本地目录管理+内置全文搜索的浏览器扩展工具.

一切安定了起来

## 发展

慢慢的,快速收集整理了上万个网页,才发现,好的网页内容:

- 一般不长久,原始网站总是很快死亡
- 而相同的内容在多次转抄过程中总是有丢失
- Google 的搜索镜像也不一定靠谱
- 大家通过书签记录的网页,基本上90天后就很难点击开了

所以,就有了将个人收集分享出来的想法:

- ScrapBook 有导出目录树的功能
- 所以,一开始就是简单的进行导出
- 然后,用 rsync 同步到自个儿的官网空间

但是,慢慢的,网络数量突破3万时,根索引的目录树就超过了10M!

- 大家就反应首页很难打开了
- 这才知道真的有人在俺的分享网站中找东西!

于是有了: [scrapbooktools/expidxlevels.py at master · ZoomQuiet/scrapbooktools](https://github.com/ZoomQuiet/scrapbooktools/blob/master/expidxlevels.py)

单纯的原样分享就变成了:

- [{ZqFLOSS} index tree exp. As HTML - ScrapBook](http://floss.zoomquiet.io/tree/)
- [{ZqSKM} index tree exp. As HTML - ScrapBook](http://skm.zoomquiet.io/tree/)

## 问题

但是,突然有一天,无法在常用的 ScrapBook 界面中对标题进行搜索了
能将整个浏览器都卡死...

再查, `ZqFLOSS` 目录已经突破5万页面,索引 xml 也超过了 25 M!

不得以再次分库,并分享:

- [{ZqDevRel} index tree exp. As HTML - ScrapBook](http://devrel.zoomquiet.io/tree/)


可是,奇怪的是分离了本地 ScrapBook 数据仓库后,问题依旧,
而且, `ZqFLOSS` 分离前有 `7.7G`;
可是拆分为两个仓库后,体积相互加,竟然几近 double !

于是怀疑多次手工批量删除时,造成了孤悬文件,然后就有了:

- [scrapbooktools/chkscrap.py at master · ZoomQuiet/scrapbooktools](https://github.com/ZoomQuiet/scrapbooktools/blob/master/chkscrap.py)
- [scrapbooktools/scrap_re_rdf.py at master · ZoomQuiet/scrapbooktools](https://github.com/ZoomQuiet/scrapbooktools/blob/master/scrap_re_rdf.py)

分别对数据目录,以及索引 xml 进行清查

但是,只有几个丢失...

## 分析
目测是 FireFox 升级,强行切换了JS 解析内核后,带来的少数不兼容,
导致了对一定体积的 XML 进行内存调度时,出了问题...

暂时无法解决.

已经向作者吼过,看RP 了...


# Changelog

- 140405 无解的快速总结
- 140217 开始回顾
