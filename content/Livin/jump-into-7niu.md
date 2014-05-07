Title: 迁出RTFD.org 
Date: 2014-01-19
Tags: RTFD,qiniu,triggered
Slug: jump-into-7niu

[TOC]

# RTFD.org

- 正名 readthedocs.org
- 别名儿 `RTFD`.org

是一个良心服务, 自动将指定的任何一个仓库中的 Sphinx 工程,
根据提交事件,自动同步,编译,发布.

完全 0 配置,以及不占用大家的任何网络资源,完全免费!


## 原先

发现后,高兴的大规模使用中,并配置了 Disqus 等等好物...

## 现在

![d005a8bd08c1](https://f.cloud.github.com/assets/834231/1538179/849551c2-4cdc-11e3-9759-d005a8bd08c1.jpg)

- [Many builds stuck in "triggered" state · Issue #435 · rtfd/readthedocs.org](https://github.com/rtfd/readthedocs.org/issues/435)
- [how stop a build triggered from long time ago with finish · Issue #592 · rtfd/readthedocs.org](https://github.com/rtfd/readthedocs.org/issues/592)

突然有一天,所有图书都不编译了,卡在了哪儿,
四处一问才发现是大规模事件,
一时解决不了.

## 然后

[无责任报道~ECUG2013Con](http://techparty.org/events/2013/12/29/et-ecugcon-sz/)
知道了 7牛, 自然的就想从国外的良心服务,迁移到国内的良心服务;

### 迁移是愉快的

- 开辟 bucket
- 配置本地 `.conf`
- 配置本地自动同步脚本

run!

### 域名是绑定不了的

当然,发布出来都是:

- chaos2.qiniudn.com
- rtfd.qiniudn.com

这样的,想使用自个儿的域名,结果: 

- [无法使用交通银行支持!](http://segmentfault.com/q/1010000000386448)
- [是否可能支持大目录的 Bucket 间迁移? - 七牛云存储问答 - SegmentFault](http://segmentfault.com/q/1010000000386461)

更加杯具的是:

    chaos.zoomquiet.io  自定义     审核失败    京ICP备09067992号  
    状态说明: 2014-01-21 11:32:36 审核失败。域名未备案

绑定的域名必须有备案!

## 是也乎

好吧,,,俺只有在自个儿的主机上用 Nginx 进行反向代理了...

# Changelog

- 140119 开始总结
