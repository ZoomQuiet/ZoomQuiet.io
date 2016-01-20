Title: ScrapBook彻查成果
Date: 2014-07-11
Tags: scrapbook,python,howto,mavericks
Slug: zq-chk4scrapbook


[TOC]


## 背景
参考:[我的学习&工具](http://wiki.woodpecker.org.cn/moin/ZqStudy/MyLearningSkill)

从06年,就将个人网络资料收集/整理/发布,
切换为主力使用 [ScrapBook](http://www.xuldev.org/scrapbook/) .

这一下子就8年过去了,常用系统也从 Ubuntu 切换为 MAC,
收集的本地网页也超过了8万个,早已被迫进行了分库.

自动发布的

- http://floss.zoomquiet.io
- http://skm.zoomquiet.io

也成为一些朋友常常挖掘的资料库.

可以说, ScrapBook 在 everynote 流行之前,就成功的解决了俺主要的在线网页资料为主的,
外部知识仓库的收集/整理/组合/复用/发布 等等基本功能/服务.

而且, 也通过Python ,完成了辅助的小脚本工具,配合 个人主机/7牛CDN,
完成了自动化的差异发布.

### 可是!
参考: [ScrapBook 生存指南](http://blog.zoomquiet.io/livin-scrapbook.html)

- 从去年开始, 本地 `FLOSS` 仓库,就已经无法正常进行标准搜索了,一搜索,整个 FireFox 就僵死.
- 而且,从其它仓库切换进入 FLOSS 时,要等待半分钟以上...


## 期待
实在太常用,所以,无法忍,而且也不打算切换到 everynote 什么的其它平台上,
作为一头合格的程序猿,就是要自个儿折腾通透哪!

所以,先决定目标:

1. 通过进一步拿合理分仓库,有效减少每个仓库包含的网页数量
1. 通过脚本分析 `scrapbook.rdf` 数据库来清除多余节点(隐藏的无效的)
1. 通过脚本分析 对应 `data/` 目录中的网页子目录,清除多余的
1. 针对全新的分仓库,建立对应的 7牛 空间,以及对应的 `*.zoomquiet.io` 子站发布

总之就是要加速,无论本地/远程

### 数据结构
为了大家平滑的理解折腾之处,先简要说明一下 ScrapBook 的数据结构:

```
XX仓库/     对应 Multi-ScrapBook 开启后,不同的Book
  +- data   实际本地网页存放入口, 类似 20050205102119 的子目录
  +- tree   导出目录树后的 html 入口
  +- ...
  `- scrapbook.rdf 插件界面使用的 xml 数据仓库
```

`scrapbook.rdf 的关键数据约定`

```
<?xml version="1.0"?>
<RDF:RDF xmlns:NS2="http://amb.vis.ne.jp/mozilla/scrapbook-rdf#"
         xmlns:NC="http://home.netscape.com/NC-rdf#"
         xmlns:RDF="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  ...
  主体内容
</RDF:RDF>

根列表:
<RDF:Seq RDF:about="urn:scrapbook:root">
    %(rdf_li)s
  </RDF:Seq>

目录容器:
<RDF:Seq RDF:about="urn:scrapbook:%(rdf_item)s">
    %(rdf_li)s
  </RDF:Seq>

目录节点条目:
<RDF:li RDF:resource="urn:scrapbook:%(rdf_item)s"/>

目录节点:
<RDF:Description RDF:about="urn:scrapbook:%(rdf_item)s"
        NS2:type="folder"
        NS2:id="%(rdf_id)s"
        NS2:title="%(rdf_title)s"
        NS2:chars=""
        NS2:icon=""
        NS2:source=""
        NS2:comment="" />

页面节点:
<RDF:Description RDF:about="urn:scrapbook:%(rdf_item)s"
        NS2:type="%(rdf_type)s"
        NS2:id="%(rdf_id)s"
        NS2:title="%(rdf_title)s"
        NS2:comment="%(rdf_comment)s"
        NS2:icon="%(rdf_icon)s"
        NS2:source="%(rdf_source)s" 
        NS2:chars="UTF-8" />

笔记节点:
<RDF:Description RDF:about="urn:scrapbook:%(rdf_item)s"
        NS2:type="note"
        NS2:id="%(rdf_id)s"
        NS2:title="%(rdf_title)s"
        NS2:chars="UTF-8"
        NS2:comment=""
        NS2:icon=""
        NS2:source=""/>

分割线节点:
<NC:BookmarkSeparator RDF:about="urn:scrapbook:%(rdf_item)s"
        NS2:type="separator"
        NS2:id="%(rdf_id)s"
        NS2:title=""
        NS2:chars=""
        NS2:comment=""
        NS2:icon=""
        NS2:source="" />


```

以上 `%(rdf_id)s` 之类是 Py 内置模板的语法,
在 `scrapbook.rdf` 实例中,都是形如: `20050205102119`

## 折腾

纪要一下折腾的过程中,要命的关键过程/代码

### 清查

一切开始之前,的体积:

```
$ du -h * 
...
5.6G    ZqDevRel
6.5G    ZqFLOSS
3.7G    ZqSKM
...

$ ls ZqDevRel/data/ | wc
   26214   26214  393210

# 计划切分为
  -> zqCoder 
  -> zqSMM

$ ls ZqFLOSS/data/ | wc
   30767   30767  461505

# 计划切分为
  -> zqDevRes
  -> zqSCM   
  -> zqPythonic
```

先在仓库中,根据拆分目标,将内容树收纳到对应的目录中,
以便复制,加载后,快速删除.

#### pax

`pax` 是个好工具,原先习惯性的用 `cp` 那叫个慢!
搜索才知道,大量小文件的迁移就应该用 `pax`
于是简单的起个背景周末跑吧....


```
$ du -hs *
...
5.7G    ZqDevRel
  5.7G    zqCoder
  5.7G    zqSMM

6.5G    ZqFLOSS
  6.5G    zqDevRes
  6.5G    zqPythonic
  6.5G    zqSCM

...
4.0K    scraptools
...
```

体积占用激增3倍!

然后,逐一用 ScrapBook 加载新的目录

#### 手工删除目录树
再对比几个仓库的体积:

```
~/KuaiPan/zScrapBook
$ ls ZqFLOSS/data/ | wc -l
   30767

$ ls zqSCM/data/ | wc -l
   25320

$ du -hs *
...
5.3G    data
...

~/KuaiPan/zScrapBook
$ ls zqDevRes/data/ | wc -l
   24045

$ ls zqPythonic/data/ | wc -l
   24294

$ ls zqSCM/data/ | wc -l
   25319

```

#### 严正的不科学!
手工折腾了半天,却发现几乎没有释放多少空间出来,
好象总是有 20000 左右的目录,是不存在的页面节点...

### 解析
首先,


### 重构

[xml containing 1 child · Issue #14 · martinblech/xmltodict](https://github.com/martinblech/xmltodict/issues/14)

`dict_constructor`

### 删除




## 回顾

JS 在 FireFox 的确不给力哪...


```
$ du -hs *
...
957M  ZqDevRel
866M  ZqFLOSS
349M  ZqKss
3.4G  ZqSKM
...
1.0G  _chaos
5.2G  _stuff
...
424K  scrapbooktools
766M  zqCoder
1.0G  zqDevRes
1.4G  zqPythonic
1.4G  zqSCM
564M  zqSMM
```

为什么,在 700M 的 zqCoder 仓库中无法搜索,但是, 3.4G 的ZqSKM 中就可以?!

认真对比,从重建的空仓库的 .rdf 中,发现:

```
<RDF:Seq RDF:about="urn:scrapbook:search">
....
</RDF:Seq>
```

这个节点中包含有意外的几万条记录!

```
for seq in doc['RDF:RDF']['RDF:Seq']:
    if 'urn:scrapbook:search' == seq['@RDF:about']:
        seq.pop('RDF:li')
        break
```

几行代码解决!


### 数据新结构

### 功能开关


## 时间帐单

```
+ 3.5H 用pax 复制,手工清除多余树
+ 1.5H 重新理解自个儿的脚本,加载自制数据结构到湿件
+ 1.0H 追加走查功能 
+ 2.0H 调试走查,优化输出,明确可清除无效节点的数量级
+ 1.5H 尝试用 click 改进功能开关,未果
+ 2.0H 对比测试不同的解析库
+ 1.0H 用xmltodict 重构原先的 走查功能
+ 1.5H 根据比对的需求,改进 xmltodict 的数据结构,追加 K/V 复用
+ 2.0H 再复制测试仓库,用 sh 小心的测试实际删除行为
+ 1.0H 通测
+ 2.5H 批量处置7 个新旧仓库,清删除 16万+ 个无用目标, 近25G+ 空间释放
+ 4.0H 整理代码, 组织文档

24.5H+ 自然时间, 3+天业余时间
```

- 140909 才算完成一个可以看的版本
- 140711 完成所有功能,启动文档回顾


#   140708 ScrapBook 分库


## +2H click

果然,清查出有大量, FLOSS 中当初没有合理清除的节点
从 ROOT 引发的树中挂不上的


## +2H 实际清减

[sh 1.08 — sh v1.08 documentation](http://amoffat.github.io/sh/)

    from sh import rm
    ...
    print(rm("-Rfv", del_dir))



- 用 sh 删除目录

:

        tree_nodes:  3574
        exp_items:  4164
        dirs:  590
        DESC : 24190
        chaos: 20616
        有效: 3574
    $ ls reDevRel/data/ | wc -l
        2996


- 用 lxml/模板 重构 rdf

人肉来总是感觉不对,

尝试:


### lxml
    忒复杂!!!

### untangle
[stchris/untangle](https://github.com/stchris/untangle)

    RDF:Seq         579
    RDF_Description     24190
    NC:BookmarkSeparator    57
    <open file '_chaos/scraotools_reDevRel.pkl', mode 'wb' at 0x100666ed0>
            exp_level_idx() RUNed~ 2263.57079 ms

快,但是,无法Dump,而且书写不直觉, 要将 ":" 变成 "_"
    obj.RDF_RDF.RDF_Description


    <open file '_chaos/scraotools_reDevRel.pkl', mode 'wb' at 0x100769ed0>
    Traceback (most recent call last):
      File "scraptools/zq_chk4scrap.py", line 457, in <module>
        RDFD = exp_level_idx(MYBOOK)
      File "scraptools/zq_chk4scrap.py", line 161, in cal_time
        result = func(*args)
      File "scraptools/zq_chk4scrap.py", line 205, in exp_level_idx
        pickle.dump(obj.RDF_RDF, output)
      File "/Users/zoomq/.pyenv/versions/2.7.6/lib/python2.7/pickle.py", line 1370, in dump
        Pickler(file, protocol).dump(obj)
      File "/Users/zoomq/.pyenv/versions/2.7.6/lib/python2.7/pickle.py", line 224, in dump
        self.save(obj)
      File "/Users/zoomq/.pyenv/versions/2.7.6/lib/python2.7/pickle.py", line 286, in save
        f(self, obj) # Call unbound method with explicit self
      File "/Users/zoomq/.pyenv/versions/2.7.6/lib/python2.7/pickle.py", line 719, in save_inst
        getstate = obj.__getstate__
      File "/Users/zoomq/.pyenv/versions/276chaos/lib/python2.7/site-packages/untangle.py", line 66, in __getattr__
        raise IndexError('Unknown key <%s>' % key)
    IndexError: Unknown key <__getstate__>


### xmltodict
[martinblech/xmltodict](https://github.com/martinblech/xmltodict)

    [u'RDF:RDF']
    RDF:Seq         579
    RDF:Description     24190
    NC:BookmarkSeparator    57
            exp_level_idx() RUNed~ 4997.31612 ms

慢,但是,能 dump 而且书写直觉
    doc['RDF:RDF']['RDF:Seq']

    [u'RDF:RDF']
    RDF:Seq         579
    RDF:Description     24190
    NC:BookmarkSeparator    57
    <open file '_chaos/scraotools_reDevRel.pkl', mode 'wb' at 0x10f26d420>
            exp_level_idx() RUNed~ 16878.75390 ms

同时,能反写出XML 来!

主要问题是行为不统一!

    <RDF:Seq RDF:about="urn:scrapbook:item20070113201921">
      <RDF:li RDF:resource="urn:scrapbook:item20070113201940"/>
      <RDF:li RDF:resource="urn:scrapbook:item20070113201941"/>
    </RDF:Seq>


时 唯一的 RDF:Li 不是 List!!

    K2SEQ[crt_id]>RDF:Li OrderedDict([(u'@RDF:resource', u'urn:scrapbook:item20070113201921')])
    K2SEQ[crt_id]['RDF:li'].len:: 1
        <class 'collections.OrderedDict'>
    K2SEQ[crt_id]>RDF:Li @RDF:resource
         try crt_node.keys:
    @RDF:resource
    K2SEQ[crt_id]>RDF:Li OrderedDict([(u'@RDF:resource', u'urn:scrapbook:item20070527160000')])
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    K2SEQ[crt_id]>RDF:Li OrderedDict([(u'@RDF:resource', u'urn:scrapbook:item20061006133550')])
    K2SEQ[crt_id]['RDF:li'].len:: 9
        <type 'list'>


[odd parse for same xml structure · Issue #67 · martinblech/xmltodict](https://github.com/martinblech/xmltodict/issues/67)


### 4H 折腾明白了:

    $ python scraptools/zq_chk4scrap.py reDevRel/
    /Users/zoomq/mnt/快盘/zScrapBook/reDevRel/scrapbook.rdf
    [u'RDF:RDF']
    RDF:Seq         579
    RDF:Description     24190
    NC:BookmarkSeparator    57
    <open file '_chaos/scraotools_reDevRel.pkl', mode 'wb' at 0x10f17a660>
            exp_level_idx() RUNed~ 17073.48084 ms

    _chaos/scraotools_reDevRel.pkl
    RDF:ROOT            13
    RDF:Seq         578
    RDF:Description     24190
    NC:BookmarkSeparator    57
            _load_pkl() RUNed~ 7872.95103 ms

         _RIGHT_NODES: 6926
         RIGHT_NODES: 3631
            re_xmltodict_rdf() RUNed~ 191.21003 ms

有这么多垃圾!

    24190 vs 3631 !!!!


但是,居然无法一次性清理干净?!

一扫::

    $ python scraptools/zq_chk4scrap.py reDevRel/
    /Users/zoomq/mnt/快盘/zScrapBook/reDevRel/scrapbook.rdf
    [u'RDF:RDF']
    RDF:Seq         579
    RDF:Description     24190
    NC:BookmarkSeparator    57
    <open file '_chaos/scraotools_reDevRel.pkl', mode 'wb' at 0x10f2376f0>
            exp_level_idx() RUNed~ 17013.92913 ms

         _RIGHT_NODES: 6926
         RIGHT_NODES: 3631
    clean notes:    11153
    cleanned DESC:  13037
    <open file '_chaos/scraotools_reDevRel.pkl', mode 'wb' at 0x10eecff60>
    _chaos/scrapbook_reDevRel.rdf
            re_xmltodict_rdf() RUNed~ 131239.34913 ms


2扫:


    $ python scraptools/zq_chk4scrap.py reDevRel/
    _chaos/scraotools_reDevRel.pkl
    RDF:ROOT    13
    RDF:Seq         578
    RDF:Description     13037
    NC:BookmarkSeparator    57
            _load_pkl() RUNed~ 4292.33599 ms

         _RIGHT_NODES: 6926
         RIGHT_NODES: 3631
    clean notes:    5506
    cleanned DESC:  7531
    <open file '_chaos/scraotools_reDevRel.pkl', mode 'wb' at 0x108874f60>
    _chaos/scrapbook_reDevRel.rdf
            re_xmltodict_rdf() RUNed~ 44531.90279 ms


3扫::

    $ python scraptools/zq_chk4scrap.py reDevRel/
    _chaos/scraotools_reDevRel.pkl
    RDF:ROOT    13
    RDF:Seq         578
    RDF:Description     7531
    NC:BookmarkSeparator    57
            _load_pkl() RUNed~ 3115.18502 ms

         _RIGHT_NODES: 6926
         RIGHT_NODES: 3631
    clean notes:    2616
    cleanned DESC:  4915
    <open file '_chaos/scraotools_reDevRel.pkl', mode 'wb' at 0x105d1edb0>
    _chaos/scrapbook_reDevRel.rdf
            re_xmltodict_rdf() RUNed~ 19026.94511 ms


4扫::

    $ python scraptools/zq_chk4scrap.py reDevRel/
    _chaos/scraotools_reDevRel.pkl
    RDF:ROOT    13
    RDF:Seq         578
    RDF:Description     4915
    NC:BookmarkSeparator    57
            _load_pkl() RUNed~ 2528.49293 ms

         _RIGHT_NODES: 6926
         RIGHT_NODES: 3631
    clean notes:    1045
    cleanned DESC:  3870
    <open file '_chaos/scraotools_reDevRel.pkl', mode 'wb' at 0x10429ced0>
    _chaos/scrapbook_reDevRel.rdf
            re_xmltodict_rdf() RUNed~ 11538.43212 ms

5扫:

    $ python scraptools/zq_chk4scrap.py reDevRel/
    _chaos/scraotools_reDevRel.pkl
    RDF:ROOT    13
    RDF:Seq         578
    RDF:Description     3870
    NC:BookmarkSeparator    57
            _load_pkl() RUNed~ 2422.85681 ms

         _RIGHT_NODES: 6926
         RIGHT_NODES: 3631
    clean notes:    286
    cleanned DESC:  3584
    <open file '_chaos/scraotools_reDevRel.pkl', mode 'wb' at 0x102c5d300>
    _chaos/scrapbook_reDevRel.rdf
            re_xmltodict_rdf() RUNed~ 9368.47901 ms


6扫::

    $ python scraptools/zq_chk4scrap.py reDevRel/
    _chaos/scraotools_reDevRel.pkl
    RDF:ROOT    13
    RDF:Seq         578
    RDF:Description     3584
    NC:BookmarkSeparator    57
            _load_pkl() RUNed~ 2225.17014 ms

         _RIGHT_NODES: 6926
         RIGHT_NODES: 3631
    clean notes:    10
    cleanned DESC:  3574
    <open file '_chaos/scraotools_reDevRel.pkl', mode 'wb' at 0x102c2af60>
    _chaos/scrapbook_reDevRel.rdf
            re_xmltodict_rdf() RUNed~ 8464.92100 ms


7扫:

    $ python scraptools/zq_chk4scrap.py reDevRel/
    _chaos/scraotools_reDevRel.pkl
    RDF:ROOT    13
    RDF:Seq         578
    RDF:Description     3574
    NC:BookmarkSeparator    57
            _load_pkl() RUNed~ 2317.77310 ms

         _RIGHT_NODES: 6926
         RIGHT_NODES: 3631
    clean notes:    0
    cleanned DESC:  3574
    <open file '_chaos/scraotools_reDevRel.pkl', mode 'wb' at 0x1021b3030>
    _chaos/scrapbook_reDevRel.rdf
            re_xmltodict_rdf() RUNed~ 8694.52500 ms


### 2小时 目录对比

sh->ls 出来时,

是 STDOUT 有隐藏字符!
兰色...居然没有意识到!


    20041214101930
    <type 'str'>
    Traceback (most recent call last):
      File "scraptools/zq_chk4scrap.py", line 724, in <module>
        mv_chaos_data(REPO_NAME, XRDF)
      File "scraptools/zq_chk4scrap.py", line 524, in mv_chaos_data
        print len(int(li)) #.strip()
    ValueError: invalid literal for int() with base 10: '\x1b[1m\x1b[34m20041214101930\x1b[39;49m\x1b[0m'



### 140710 18:04
完成初步完备流程:

- 从原始 scrapbook.rdf 读入为 Py 对象
- 模拟肉眼巡查, walk 出显示的合法内容数据集
  - 加入其它辅助KV 节点,写为中间工作 .pkl
  - 加载 工作 .pkl 到内存
  - 对比原始 .rdf 数据中的节点和 walk 出来有效的,逐一清除无效的
    - 必须,尝试多次,直到清除干净
    - 为毛...?
- 对比实际目录和有效节点ID 的关系,将无效的,mv 到其它目录完成净化



## TODO

- 解决反复清查的问题
- 提高效率

:

    $ du -hs *
    5.1G    ZqDevRel
    950M    reDevRel
        5.2G    zqCoder
        4.9G    zqSMM
    8.0M    _chaos
    4.2G    _stuff

    6.5G    ZqFLOSS
        5.2G    zqDevRes
        5.2G    zqPythonic
        5.3G    zqSCM
    3.7G    ZqSKM
