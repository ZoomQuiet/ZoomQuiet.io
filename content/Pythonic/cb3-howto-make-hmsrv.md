Title: 如何基于CB3构建家庭服务器
Date: 2014-01-27 23:48
Tags: MAC,CT,Cubier,CubieBoard,Howto
Slug: cb3-howto-make-hmsrv

[TOC]


[CBInstallfest 的体验](http://blog.zoomquiet.io/cbi-zq-install.html)
之后,总是要一步步完成心目中的 家服务器

# Issue

基于CB3使用 lununtu-server-VGA 操作系统

- 环境:
  + .bashrc
  + .inputrc

- 预装: 
  - sshd
  - apt-fast
    - [Index of /linux/apt-fast](http://www.mattparnell.com/linux/apt-fast/)
  - vim
  - mc
  - ...

- 不要: 
  - php
  - mysql
  - apache


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


## 分析
之前类似的系统在 Ubuntu/FreeBSD 上都折腾过,应该没有什么问题的...

所以,出了各种问题,用了半个月才断断续续的折腾完!

背景:

- 原先家庭服务器是一台兼容PC, FreeBSD8.2, 4G内存,1T硬盘+30G启动盘, 已经死亡
- 目标环境是:
  - CB3
  - 2G 内存
  - 2G 启动盘
  - 1T 近线2吋盘
  - 1T U盘,3吋老盘,恢复数据

# 过程

宏观回顾一下要点:

1. nand 的系统要选择正确,否则 VGA 是支持不能的
1. 不作死不会死,千万别折腾不必要的功能/配置
1. 外挂硬盘以及历史数据,如果当初没有想到有迁移的这天只能辛苦人肉搬
1. yum 越来越靠谱了,但是,还是相信 apt 为好

## CB 初始化

参考: [CBInstallfest 的体验](http://blog.zoomquiet.io/cbi-zq-install.html)
之后,总是要一步步完成心目中的 家服务器

## 系统整顿

CB 自制的 lubuntu 系统,最扯的事儿是:

    居然
    没有
    默认
    安装
    SSH

真心让俺折腾了很久才发现这么奇葩的设计...

然后进行一系列习惯环境的配置, 特别是:

- 第一时间快速 axel 以及 [Apt-fast](http://wiki.ubuntu.org.cn/Apt-fast)
- 习惯的各种 shell 别名:
    
    :::bash
    alias ses='sudo gedit /etc/apt/sources.list'
    alias acs='apt-cache search'
    alias agu='sudo apt-fast update'
    alias agg='sudo apt-fast upgrade'
    alias agi='sudo apt-fast install'
    alias agclean='sudo apt-get clean && sudo apt-get autoclean'
    alias apse='aptitude search'
    alias apsh='sudo aptitude show'
    alias apu='sudo aptitude update'
    alias apg='sudo aptitude safe-upgrade'
    alias api='sudo apt-get install'
    alias aprm='sudo aptitude remove'
    alias apclean='sudo aptitude autoclean'
    alias ppaddkey='sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys'


然后,第一时间杀灭预安装的 Apache,MySQL,PHP

参考:

- [Ubuntu卸载Apache+Mysql+PHP - 徐航的个人页面 - 开源中国社区](http://my.oschina.net/sherwayne/blog/108685)

    :::bash
    $ sudo apt-get --purge remove apache2
    $ sudo apt-get --purge remove apache2.2-common
    $ sudo apt-get autoremove apache2
    $ sudo aptitude purge mysql-server mysql-server-5.0
    $ sudo apt-get autoremove php5 
    $ sudo rm -rf /var/lib/mysql

### UTF8

默认的: 

    :::bash
    $ locale
    LANG=
    LANGUAGE=
    LC_CTYPE="POSIX"
    LC_NUMERIC="POSIX"
    LC_TIME="POSIX"
    LC_COLLATE="POSIX"
    LC_MONETARY="POSIX"
    LC_MESSAGES="POSIX"
    LC_PAPER="POSIX"
    LC_NAME="POSIX"
    LC_ADDRESS="POSIX"
    LC_TELEPHONE="POSIX"
    LC_MEASUREMENT="POSIX"
    LC_IDENTIFICATION="POSIX"
    LC_ALL=

参考:

- [Using UTF-8 in Debian](http://fruit.je/utf-8)
- [修改locale - Ubuntu中文](http://wiki.ubuntu.org.cn/%E4%BF%AE%E6%94%B9locale)


重启后依然!

    :::bash
    zoomq@cubietruck:~$ locale
    LANG=
    LANGUAGE=
    LC_CTYPE="POSIX"
    LC_NUMERIC="POSIX"
    LC_TIME="POSIX"
    LC_COLLATE="POSIX"
    LC_MONETARY="POSIX"
    LC_MESSAGES="POSIX"
    LC_PAPER="POSIX"
    LC_NAME="POSIX"
    LC_ADDRESS="POSIX"
    LC_TELEPHONE="POSIX"
    LC_MEASUREMENT="POSIX"
    LC_IDENTIFICATION="POSIX"
    LC_ALL=


但是,从 screen 中进入时,就已经

    :::bash
    $ locale
    LANG=en_US.UTF-8
    LANGUAGE=en_US:en
    LC_CTYPE="en_US.UTF-8"
    LC_NUMERIC="en_US.UTF-8"
    LC_TIME="en_US.UTF-8"
    LC_COLLATE="en_US.UTF-8"
    LC_MONETARY="en_US.UTF-8"
    LC_MESSAGES="en_US.UTF-8"
    LC_PAPER="en_US.UTF-8"
    LC_NAME="en_US.UTF-8"
    LC_ADDRESS="en_US.UTF-8"
    LC_TELEPHONE="en_US.UTF-8"
    LC_MEASUREMENT="en_US.UTF-8"
    LC_IDENTIFICATION="en_US.UTF-8"
    LC_ALL=


好吧,也算解决,
目测是因为系统默许不加载用户配置,
但是,一般俺只在 Screen 光辉中生存的,所以,不是问题.


## 数据迁移

专门问过高人:

    from:  Zoom.Quiet <zoom.quiet@gmail.com>
    to:  shlug <shlug@googlegroups.com>
    date:  Mon, Jan 20, 2014 at 4:35 PM
    subject:   1Tb 的2.5吋盘给 Ubuntu 用应该选择什么FS?


参考: [linux下的文件系统选型 | shell's home](http://floss.zoomquiet.io/data/20110828225725/index.html)
以及相关的各种文档,

进行了各种尝试,只能说那真是千辛万苦哪:

- 老硬盘不格式化
  - lununtu 直接/USB加挂3吋盘
    - 无法对 UFS 进行读写
    - 无解
- 老硬盘格式化
  - 购买了2吋 1T盘, etx4 格式化,挂好
  - 怎么将老盘的 BSD 文件系统中的数据迁移出来?
    - MAC 挂 UFS ~ 无解
    - Linux 挂 UFS ~ 失败
    - FreeBSD 挂 UFS 
      - 嚓了! 也失败!
      - 这不科学,再换一台BSD ,一下子就成功了!
      - 原来是 BSD 8.2 和 9.1 的系统不同导致...
  - 然后,就变成:
    - MAC 接 1T 的专用U盘(原先用作 TimeMachine 空间的)
    - 再用 sshfs 远程挂上机房的 BSD 主机
    - 人工识别可用数据,逐一复制
- 恢复上线
  - 所有数据在 MAC 专用U盘中了
  - 回家将老盘用外置U盘接上
  - 从 lununtu 中重新分区,格式化为 `vfat` 
    - `这是唯一一个所有系统都良好兼容的文件格式，工具又多` ~ shell909090 曰过
  - 然后,同样的通过网络 用 sshfs 挂上 CB 中的所有硬盘
  - 人工从 MAC 中灌回...

整个 700多G 数据,就这样迁移到了 CB 控制的两个硬盘共 2T 空间中...

### 相关片段


    $ cat /proc/partitions
    major minor  #blocks  name

      93        0    7520256 nand
      93        1      65536 nanda
      93        2    2097152 nandb
      93        3    5341184 nandc
       8        0  976762584 sda
       8       16 1953514584 sdb
       8       17     204800 sdb1
       8       18  781380608 sdb2
       8       19 1171928064 sdb3

    $ sudo mount.exfat-fuse /dev/sdb2 /mnt/bk2wk
    $ sudo mount.exfat-fuse /dev/sdb3 /mnt/dl4p2p

但是, 远程 sshfs 后目录只读!?

- 只能用 root 的远程用户登录...
- 最好用 密匙...
- [SSH/OpenSSH/Keys - Community Ubuntu Documentation](https://help.ubuntu.com/community/SSH/OpenSSH/Keys)


### 外置硬盘盒

    $ dmesg | grep da0
    ada0 at ata4 bus 0 scbus2 target 0 lun 0
    ada0: <ST3160815AS 3.ADA> ATA-7 SATA 2.x device
    ada0: 300.000MB/s transfers (SATA 2.x, UDMA5, PIO 8192bytes)
    ada0: 152587MB (312500000 512 byte sectors: 16H 63S/T 16383C)
    ada0: Previously was known as ad8
    Trying to mount root from ufs:/dev/ada0s1a [rw]...
    da0 at umass-sim0 bus 0 scbus6 target 0 lun 0
    da0: <ATA ST2000DL003-9VT1 CC3C> Fixed Direct Access SCSI-6 device
    da0: 40.000MB/s transfers
    da0: 1907729MB (3907029168 512 byte sectors: 255H 63S/T 243201C)

    $ gpart show /dev/da0
    =>        34  3907029101  da0  GPT  (1.8T)
              34           6       - free -  (3.0k)
              40         128    1  freebsd-boot  (64k)
             168    16777216    2  freebsd-ufs  (8.0G)
        16777384  3886022656    3  freebsd-ufs  (1.8T)
      3902800040     4229094    4  freebsd-swap  (2.0G)
      3907029134           1       - free -  (512B)


### 伟光大的 sshfs


    $ brew link fuse4x
    Linking /usr/local/Cellar/fuse4x/0.9.2... Warning: Could not link fuse4x. Unlinking...

    Error: Could not symlink file: /usr/local/Cellar/fuse4x/0.9.2/lib/pkgconfig/fuse.pc
    Target /usr/local/lib/pkgconfig/fuse.pc already exists. You may need to delete it.
    To force the link and overwrite all other conflicting files, do:
      brew link --overwrite formula_name

    To list all files that would be deleted:
      brew link --overwrite --dry-run formula_name

    zoomq @ MBP111216ZQ in /usr/local/lib
    $ brew link --overwrite fuse4x
    Linking /usr/local/Cellar/fuse4x/0.9.2... 7 symlinks created


    $ brew install osxfuse
    ==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/osxfuse-2.6.2.mavericks.bottle.tar.gz
    ==> Pouring osxfuse-2.6.2.mavericks.bottle.tar.gz
    ==> Caveats
    If upgrading from a previous version of osxfuse, the previous kernel extension
    will need to be unloaded before installing the new version. First, check that
    no FUSE-based file systems are running:

      mount -t osxfusefs

    Unmount all FUSE file systems and then unload the kernel extension:

      sudo kextunload -b com.github.osxfuse.filesystems.osxfusefs

    The new osxfuse file system bundle needs to be installed by the root user:

      sudo /bin/cp -RfX /usr/local/Cellar/osxfuse/2.6.2/Library/Filesystems/osxfusefs.fs /Library/Filesystems
      sudo chmod +s /Library/Filesystems/osxfusefs.fs/Support/load_osxfusefs
    ==> Summary
    🍺  /usr/local/Cellar/osxfuse/2.6.2: 84 files, 5.0M


### exFAT

    $ cat /etc/lsb-release.bk
    DISTRIB_ID=Linaro
    DISTRIB_RELEASE=13.08
    DISTRIB_CODENAME=raring
    DISTRIB_DESCRIPTION="Linaro 13.08"

    $ sudo vi /etc/lsb-release
    DISTRIB_ID=Ubuntu
    DISTRIB_RELEASE=13.04
    DISTRIB_CODENAME=raring
    DISTRIB_DESCRIPTION="Ubuntu 13.04"

    $ sudo apt-add-repository ppa:relan/exfat
    你将向系统添加如下 PPA：
     PPA for the free exFAT file system implementation project: http://code.google.com/p/exfat/
     更多信息： https://launchpad.net/~relan/+archive/exfat
    按回车继续或者 Ctrl+c 取消添加

    gpg: 钥匙环‘/tmp/tmppjaczn/secring.gpg’已建立
    gpg: 钥匙环‘/tmp/tmppjaczn/pubring.gpg’已建立
    gpg: 下载密钥‘A252A784’，从 hkp 服务器 keyserver.ubuntu.com
    gpg: /tmp/tmppjaczn/trustdb.gpg：建立了信任度数据库
    gpg: 密钥 A252A784：公钥“Launchpad Free exFAT file system implementation”已导入
    gpg: 合计被处理的数量：1
    gpg:               已导入：1  (RSA: 1)
    OK


    $ acs exfat
    exfat-fuse - read and write exFAT driver for FUSE
    exfat-utils - utilities to create, check, label and dump exFAT filesystem

    $ agi exfat-fuse

     Working... this may take a while.
    # apt-fast mirror list: Mon Jan 27 16:42:10 UTC 2014
    http://ports.ubuntu.com/ubuntu-ports/pool/universe/f/fuse-exfat/exfat-fuse_1.0.1-1_armhf.deb
     checksum=md5=fcacfbade2df1f97d72ba9912961883f
     out=exfat-fuse_1.0.1-1_armhf.deb
    http://ports.ubuntu.com/ubuntu-ports/pool/universe/e/exfat-utils/exfat-utils_1.0.1-1_armhf.deb
     checksum=md5=ef8bc2e59569645b7140e930e81809f3
     out=exfat-utils_1.0.1-1_armhf.deb
    ...

    下载结果：
    gid   |stat|avg speed  |path/URI
    ======+====+===========+=======================================================
    07028f|OK  |    66KiB/s|/var/cache/apt/archives/apt-fast/exfat-fuse_1.0.1-1_armhf.deb
    e4fa30|OK  |    40KiB/s|/var/cache/apt/archives/apt-fast/exfat-utils_1.0.1-1_armhf.deb

    状态标识：
    (OK)：完成下载。
    正在读取软件包列表... 完成
    正在分析软件包的依赖关系树
    正在读取状态信息... 完成
    将会安装下列额外的软件包：
      exfat-utils
    下列【新】软件包将被安装：
      exfat-fuse exfat-utils
    升级了 0 个软件包，新安装了 2 个软件包，要卸载 0 个软件包，有 1 个软件包未被升级。
    需要下载 0 B/80.7 kB 的软件包。
    解压缩后会消耗掉 248 kB 的额外空间。
    您希望继续执行吗？[Y/n]
    【警告】：下列软件包不能通过验证！
      exfat-fuse exfat-utils
    忽略了认证警告。
    Selecting previously unselected package exfat-fuse.
    (正在读取数据库 ... 系统当前共安装有 27896 个文件和目录。)
    正在解压缩 exfat-fuse (从 .../exfat-fuse_1.0.1-1_armhf.deb) ...
    Selecting previously unselected package exfat-utils.
    正在解压缩 exfat-utils (从 .../exfat-utils_1.0.1-1_armhf.deb) ...
    正在处理用于 man-db 的触发器...
    正在设置 exfat-fuse (1.0.1-1) ...
    正在设置 exfat-utils (1.0.1-1) ...


    $ sudo fdisk -l /dev/sdb

    WARNING: GPT (GUID Partition Table) detected on '/dev/sdb'! The util fdisk doesn't support GPT. Use GNU Parted.


    Disk /dev/sdb: 2000.4 GB, 2000398934016 bytes
    255 heads, 63 sectors/track, 243201 cylinders, total 3907029168 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x00000000

       Device Boot      Start         End      Blocks   Id  System
    /dev/sdb1               1      409639      204819+  ee  GPT
    /dev/sdb2          411648  1563172863   781380608    7  HPFS/NTFS/exFAT
    /dev/sdb3      1563172864  3907028991  1171928064    7  HPFS/NTFS/exFAT


### 系统硬盘

观察:


    $ sudo fdisk -l /dev/sda

    Disk /dev/sda: 1000.2 GB, 1000204886016 bytes
    255 heads, 63 sectors/track, 121601 cylinders, total 1953525168 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 4096 bytes
    I/O size (minimum/optimal): 4096 bytes / 4096 bytes
    Disk identifier: 0x00000000

    Disk /dev/sda doesn't contain a valid partition table


参考:

- [使用fdisk命令对linux硬盘进行操作 - Linux/Unix - 刘苏平的博客](http://www.liusuping.com/ubuntu-linux/linux-fdisk-disk.html)
- [多硬盘分区管理fdisk-张丹-leonarding-ITPUB博客](http://blog.itpub.net/26686207/viewspace-765782/)


格式化:

    $ sudo mkfs.ext4 /dev/sda3


#### fatab

观察:

    $ cat /proc/partitions
    major minor  #blocks  name

      93        0    7520256 nand
      93        1      65536 nanda
      93        2    2097152 nandb
      93        3    5341184 nandc
       8        0  976762584 sda
       8        1    8388608 sda1
       8        2    2097152 sda2
       8        3  966275800 sda3
       8       16 1953514584 sdb
       8       17     204800 sdb1
       8       18  781380608 sdb2
       8       19 1171928064 sdb3

    $ sudo blkid
    /dev/nanda: SEC_TYPE="msdos" LABEL="Volumn" TYPE="vfat"
    /dev/nandb: UUID="d20c81fd-3188-4650-b124-2fa090bb7920" TYPE="ext4"
    /dev/nandc: UUID="1914bbf8-2641-4b3f-a00e-4afa65d0ed8f" TYPE="ext4"

    /dev/sda3: UUID="b9db3117-90d7-48a6-8302-0b316b9745fd" TYPE="ext4"
    /dev/sdb1: LABEL="EFI" UUID="67E3-17ED" TYPE="vfat"
    /dev/sdb2: LABEL="bk4wk" UUID="52E4-78FF" TYPE="exfat"
    /dev/sdb3: LABEL="dl4p2p" UUID="52E4-7901" TYPE="exfat"


参考:

- [Cubieboard 开箱和入门 | Name5566](http://name5566.com/4398.html)
- [Cubieboard - Part 1](http://www.bango29.com/cubieboard-part-1/)

配置:

    /dev/sda1    /media/ext  ext4    defaults    0   2
    /dev/nandc    /mnt/nandc  ext4    defaults    0   2
    /mnt/nandc/swapfile    none    swap    sw  0   0
    /dev/sda3    /mnt/data  ext4    defaults    0   2
    /dev/sdb2    /mnt/bk4wk  exfat    rw,async,umask=0   0   0
    /dev/sdb3    /mnt/dl4p2p  exfat    rw,async,umask=0   0   0



#### 你不能在当前挂载着的分区上扩容的
~ `NoZuoNoDieWhyUtry`

- [求助，CT如何给nand分区，获得8G空间？ - 上手问题 - Cubieboard中文论坛 - Powered by Discuz!](http://forum.cubietech.com/forum.php?mod=viewthread&tid=1772)
- [求救：释放CB2 NAND 剩余空间 - 解决 - 上手问题 - Cubieboard中文论坛 - Powered by Discuz!](http://forum.cubietech.com/forum.php?mod=viewthread&tid=1454&extra=page%3D2)

    $ sudo nand-part -f a20 /dev/nand
    check partition table copy 0: mbr: version 0x00000200, magic softw411
    OK
    check partition table copy 1: mbr: version 0x00000200, magic softw411
    BAD!
    check partition table copy 2: mbr: version 0x00000200, magic softw411
    BAD!
    check partition table copy 3: mbr: version 0x00000200, magic softw411
    BAD!
    mbr: version 0x00000200, magic softw411
    3 partitions
    partition  1: class =         DISK, name =   bootloader, partition start =    32768, partition size =   131072 user_type=0
    partition  2: class =         DISK, name =       rootfs, partition start =   163840, partition size =  4194304 user_type=0
    partition  3: class =         DISK, name =        UDISK, partition start =  4358144, partition size = 10584064 user_type=0

等等吧,俺折腾完, CB 变码头了,才见到标题那句话!

才明确,想扩展内置OS 空间,要先从 SD 系统重启...所以,就算了吧...


- [Cubieboard自动挂载TF卡fstab设置方法 | OPENERP-从零开始!](http://00-00-00-00.com/2013/08/13/cubieboard%e8%87%aa%e5%8a%a8%e6%8c%82%e8%bd%bdtf%e5%8d%a1fstab%e8%ae%be%e7%bd%ae%e6%96%b9%e6%b3%95/)


## 家庭影院

就几点功能:

- 自动下载
- 远程加载
- 远程播放

### MLDonkey

安装:

    $ agi -y mldonkey-server

就没有然后了,
启动,远程用网页控制就好,
唯一要注意的是怎么提升内网的 edonkey 为 `HIGH IP`

### samba

这是标准的跨平台文件分享服务了:

安装:

    $ agi -y samba

配置也非常直接..


### MiniDLNA

还没有折腾...

# Changelog

- 140505 快速完结
- 140127 单立文章追踪
