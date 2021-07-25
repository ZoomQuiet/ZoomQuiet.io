Title: 拙见/ DNS之殇
Date: 2020-03-31 10:42
Modified: 2020-03-31 12:42
Authors: ZoomQuiet
Category: MurMur
Tags: IMHO, DNS, logging
Summary: MurMur/ DNS in china is one kinds of sadding song
Slug: imho-murmur-dns-sad-story


这是大妈在 **ZoomQuiet** 的第**011**篇原创

> 普通程序老猿一则感叹...

-------------
## 背景

自从能家庭上网, 我们就一直和网络服务供应商在斗智斗勇;

最早 瀛海威 的互联网广告是:

    中国人离信息高速公路有多远
    ———向北1500米

现在想, 是真的良心...

-------------
## 现象

- gitlab.com 每天不同时段打开的速度完全不同
- github-pages 发布的静态网站经常无法打开
- git pull 工作仓库有时说仓库不存在
- ...


而家中的互联网接入有这么几个:

- 移动宽带, 手机158套餐送的, 很多年了, 也自动升级到 500M 光纤, 配 Nighthawk R7000 无线路由器
- 移动宽带, 手机98套餐送的, 很多年了, 也自动升级到 300M 光纤, 原配 TP-Link 无线路由器
- 广东有线宽带, 电视台强行升级, 原配杂牌 AP
- 华为 mifi , 自驾旅游时用, 配置飞猫物联网流量卡, 600G/月


-------------
## 嗯哼

101.camp 是无意中在 naemcheap 抢到的域名, 用 github-pages 发布,
基于 cloudflare 进行加速.

没想到除了 mifi 其它基本无法打开,
感觉不对味儿.

追查了一下, 发现, cloudflare 发布的公共 DNS 服务: 1.1.1.1 

- 除了 mifi 无线接入电脑后, 可以 Ping 通
- 其它所有 wifi 热点, 接入后, 根本不解析
- 这就很说明问题了...

![R7000](http://ydlj.zoomquiet.top/ipic/2020-03-31-cfgAP.jpg)

> 追查了一下国内可用公共 DNS 服务, 在路由器上配置

![cnPUBDNS](http://ydlj.zoomquiet.top/ipic/2020-03-31-cnPUBDNS.jpg)

对比, 无法配置 AP 的有线宽带:

![cnNOMDNS](http://ydlj.zoomquiet.top/ipic/2020-03-31-cnNOMDNS.jpg)

以及一直可以访问, 但是很慢的 mifi :

![mifi](http://ydlj.zoomquiet.top/ipic/2020-03-31-mifi.jpg)


-------------
## 所以

```python

但行好事
莫问前程
好好学习
天天向上

```

这儿的 `好`, 是四声, 自己喜欢的事儿.

什么是不惑?

> 从心所欲不逾距

也就是说, 将欲望本身进行 hacking , 从源头清除可能触发和谐的念头.

那么, 具体怎么作呢?

这是另外一个系列的嗯哼了...


-------------
## refer.

- [1.1.1.1 好记牛逼 - Cloudflare 推出全球平均速度最快的 DNS！ - 异次元软件下载](https://www.iplaysoft.com/p/cloudflare-dns)
    + [腾讯旗下 DNSPod 也推出公共 DNS 解析服务 Public DNS+ - 异次元软件下载](https://www.iplaysoft.com/news/2773)
    + [阿里公共 DNS 解析服务器 - 上网加速、无广告、无劫持、全国高速节点、低延迟响应 - 异次元软件下载](https://www.iplaysoft.com/alidns.html)
- ...
- 豆列:[蟒营™101.camp](https://www.douban.com/doulist/119293075/)


文中链接感谢["文章助手"的助手](https://linux.cn/static/tools/a.html) 的支持,
(来自 [LINUX中国]((https://linux.cn/article-11850-1.html)) 的小应用)

- 点击, 将自动跳入小应用, 并复制链接到剪贴板
- 然后, 打开浏览器, 复制到地址栏, 就能访问了
- 好处, 避开了微信内置特殊浏览器的有关屏蔽策略
- 问题, 操作复杂了, 要打开手机上的浏览器, 如果在桌面微信则无法使用


JD 下单链接 -> 点击后再打开浏览器复制到地址栏访问 -> 俺能获得少许佣金:

- [寻路中国&江城(共2册)](https://union-click.jd.com/jdc?e=&p=AyIGZRNdEgMTDlEbXCUHEANXGlgSCxsOUysfSlpMWGVCHlBDUAxLBQNQVk4YCQQAQB1AWQkFHUVBRhkSQw9THUJVEEMFSgxUVxZPI0AOFwVRGVoWBRsOXB1rC2RaQQNlDEFhZ0NcT159dhtGKX5bUw4eN1QrWxQDEQVWGFkXBSI3VRxrVGwXBl0cXiUDIgdRElkdBxIAUxhcFwsiAFUSa35cTFs1XwNBRyI3ZRhrJTISN1YrGXsBQVcFElNCARMPAU5eEVIVD1wfDxMDFQcBTwkQVkJXUytZFAMWDg%3D%3D)
- ...

-------------
>> NN 3969

好文笔,感叹号年度配额: **1/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):


```python

私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开课程: 蟒营 (订阅号: Mainium)
历史吐糟: Chaos42 (订阅号 PythoniCamp)

as 核心组织者:
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        TFUG珠海 (订阅号: ZH_TFUG)
```

-------------

