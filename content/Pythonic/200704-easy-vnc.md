Title: VNC回归轻松
Slug: 200704-easy-vnc
Date: 2020-07-04 19:42
Summary: SCM/ 跨平台桌面控制最纯粹和轻松的协议桟还是原生的好...
Tags: DAMA,SCM,VNC,Linux,macOS
Author: ZoomQuiet
Status: published


[TOC]


## BG.
很早就有这种需求:

比如当年参与开发浏览器时,
对应工程是 windows only 的,
而俺的笔记本是 macOS,
所以, 必须有个方便的远程控制工具,将 PB 上的桌面变成本地一个窗口,
并能无缝进行切换控制.

当年用 vnc server 的 windows 版本.

后来创业时, 要确保客户端同时可以安定运行在 win7 以及 linux 上,
更加需要一个通用的全平台桌面控制工具.

当时用的是 TeamViewer :

- 商业软件
- 非常稳定
- 功能良好

问题是, 对于私人商用非常敏感,
用的时间长点儿, 就判定为非法商用直接断掉了.

## problems

然后, 也尝试过各种其它通用类 VNC 工具:

- X2Go 安装失败
- TigerVNC/UltraVNC/RDP/... 不兼容
- NoMachine NX ~ 唉嘛开始还好, 真正一用各种 diss, 而且无法删除
- 还有国产的什么太阳花桌面 ~ 根本无用


只能切换到 RealVNC, 也是商用, 但是, 印象不错;

- 好容易按照官方文档在 mac/ubuntu 间配置好
- 也用了一段时间
- 没想到, 一次系统升级后无论怎么折腾
    + 远程进入后都是黑屏
    + 无法进入 GNOME 桌面.



## asking
> 搜索才发现, 这是常见问题...

尝试了一堆方法都没办法解决, 那个糟心哪...

想想, 用 RealVNC 其实和 TeamViewer 没什么区别:

- 每次连接主机, 都要先去人家官网绕一圈
- 注册一台主机, 而且免费有限额,只能5台
- 真正连接自己本地局域网旁边一台机器时
- 其实, 无论客户端/服务端 都要连接官网检验是否合法
- 而且, 在使用过程中, 俺的所有操作也一定有对应监察数据上报..

也就是说, 俺用俺自己的主机, 就得向厂商老实汇报思想, 否则断你没商量.

俺为什么要这么贱?


## fixed
> 回归 FLOSS 社区内置方案吧...

安装标准 vnc 服务:

    $ sudo apt install vnc4server xfce4 xfce4-goodies

配置访问口令:

    $ vncpasswd

指定启动桌面 ~/.vnc/xstartup :

    #!/bin/bash
    startxfce4 &

并启用配置:

    $ chmod +x ~/.vnc/xstartup

启动服务:

    $ vnc4server

检验状态:

    $ ss -ltn
    ...
    LISTEN      0      5            *:5901                     *:* 

> 注意: 如果有防火墙的话, 要打开 5901 的访问

macOS 本地代理端口:

    ༄  ssh -L 5901:127.0.0.1:5901 -C -N -l <主机用户> <主机IP>

(也就是将 Linux 主机上的 :5901 用 SSH 工具映射为本地 :5901)

![连接](http://ydlj.zoomquiet.top/ipic/2020-07-25-ScreenShot%202020-07-25%2010.37.01.jpg)

使用本地端口:

    vnc://localhost:5901


**Bazinga**

![win7vbox](http://ydlj.zoomquiet.top/ipic/2020-07-25-ScreenShot%202020-07-25%2010.39.36.jpg)


- Ubuntu 中安装 vncserver 以及 xfce4 桌面
- Ubuntu 中启动 vncserver
- macOS 中用 SSH 反向代理对应端口
- 用 macOS 内置远程桌面工具直连进入 Ubuntu 桌面
    + 安装 VirtualBOX 
    + 加载 win7 镜像
    + 同时自由使用 windiws 环境以及 linux 工具


而且速度比之前各种 VNC 工具要快, 充分发挥了本地网络能力.


## refer.

- [VNC server on Ubuntu 18.04 Bionic Beaver Linux - LinuxConfig.org](https://linuxconfig.org/vnc-server-on-ubuntu-18-04-bionic-beaver-linux)
- [VNC from Mac to Linux – Computer Action Team](https://cat.pdx.edu/platforms/mac/remote-access/vnc-to-linux/)
- [Install VNC on Ubuntu 18.04 | Linode](https://www.linode.com/docs/applications/remote-desktop/install-vnc-on-ubuntu-18-04/)
- [How do I set up VNC with Mac OSX? | Linode Questions](https://www.linode.com/community/questions/18877/how-do-i-set-up-vnc-with-mac-osx)
- [How to Install and Configure VNC on Ubuntu 14.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-14-04)
- ...


## logging

- 200725 zoomquiet pub
- 200704 zoomquiet 解决
- 200626 zoomquiet init.

