Title: 如何持证 (SSL) 开车
Date: 2019-01-30 10:10
Tags: MAC,Livin,SCM,SSL
Slug: jump-into-ssl

[TOC]

## BG

[Let's Encrypt 2019：带来更多振奋人心的新功能 - 开源中国](https://mp.weixin.qq.com/s/qig7l-Tc1P6gp_Ldm2bQJg)

被成功安利...

## goal

因各种网站发布的年代, 使用技术各不相同, 但是好在都能依托 `*-pages` 服务快速发布:

- github/gitlab 为核心
- 免费 SSL 认证为基础
- 最好能一次配置长期可用

## logging

### gh-pages

原先的:

> ༄  dig blog.zoomquiet.io +nostats +nocomments +nocmd

    ; <<>> DiG 9.8.3-P1 <<>> blog.zoomquiet.io +nostats +nocomments +nocmd
    ;; global options: +cmd
    ;blog.zoomquiet.io.     IN  A
    blog.zoomquiet.io.  600 IN  CNAME   zoomquiet.github.io.
    zoomquiet.github.io.    3251    IN  A   185.199.108.153
    zoomquiet.github.io.    3251    IN  A   185.199.109.153
    zoomquiet.github.io.    3251    IN  A   185.199.110.153
    zoomquiet.github.io.    3251    IN  A   185.199.111.153


- 暂停原先 `CNAME` -> `ZoomQuiet.github.io.`
- 追加新 `A` 记录->`185.199.111.153`
- 立即...

> ༄  dig blog.zoomquiet.io +nostats +nocomments +nocmd

    ; <<>> DiG 9.8.3-P1 <<>> blog.zoomquiet.io +nostats +nocomments +nocmd
    ;; global options: +cmd
    ;blog.zoomquiet.io.     IN  A
    blog.zoomquiet.io.  600 IN  CNAME   zoomquiet.github.io.
    zoomquiet.github.io.    2989    IN  A   185.199.111.153
    zoomquiet.github.io.    2989    IN  A   185.199.108.153
    zoomquiet.github.io.    2989    IN  A   185.199.109.153
    zoomquiet.github.io.    2989    IN  A   185.199.110.153

![](_images/ssl-gh-pages-alert-cname.png)


### gl-pages


> ༄  dig 101.camp +nostats +nocomments +nocmd

    ; <<>> DiG 9.8.3-P1 <<>> 101.camp +nostats +nocomments +nocmd
    ;; global options: +cmd
    ;101.camp.          IN  A
    101.camp.       1799    IN  CNAME   pythonicamp.gitlab.io.
    pythonicamp.gitlab.io.  300 IN  A   35.185.44.232
    gitlab.io.      48445   IN  NS  ns-1116.awsdns-11.org.
    gitlab.io.      48445   IN  NS  ns-926.awsdns-51.net.
    gitlab.io.      48445   IN  NS  ns-1697.awsdns-20.co.uk.
    gitlab.io.      48445   IN  NS  ns-288.awsdns-36.com.
    ns-288.awsdns-36.com.   147125  IN  A   205.251.193.32
    ns-926.awsdns-51.net.   48349   IN  A   205.251.195.158
    ns-1116.awsdns-11.org.  136520  IN  A   205.251.196.92
    ns-1697.awsdns-20.co.uk. 48327  IN  A   205.251.198.161
    ns-288.awsdns-36.com.   136726  IN  AAAA    2600:9000:5301:2000::1
    ns-926.awsdns-51.net.   48349   IN  AAAA    2600:9000:5303:9e00::1
    ns-1116.awsdns-11.org.  136520  IN  AAAA    2600:9000:5304:5c00::1
    ns-1697.awsdns-20.co.uk. 48327  IN  AAAA    2600:9000:5306:a100::1



## summary

- DNSPod 依然是感觉最舒服的 DNS 管理界面, 可惜彻底被放弃了, 能迁走就迁吧...
- gitlab 比 github 要 hardcore 很多
    + 但是, 乐趣也更多也
- 嫑怕嫑怕嫑怕
    + 官方文档, 总是最合理的
    + 一定要安心静静读一遍, 比查找多少中文说明都好用
    + 所以, 俺这篇, 也纯粹是私人 BDD, 包含一些隐坑, 不好意思提了
        * 就渴望您也撞到
        * 好一起呵呵...

## refer

- [如何持证 (HTTPS) 开车 · Yixuan](https://yixuan.li/geek/2019/01/21/howToDriveWithHTTPS/)
    + [GitHub Pages HTTPS 设置 | 查错指南](https://help.github.com/articles/troubleshooting-custom-domains/)
    + [如何给你的 GitHub Pages 加上 HTTPS 证书](https://help.github.com/articles/securing-your-github-pages-site-with-https/)
- [Lets encrypt for gitlab pages · Pages · Project · User · Help · GitLab](https://gitlab.com/help/user/project/pages/lets_encrypt_for_gitlab_pages.md)
    + [rolodato/gitlab-letsencrypt: Easily generate a Let's Encrypt certificate for GitLab Pages](https://github.com/rolodato/gitlab-letsencrypt)
    + [Getting started part three · Pages · Project · User · Help · GitLab](https://gitlab.com/help/user/project/pages/getting_started_part_three.md#dns-records)
    + ...