Title: Mavericks 中用 sshfs
Date: 2014-10-24
Tags: MAC,sshfs
Slug: sshfs-in-mavericks

[TOC]


# 背景

自从 2011-12-16 入手 MBP 以来,就发现只有 sshfs 来连接各种系统的硬盘最方便

- 依赖少, 双方有 ssh 就好
- 配置少, ssh 服务的启动没有 smb 服务那么多的配置
- 自动断, 不会象 smb 死占一个虚假的挂接点

# 问题

每次 brew 出点小问题,就导致 sshfs 或是不痛快;

目测已经折腾过至少4次了

- 送修理两次
- 从 10.6 升级 到 10.9 一次
- brew 在硬盘权限修订后,完全崩溃,重新安装 又一次

# 分析

毕竟 sshfs 依赖 FUSE 这种 plan9 发展来的神物,
是第三方的东西...

而且历史上:

- fuse4x
- macfuse
- osxfuse
- ...

出现过很多靠谱不靠谱的...

# 解决

认真根据 homebrew 上最新 issue 的指引

- 先停了以往各种版本的 `FUSE`
- 正常的安装

```
$ brew install sshfs
```


由脚本自动安装所有依赖包.

并根据安装提示进行必要的系统配置



    sudo /bin/cp -RfX /usr/local/opt/osxfuse/Library/Filesystems/osxfusefs.fs \
        /Library/Filesystems/
    sudo chmod +s /Library/Filesystems/osxfusefs.fs/Support/load_osxfusefs


首次,进行挂接时,会有驱动非官方的警告,知道就好,
其它一切正常的了 ;-)

参考:

- [Montar SSHFS en OS X Mavericks](http://www.jesusherman.com/blog/general/montar-sshfs-en-os-x-mavericks/)
- [Fix to remove or uninstall MacFuse on Mountain Lion when you get the error "MacFUSE Uninstaller: Can not find the Archive.bom for MacFUSE Core package." - Crude Technologies](http://michael.terretta.com/fix-to-remove-or-uninstall-macfuse-on-mountain-lion-when-you-get-the-error-macfuse-uninstaller-can-not-find-the-archive-dot-bom-for-macfuse-core-package-dot)
- [how to remove macfuse and ntfs 3g on osx lion? | Apple Support Communities](https://discussions.apple.com/message/18355704#18355704)
- ... etc.