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

整体上, 无论在哪个 `*-pages` 平台, 要折腾的事儿相似, 就3步:

- 追加配置含 `SSL` 解析能力的 DNS 服务主机 `A` 地址
    + 并解决引发的有关 `CANEM` 冲突问题
- 在 `*-pages` 平台配置 `Enforce HTTPS` 有关嗯哼
- 优雅的等待一切生效 ;-)
    + 并解决可能的资源冲突问题

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

![邮件事务](_images/ssl-domain-transfer-flow.png)


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

修订配置文件 `pelicanconf.py`: 

    SITEURL = 'http://blog.zoomquiet.io'
    -->
            'https://blog.zoomquiet.io'

但是, 进行 push 失败:

    ༄  git pu

    To github.com:ZoomQuiet/ZoomQuiet.github.io.git
     ! [rejected]        master -> master (fetch first)
    error: failed to push some refs to 'git@github.com:ZoomQuiet/ZoomQuiet.github.io.git'
    hint: Updates were rejected because the remote contains work that you do
    hint: not have locally. This is usually caused by another repository pushing
    hint: to the same ref. You may want to first integrate the remote changes
    hint: (e.g., 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.


> 因为仓库目录中 `CNAME` 文件自动构建过,和本地没同步上

![CNAME 重建](_images/ssl-domain-cname-renew.png)

> 再重新编译->push->等待 gh-pages 完成发布

![等待部署](_images/gh-pages-waitting.png)

那个褐色小点, 变成绿色对勾, 就说明一切安好...


![WOLA](_images/ssl-all-ok.png)



### gl-pages
其实, gitlab 上网站先持证上岗的...

先出示一下成果:

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
    ...

#### domain
> 首先操作就撞到神奇形象

![DNSPod 升级?](_images/SSL-dnspod-acord-error.png)

![DNSPod 冲突](_images/SSL-dnspod-cname-error.png)

> 不得以, 迁移回 neamcheap 来配置, 顺畅完成:

![neamcheap 可配](_images/SSL-namecheap-acords.png)

- 当然, 这波配置, 看错文档, 配置成 github 解析主机了
- 但是, 证明 DNSPod 完全不可用了...


#### pages
> 配置证书前, 得先生成, gitlab 不象 github 为用户自动生成, 得自行嗯哼

- 先安装 [Certbot](https://certbot.eff.org/)
- [Let's Encrypt](https://letsencrypt.org/) 官方推出的证书生成工具

> brew install certbot

然后手工给对应域名生成密匙对:

    $ sudo certbot certonly -a manual -d 101.camp --email zoom.quiet@gmail.com

- 注意, 这里 `-d` 参数可以叠加
- 不过, 毎生成一个, 必须同时完成自证检验,才能继续
- 否则, 等于放弃当前生成的密匙

> 即, 蔱根据提示完成:

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    Create a file containing just this data:

    iIpSoAbePD ... 1tTDSskcHQFs

    And make it available on your web server at this URL:

    http://101.camp/.well-known/acme-challenge/iIpSoAbePDhDmGwPUDfER-Czl_bxduu2Cp6qE-IxjLI

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Press Enter to Continue

此时, 千万别按回车:

- 得回到仓库中
- 构建 `.well-known/acme-challenge/iIpSoAbePDhDmGwPUDfER-Czl_bxduu2Cp6qE-IxjLI` 目录
- 并在其中构建 `index.html` 文件
- 文件内容就那一行提供的用来检验的数据
- 当然, 对于 gl-pages 网站
- 只是手工建立目录和文件, 复制进入数据
- 再 `git push` 就好
- 只是, 按回车前, 一定要先
    + 访问那个 URI
    + 看一眼, 是否可以获得对应数据

> 按下回车

    Waiting for verification...
    Cleaning up challenges

    IMPORTANT NOTES:
     - Congratulations! Your certificate and chain have been saved at:
       /etc/letsencrypt/live/101.camp/fullchain.pem
       Your key file has been saved at:
       /etc/letsencrypt/live/101.camp/privkey.pem
       Your cert will expire on 2019-04-23. To obtain a new or tweaked
       version of this certificate in the future, simply run certbot
       again. To non-interactively renew *all* of your certificates, run
       "certbot renew"
     - If you like Certbot, please consider supporting our work by:

       Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
       Donating to EFF:                    https://eff.org/donate-le
       

嗯哼, 好了, 出现以上类似信息

- 说明, 已经在官方注册好并检验通过私人证书了
- 不过, 这种证书只有 4个月 寿命
- 到时得运行 `certbot renew` 一下

接下来正常重新配置一下 gl-pages 中的域名

![gl 强制嗯哼](_images/SSL-gl-pages-ssl.png)

> 打开 HTTPS 开关

![gl 域名上证](_images/SSL-gl-pages-redomain.png)

> 根据提示, 从本地 `letsencrypt` 证书目录中复制出有关嗯哼就好
       

- 当然, 别忘记重新在域名解析商, 配置新的 `TXT` 字串


#### waitting
首先..

![证件无效](_images/SSL-chrome-chk-CA-not.png)

然后可以看到:

![检验通过](_images/SSL-CAX3-ok.png)

接着...

![还未安全](_images/SSL-chrome-chk-CA-ok.png)

最后...

![部分安全](_images/SSL-chrome-chk-info.png)

这是因为有的图片/css/js 资源, 还是用 hhtp 引用的, 得升级:

![iPic](_images/ipic-http.png)

俺采购的工具, 才发现主要图床还是 http 的

追查文档:

![7牛有关页面](_images/SSL-7niu-cdn.png)

> 对比隔壁 ...

![UPYUN 有关页面](_images/SSL-upyun-https.png)

嚓, 这不很明显, 只能选择后者了...

- 当然, 又引发了欠费等等额外处置事务
- 那就是另外的故事了
- 但是, 反正可以先直接用 gl-pages 空间嘛
    + 已经 HHTPS 光辉笼罩下的资源渠道...


![一切安全](_images/SSL-chrome-chk-good.png)

终于...收功


## iPic
> 是的, mac 下 docker 工具中最接地气的了


在和有关人士沟通后, 人工通过了俺单域名免费 SSL 的订单,
然后发现和对应 bucket 的配合是这样的:

- 首先,在 SSL 采购界面中,点击 `补全`

![补全](https://ipic.zoomquiet.top/2019-02-13-%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-02-13%2016.19.48.png)

- 然后才有域名绑定界面出现, 当然的要求先备案

![SSL 配置](https://ipic.zoomquiet.top/2019-02-13-%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-02-13%2016.32.44.png)

- 再回到对应云存储控制界面中, 再次绑定域名
- 最后,参考: [如何进行 HTTPS 配置？ – 又拍云-文档帮助中心](https://help.upyun.com/knowledge-base/cdn-https/)
    + 还得 `服务管理 > 功能配置 > HTTPS`, 点击 `管理` 才能真正打开 HTTPS

![管理](https://ipic.zoomquiet.top/2019-02-13-%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-02-13%2017.17.32.png)

- 这样就完成了隐藏的云端 SSL 密匙部署, 以及空间域名绑定过程
- 是的, 以上3张图片都是 `HTTPS` 持证资源了



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


## Sayeahooo

- 1.5h 资料搜索理解
- 2d gitlab 尝试/生效
- 4h github 嗯哼
    + 3.5h 域名迁移尝试
- 2h 截屏,文档嗯哼...
- 190213 2h 沟通以及尝试
    + iPic 获得一个稳定 HTTPS 入口
