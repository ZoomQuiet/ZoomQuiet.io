Title: 修复 subl3 包安装
Date: 2019-04-03 12:12
Tags: MAC,Livin,SCM,subl
Slug: fix-subl-package-installation

[TOC]

## BG

突然: `cmd+shift+P` 选择 `Package Control: install package` 时,一直:

>>> There are no packages available for installation


## goal

当然就是解决呗:

- 各种官方都有吼
- [Troubleshooting \- Package Control](https://packagecontrol.io/docs/troubleshooting)
- [There are no packages available for installation - Package Control of Sublime Text 3 · Issue #959 · wbond/package_control](https://github.com/wbond/package_control/issues/959#issuecomment-168447848)
- ...

## logging

打开 debug 观察:

    Package Control: Skipping automatic upgrade, last run at 2019-04-03 11:45:00, next run at 2019-04-03 12:45:00 or after
    Detected ASCII vs Undefined with 100% confidence
    Package Control: Fetching list of available packages and dependencies
      Platform: osx-x64
      Sublime Text Version: 3200
      Package Control Version: 3.3.0
    Package Control: Download Debug
      URL: https://packagecontrol.io/channel_v3.json
      Timeout: 30
      Resolved IP: 74.207.232.232
      Resolved IPv6: 2600:3c02::f03c:91ff:fec5:4fd5
    Package Control: Urllib Debug Proxy
      http_proxy: 
      https_proxy: 
      proxy_username: 
      proxy_password: 
    Package Control: Found previously exported CA bundle at /Users/zoomq/Library/Application Support/Sublime Text 3/Packages/User/oscrypto-ca-bundle.crt (268761 bytes)
    Package Control: Urllib HTTPS Debug General
      Connecting to packagecontrol.io on port 443
    Package Control: Error downloading channel. URL error [Errno 65] No route to host downloading https://packagecontrol.io/channel_v3.json.

果断就是 `https://packagecontrol.io/channel_v3.json` 资源无法访问;

尝试配置 host 无果;
也升级 `Package Control` 本身;

看来是和谐了? 那么:

- 翻越, 下载
- 发布为 http://101.zoomquiet.top/res/subl/channel_v3.json
- 配置到 `Package Control.sublime-settings`
    + Preferences > Package Settings > Package Control > Settings - User

追加为:

    "channels": [
        "http://101.zoomquiet.top/res/subl/channel_v3.json"
    ],

再来就好了:

    Package Control: Fetching list of available packages and dependencies
      Platform: osx-x64
      Sublime Text Version: 3200
      Package Control Version: 3.3.0
    Package Control: Download Debug
      URL: http://101.zoomquiet.top/res/subl/channel_v3.json
      Timeout: 30
      Resolved IP: 183.236.31.251
    Package Control: Urllib Debug Proxy
      http_proxy: 
      https_proxy: 
      proxy_username: 
      proxy_password: 
    Package Control: Urllib HTTP Debug General
      Connecting to 101.zoomquiet.top on port 80
    Package Control: Urllib HTTP Debug Write
      GET /res/subl/channel_v3.json HTTP/1.1
      User-Agent: Package Control v3.3.0
      Connection: Keep-Alive
      Host: 101.zoomquiet.top
      Accept-Encoding: bzip2,gzip,deflate
    Package Control: Urllib HTTP Debug Read
      HTTP/1.1 200 OK
      Server: marco/2.9
      Date: Wed, 03 Apr 2019 04:34:47 GMT
      Content-Type: application/json
      Transfer-Encoding: chunked
      Connection: keep-alive
      Vary: Accept-Encoding
      X-Source: C/200
      Content-Disposition: inline; filename="channel_v3.json"; filename*=utf-8' 'channel_v3.json
      X-Reqid: JCYAAB2A-KCu3JEV
      Cache-Control: max-age=2592000
      ETag: W/"FupX-eSMnVrkAsAr7E6aNcS8eye6"
      X-Log: redis.g/404;rdb.g/no such key;DBD/404;v4.get/Document not found;rs5_shard.sel:2;rwro.get:3;RS.dbs:3;RS:3;redis.s;2s.gh;PFDS;IO:5
      X-Slice-ETag: FupX-eSMnVrkAsAr7E6aNcS8eye6
      X-Slice-Complete-Length: 3461591
      X-Slice-Size: 1048576
      Content-Transfer-Encoding: binary
      X-Qnm-Cache: Miss
      X-Svr: IO
      Access-Control-Expose-Headers: X-Log, X-Reqid
      Access-Control-Allow-Origin: *
      X-M-Reqid: 1mcAAMfJXKCu3JEV
      X-Qiniu-Zone: 2
      X-M-Log: QNM:xs1163;SRCPROXY:xs485;SRC:31;SRCPROXY:31;QNM3:138
      Last-Modified: Wed, 03 Apr 2019 04:31:53 GMT
      Access-Control-Max-Age: 2592000
      Expires: Fri, 03 May 2019 04:33:06 GMT
      Age: 101
      X-Request-Id: 67a882de6a2b534dd68e3fe0a15c7128; 7f96de58c802da2ccd119a99b08623f6
      Via: S.mix-js-czx2-045, T.46.M, V.mix-js-czx2-049, T.231.H, M.cmn-gd-can-228
      Content-Encoding: gzip
    Package Control: Caching http://101.zoomquiet.top/res/subl/channel_v3.json in /Users/zoomq/Library/Application Support/Sublime Text 3/Packages/User/Package Control.cache/5bd341de6f2ee7d8d6c4aa065520052a
    Package Control: Urllib HTTP Debug General
      Closing connection to 101.zoomquiet.top on port 80 after 1 request



## Sayeahooo
> 所以, 有一个可以随时发布自己资源的外网空间是好的...

- 1.5h 资料搜索理解
- 2d 冷静
- .5h 实施
- .5h 文档嗯哼...


