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

触发对应 gh-pages 配置处 `CNAME` 冲突报警

![冲突报警](_images/ssl-gh-pages-alert-cname.png)


删除原先 `blog.zoomquiet.io` 定制域名后, gh-pages 状态恢复:

![暂时默认](_images/ssl-gh-pages-revert-domain.png)


- 然而, 这肯定不是俺要的效果哪...
- 进一步的, 发现, 这是 `DNSPod` 的问题
- namecheap 等等, 其它老厂, 是支持这种 `A` 记录和 `CNAME` 记录指向不同的
- 所以, 回查当初域名服务商:
    + 才发现, 因为抢注的早, 当年支付私人购买 `.io` 的 iwantmyname.com
    + 实在太弱, 根本没有完备的域名配置服务
    + 而且一直以来域名托管年费也比其它大厂贵一倍
    + 说不得, 只能迁移了:


- 先 `unlock`
- 获得 `Transfer Auth Code`
- 再到 namecheap 发起转移工单
- 再回 iwantmyname 同意转移
- 等待生效
- 再将 DNSPod 上对应各种配置, 逐一手工配置回 namecheap 中
- 再对应增补 SSL 依赖的 gh-pages 有关配置:
    + blog 主机 `A` 记录->`185.199.111.153`
    + blog 主机 `CNAME` -> `ZoomQuiet.github.io.`


迁移前:

> ༄  dig zoomquiet.io +nostats +nocomments +nocmd

    ; <<>> DiG 9.8.3-P1 <<>> zoomquiet.io +nostats +nocomments +nocmd
    ;; global options: +cmd
    ;zoomquiet.io.          IN  A
    zoomquiet.io.       600 IN  A   172.105.199.192
    zoomquiet.io.       600 IN  NS  f1g1ns1.dnspod.net.
    zoomquiet.io.       600 IN  NS  f1g1ns2.dnspod.net.
    ...

> 先给銭:

![迁移费用](_images/ssl-domain-transfer-pay.png)

> 再同意...

![同意迁移](_images/ssl-domain-transfer.png)

- 而且人家立即有挽救邮件来问, 为毛走哪....


> namecheap 中进行恢复

![旧解析](_images/ssl-domain-dnspod.png)

> 使用官方模板, 替代 `DNSPod` 代理的...

![解析模板](_images/ssl-domain-dns2namecheap.png)


![生效等待](_images/ssl-domain-waitting.png)

![迁移成功](_images/ssl-domain-in-namecheap.png)


迁移并重置后:

> ༄  dig zoomquiet.io +nostats +nocomments +nocmd

    ; <<>> DiG 9.8.3-P1 <<>> zoomquiet.io +nostats +nocomments +nocmd
    ;; global options: +cmd
    ;zoomquiet.io.          IN  A
    zoomquiet.io.       600 IN  A   172.105.199.192


- 然后, 逐一先将老的 几十条配置, 逐一复制到 namecheap 解析面板中
- 然后, 按照文档要求的,配置好:

![全部OK](_images/ssl-domain-ko.png)


> ༄  dig blog.zoomquiet.io +nostats +nocomments +nocmd

    ; <<>> DiG 9.8.3-P1 <<>> blog.zoomquiet.io +nostats +nocomments +nocmd
    ;; global options: +cmd
    ;blog.zoomquiet.io.     IN  A
    blog.zoomquiet.io.  1799    IN  CNAME   zoomquiet.github.io.
    zoomquiet.github.io.    3600    IN  A   185.199.111.153
    zoomquiet.github.io.    3600    IN  A   185.199.110.153
    zoomquiet.github.io.    3600    IN  A   185.199.109.153
    zoomquiet.github.io.    3600    IN  A   185.199.108.153
    github.io.      698 IN  NS  ns-1622.awsdns-10.co.uk.
    github.io.      698 IN  NS  ns-393.awsdns-49.com.
    github.io.      698 IN  NS  ns-692.awsdns-22.net.
    ...

> 可以看到, 壕 github 全部用 AWS 域名服务来解析的...


![gh 正常](_images/ssl-gh-pages-ko.png)

> 此时 gi-pages 配置已经感知到一切良好


![证书有效](_images/ssl-chrome-info.png)

点击 chrom 域名前的小图标, 可以看到 SSL 已生效

![检验](_images/ssl-chrome-chk.png)

当然, 原先模板中一系列资源指向老 `http` 资源都无法使用了

![资源丢失](_images/ssl-res-load-err.png)



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
    + 而且功能已经落后

![报警](_images/ssl-dnspod-err.png)

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
    + [Using a custom domain with GitHub Pages - User Documentation](https://help.github.com/articles/using-a-custom-domain-with-github-pages/)
        * [Setting up a custom subdomain - User Documentation](https://help.github.com/articles/setting-up-a-custom-subdomain/)
- [Lets encrypt for gitlab pages · Pages · Project · User · Help · GitLab](https://gitlab.com/help/user/project/pages/lets_encrypt_for_gitlab_pages.md)
    + [rolodato/gitlab-letsencrypt: Easily generate a Let's Encrypt certificate for GitLab Pages](https://github.com/rolodato/gitlab-letsencrypt)
    + [Getting started part three · Pages · Project · User · Help · GitLab](https://gitlab.com/help/user/project/pages/getting_started_part_three.md#dns-records)
    + ...
- [How to Transfer a Domain \- Domain Transfers \-Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/9175/83/how-to-transfer-a-domain)
    + [How do I transfer my existing domain to Namecheap? \- Domain Transfers](https://www.namecheap.com/support/knowledgebase/article.aspx/255/83/how-do-i-transfer-my-existing-domain-to-namecheap)
    + [How do I verify that my domain is eligible for transfer? \- Domain Transfers](https://www.namecheap.com/support/knowledgebase/article.aspx/9798/83/how-do-i-verify-that-my-domain-is-eligible-for-transfer)
    + [iwantmyname \| How do I transfer a domain to another re\.\.\.](https://help.iwantmyname.com/customer/portal/articles/184477-how-do-i-transfer-a-domain-to-another-registrar-)
    + [iwantmyname \| Domain Transfer](https://help.iwantmyname.com/customer/portal/topics/83858-domain-transfer)
    + ...