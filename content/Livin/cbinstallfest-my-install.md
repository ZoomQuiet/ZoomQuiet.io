Title: CBInstallfest 的体验
Date: 2014-01-11
Tags: MAC,CT,Cubier,CubieBoard,ZQ
Slug: cbi-zq-install

[TOC]

## CBI 
[CBInstall.1 欢乐完成](http://blog.zhgdg.org/2014-01/et-cbi1/)
记要了现场活动的情况;

当然,俺也是学员之一,要交作业的,所以,俺的刷机笔记如下:

## 目标
用CB3 替代原先的兼容 PC 机作家庭服务器!

## 环境

- MBP 11年下半年版, 15吋
- MAC OS X 10.9 Mavericks
- CB3(CubieTruck) 以及套件的配件

## 刷机

果然如宣传的,是那么简单!

1. 准备工具 ~ [LiveSuit](http://docs.cubieboard.org/tutorials/common/livesuit_installation_guide) 
1. 下载镜像 ~ [NAND镜像](http://dl.cubieboard.org/software)
1. 刷机

尝试了 arch linux 的镜像,发觉进入后包管理命令,完全不熟悉,所以,只好坚持使用 Ubuntu了.

### 细节

- [LiveSuit](http://docs.cubieboard.org/tutorials/common/livesuit_installation_guide) 真心傻瓜,在MAC 上完全无碍!

![livesuit_mac](http://zoomq.qiniudn.com/ZHGDG/2014/140111-CBInstallfest.1/livesuit_mac.png)

- 下载时,为了大家的幸福,不要下载 .img 的文件,下载压缩的 .gz 文档本地解开就好

    $ 7z x lubuntu-server-nand.img.gz

- 为了防止手指意外的摸到带电元件,应该先将赠送的PV板安装上,注意:
![cubietruck_fel_button](http://dyhr.com/wp-content/uploads/Cubietruck_FEL_button-300x224.jpg)
    - 正确的次序
    - 以及要将板上的保护膜清除
    - 另外,应该用 CB 驱动激光雕刻仪,来给每个PV 板刻上 CB小猴纸的 logo ,建议已经严正向 Benn 吼过了

- 刷机时, `FEL` 键-USB线-电脑的先后顺序:

    1. 电脑里先运行 LiveSuit 并加载目标NAND 镜像
    1. 按住`FEL` 键,不松,然后插入USB线
    1. 再将 USB线插入电脑
    1. 然后松开 `FEL` 键
    1. LiveSuit 识别外部 CB 板,开始请求确认,准备好开始刷机了

- 刷机一般5分钟以内就可以完成:
    - LiveSute 进度 100% 提示已经完成
    - CB 板上的几个 LED 灯开始闪动
    - 这时,可以长按板上的 `POWER ON` 键,进行热关闭
    - 等板上的灯都更灭时,代表 CB 已经加载的系统完全终止运行
    - 这时就可以拔下 USB 线了
    - 再将 CB 的电源插入,刷好的系统就真正自举运行起来了!

- 首次启动系统时, Ubuntu 会尝试获得当前的网络IP, 而且过期时间定为60秒,我们就只能安静的等哈等! 
    - 这绝对是应该优化的默认配置.


![ct_default_py.png（PNG 图像，814x201 像素）](http://zoomq.qiniudn.com/ZHGDG/2014/140111-CBInstallfest.1/ct_default_py.png)

- 默认安装了Python 点赞!

## 问题

1. 对于可以通过内核接口,调整板上 LED 灯的事儿
    - 这么有趣,为毛不给出对应的文档?

2. 两次都上了 Nand 镜像文件名的当! 比如: 

    :::text
    http://dl.cubieboard.org/software/a20-cubietruck/lubuntu/ \
    ct-lubuntu-nand-v1.01/ct-lubuntu-server/lubuntu-server-nand.img.gz
    ct-lubuntu-nand-v1.00/ct-lubuntu-server-20131026/lubuntu-server-nand.img.gz
    ct-lubuntu-nand-v1.00/VGA/lubuntu-server-nand.img.gz
    
从下载路径的确可以看出是针对什么的镜像;
但是,无论哪种版本的镜像, lubuntu 的下载下来
都是 `lubuntu-server-nand.img.gz`
解压缩 也都是 `lubuntu-server-nand.img`
根本就看不出什么是什么了!
强烈建议,重新制定版本规范,也包含最终下载文件名;比如:

    ct-lubuntu-13.06-server-nand.img.gz
    ct-vga-lubuntu-13.06-server-nand.img.gz


### VGA

是的,兴冲冲,回家准备接上网络,开始家庭服务器的配置!
结果发现,5年前的液瞐屏幕接上没有反应!
再扛来老婆的新液瞐屏也是只有间或的白色闪线,没有信号输出!

这就要了亲命! 

- 命令行上加载驱动,启动wifi 接入家庭无线网络,不是不行,只是没必要,因为以后的正当运行环境是拉网线的
- 然而,网络和能接 HDMI 的液瞐电视不是一房,没办法现拉根网线去

所以,果断 google 之!
果然,是常见问题! 居然 VGA 的输出是需要特殊系统镜像的!

这也才发现, CB3 的 VGA 支持系统镜像,居然只有在 `lubuntu-nand-v1.00` 中有,
`lubuntu-nand-v1.01` 中还没有完成兼容!

重新刷上对口的 OS, 这下子终于见到熟悉的命令行界面了!!!

但是:

    :::text
    Welcome to Linaro 13.08 (GNU/Linux 3.4.61+ armv7l)

     * Documentation:  https://wiki.linaro.org/
    New release '13.10' available.
    Run 'do-release-upgrade' to upgrade to it.

这倒底是升级呢? 还是不升级呢?!

### IP

修订: `/etc/network/interfaces` 为:
    
    :::bash
    auto lo eth0
    iface lo inet loopback
    #iface eth0 inet dhcp
    iface eth0 inet static

    address 192.168.0.111
    gateway 192.168.0.1
    netmask 255.255.255.0
    network 192.168.0.0
    broadcast 192.168.0.255

重启网络:

    :::bash
    /etc/init.d/networking restart

就将原先每次重启时,可能变化的动态 IP 变成内网的静态 IP 了

### Connection refused

然后,配置了 `sudo` 用户,刷了初始口令,就可以离开 VGA 远程随时随地进行控制了!

可是竟然反馈说: `Connection refused`

果断 Google 发布,是常见问题!

[openssh - How to solve 'Connection refused' errors in SSH connection? - Ask Ubuntu](http://askubuntu.com/questions/30080/how-to-solve-connection-refused-errors-in-ssh-connection)

完全无法相信自个儿的眼睛! 竟然是因为根本没有 `sshd` 进程运行的原因!

    :::bash
    sudo apt-get install openssh-server openssh-client
    sudo /etc/init.d/ssh start

再尝试

    $ ssh 192.168.0.111


一切正常了!



### ftab

看CB3 的硬件参数,应该有8G 内置空间的, 但是查询:

    :::shell
    $ df -h
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/root       2.0G 1019M  907M  53% /
    devtmpfs        913M  4.0K  913M   1% /dev
    none            4.0K     0  4.0K   0% /sys/fs/cgroup
    none            183M  160K  183M   1% /run
    none            5.0M     0  5.0M   0% /run/lock
    none            913M     0  913M   0% /run/shm
    none            100M     0  100M   0% /run/user

不对哪,肿么只有2G 的空间?
    
    :::shell
    $ sudo fdisk -l

    Disk /dev/nand: 7700 MB, 7700742144 bytes
    255 heads, 63 sectors/track, 936 cylinders, total 15040512 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x00000000

    Disk /dev/nand doesn't contain a valid partition table

    Disk /dev/nanda: 67 MB, 67108864 bytes
    255 heads, 63 sectors/track, 8 cylinders, total 131072 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x00000000

         Device Boot      Start         End      Blocks   Id  System

    Disk /dev/nandb: 2147 MB, 2147483648 bytes
    255 heads, 63 sectors/track, 261 cylinders, total 4194304 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x00000000

    Disk /dev/nandb doesn't contain a valid partition table

    Disk /dev/nandc: 5469 MB, 5469372416 bytes
    255 heads, 63 sectors/track, 664 cylinders, total 10682368 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x00000000

    Disk /dev/nandc doesn't contain a valid partition table


果然有 `/dev/nandc` 没有挂上;

于是,先建立文件系统:

    :::text
    mkfs.ext4 /dev/nandc
    mke2fs 1.42.5 (29-Jul-2012)
    Filesystem label=
    OS type: Linux
    Block size=4096 (log=2)
    Fragment size=4096 (log=2)
    ...

    Allocating group tables: done
    Writing inode tables: done
    Creating journal (32768 blocks):
    done
    Writing superblocks and filesystem accounting information: done

然后,不折腾,直接使用: `/etc/rc.local`

    sudo mount /dev/nandc /mnt/nandc

追加一行,完成! 这样重启时,将在最后一刻重新挂接上丢失的分区

### 其它

习惯性的安装 `htop` 一看:

![ct_default_deamon.png（PNG 图像，1005x709 像素）](http://zoomq.qiniudn.com/ZHGDG/2014/140111-CBInstallfest.1/ct_default_deamon.png)

目测, 这一镜像的程序猿是 `LAMP` 标准屌丝web 程序猿哪!!!

按惯例, `server` 版的发行系统镜像,应该是最小运维依赖核心系统:

- 有最稳定的 内核
- 包含最常见的系统工具
- 包含最常见的硬件驱动
- 默认启动 `sshd`
- 默认配置好 `apt-fast` ~ 用 axel 来加速 apt-get 软件安装
- ..etc. 总之是面向 SA 的一个方便环境

怎么也没有想到,默认是启动跑了 `MySQL`+`Apache` 这两种一般 SA 一见就删除的东西

有点 `细思恐极` CB 应该及时提升自个儿 SA 的运营观念了,不能停留在上世纪了呢...

# TODO

为了完全替代俺家原先的家庭服务器,可以支持多系统的内网络使用,
还要折腾的事儿有:

1. 通过 USB 挂接 FreeBSD 格式化的 UFS 分区
1. 通过板载 SATA 接口,加装 2.5吋 1T 新硬盘
1. 安装 Samba 系统,提供空间给其它 M$ 设备使用
1. 安装 netatalk ,支持 `Apple Time Machine`
1. 安装 MLDonkey 通过网页控制 `P2P` 下载
1. 安装 MiniDLNA 发布家庭媒体服务,支持远程播放下载的电影

...

总之,要搾干 CB 的一切潜能!




# 参考:
[How to install Lubuntu Server on Cubietruck from Mac OS X](http://dyhr.com/2013/11/22/how-to-install-lubuntu-server-on-cubietruck-from-mac-os-x/)

## CbuieBoard
  [Cubieboard ：享誉国外 Linux 圈子的中国产品- 爱范儿· Beats of Bits](http://www.ifanr.com/367898)
- [Cubieboard/zh cn - linux-sunxi.org](http://linux-sunxi.org/Cubieboard/zh_cn)

- [Cubieboard3: Cubietruck is all ready](http://cubieboard.org/2013/10/30/cubieboard3-cubietruck-is-all-ready/) (cubieboard.org)
- [Tutorials for Cubietruck](http://docs.cubieboard.org/tutorials/cb3/start) (cubieboard.org)
- [FAQ](http://docs.cubieboard.org/faq/faqs) (cubieboard.org)

## Linux
- [LiveSuit Guide](http://docs.cubieboard.org/tutorials/common/livesuit_installation_guide)  (cubieboard.org)
- [www.lubuntu.net](http://www.lubuntu.net/)
- [InstallingANewHardDrive](https://help.ubuntu.com/community/InstallingANewHardDrive?action=fullsearch&value=linkto%3A%22InstallingANewHardDrive%22&context=180)
- [Cubieboard | Arch Linux ARM](http://archlinuxarm.org/platforms/armv7/allwinner/cubieboard)
- [Cubieboard 2 | Arch Linux ARM](http://archlinuxarm.org/platforms/armv7/allwinner/cubieboard-2)



# Changelog

- 140119 终于汇集了所有唠叨!
- 140111 开始总结
