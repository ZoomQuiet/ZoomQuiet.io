Title: 如何基于 CB3 构建家庭服务器
Date: 2014-01-27 23:48
Tags: MAC,CT,Cubier,CubieBoard,Howto
Slug: cb3-howto-make-hmsrv

[TOC]


[CBInstallfest 的体验](http://blog.zoomquiet.io/cbi-zq-install.html)
之后,总是要一步步完成心目中的 家服务器
## Issue

CB3 lununtu-server-VGA

- 预装: 
  - sshd
  - apt-fast
  - vim
  - mc
  - ...

- 不要: 
  - php
  - mysql
  - apache


## TODO

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

## 过程

### 数据迁移

### nand*
$ sudo !!
sudo fdisk -l /dev/nandc

Disk /dev/nandc: 5469 MB, 5469372416 bytes
255 heads, 63 sectors/track, 664 cylinders, total 10682368 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

Disk /dev/nandc doesn't contain a valid partition table


### fdisk
- [使用fdisk命令对linux硬盘进行操作 - Linux/Unix - 刘苏平的博客](http://www.liusuping.com/ubuntu-linux/linux-fdisk-disk.html)
- [多硬盘分区管理fdisk-张丹-leonarding-ITPUB博客](http://blog.itpub.net/26686207/viewspace-765782/)

### 硬盘加挂

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

sudo mount.exfat-fuse /dev/sdb2 /mnt/bk2wk
sudo mount.exfat-fuse /dev/sdb3 /mnt/dl4p2p

但是, 远程 sshfs 后目录只读!?

- 只能用 root 的远程用户登录...
- 最好用 密匙...

[SSH/OpenSSH/Keys - Community Ubuntu Documentation](https://help.ubuntu.com/community/SSH/OpenSSH/Keys)

/etc/ssh/sshd_config contains the following lines, and that they are uncommented;

PubkeyAuthentication yes
RSAAuthentication yes

`Permission denied (publickey)` 


    # chmod go-w ~/
    # chmod 700 ~/.ssh
    # chmod 600 ~/.ssh/authorized_keys



##### gpart

[gpt的悲剧 | A programmer's life](http://blog.sunchangming.com/post/47268338621)



[How to recover lost partition table using Ubuntu Live CD and gpart](http://docs.oseems.com/general/operatingsystem/linux/recover-lost-partition-table)




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



$ sudo fdisk -l /dev/sda

Disk /dev/sda: 1000.2 GB, 1000204886016 bytes
255 heads, 63 sectors/track, 121601 cylinders, total 1953525168 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disk identifier: 0x00000000

Disk /dev/sda doesn't contain a valid partition table




#### exFAT


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





### 系统整顿

#### MySQL
- [Ubuntu下彻底卸载mysql - yjhmily - BlogJava](http://www.blogjava.net/yjhmily/articles/336926.html)
- [ubuntu - Removing MySQL 5.5 Completely - Stack Overflow](http://stackoverflow.com/questions/10853004/removing-mysql-5-5-completely)




$ sudo apt-get remove --purge mysql-server mysql-client mysql-common

(Reading database ... 27889 files and directories currently installed.)
Removing linaro-lamp-server ...
Removing mysql-server ...
Removing mysql-server-5.5 ...
Purging configuration files for mysql-server-5.5 ...
Removing mysql-client-5.5 ...
Removing libdbd-mysql-perl ...
Removing php5-mysql ...
Purging configuration files for php5-mysql ...
Removing libmysqlclient18:armhf ...
Purging configuration files for libmysqlclient18:armhf ...
Removing mysql-common ...
Purging configuration files for mysql-common ...
dpkg: warning: while removing mysql-common, directory '/etc/mysql' not empty so not removed
Processing triggers for man-db ...
Processing triggers for ureadahead ...
Processing triggers for libapache2-mod-php5 ...
 * Reloading web server config
   ...done.
Processing triggers for libc-bin ...
ldconfig deferred processing now taking place
Selecting previously unselected package dmidecode.
(Reading database ... 27705 files and directories currently installed.)
Unpacking dmidecode (from .../dmidecode_2.12-0linaro1_armhf.deb) ...
Processing triggers for man-db ...
Setting up dmidecode (2.12-0linaro1) ...

$ sudo rm -rf /var/lib/mysql

#### UTF8

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


- [Using UTF-8 in Debian](http://fruit.je/utf-8)
- [修改locale - Ubuntu中文](http://wiki.ubuntu.org.cn/%E4%BF%AE%E6%94%B9locale)

$ locale
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_MESSAGES to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
LANG=en_US.UTF-8
LANGUAGE=
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


$ cat /etc/default/locale
LANG=C.UTF-8


$ locale -a
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_MESSAGES to default locale: No such file or directory
locale: Cannot set LC_COLLATE to default locale: No such file or directory
C
C.UTF-8
POSIX
zh_CN.utf8
zh_HK.utf8
zh_SG.utf8
zh_TW.utf8


重启后依然!

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




### 软件安装

### 睡觉维护




## HHD

Disk /dev/sda: 1000.2 GB, 1000204886016 bytes
255 heads, 63 sectors/track, 121601 cylinders, total 1953525168 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disk identifier: 0x00000000

Disk /dev/sda doesn't contain a valid partition table

WARNING: GPT (GUID Partition Table) detected on '/dev/sdb'! The util fdisk doesn't support GPT. Use GNU Parted.


Disk /dev/sdb: 2000.4 GB, 2000398934016 bytes
256 heads, 63 sectors/track, 242251 cylinders, total 3907029168 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1   *           1  3907029167  1953514583+  ee  GPT

$ cat /proc/partitions
major minor  #blocks  name

  93        0    7520256 nand
  93        1      65536 nanda
  93        2    2097152 nandb
  93        3    5341184 nandc
   8        0  976762584 sda
   8       16 1953514584 sdb
   8       17         64 sdb1
   8       18    8388608 sdb2
   8       19 1943011328 sdb3
   8       20    2114547 sdb4


### UFS

[mount external partition - FedoraForum.org](http://forums.fedoraforum.org/showthread.php?t=285255)

$ ll /lib/modules/3.4.61+/kernel/fs/
total 20
drwxrwxr-x 2 1003 1003 4096 Nov 12 12:24 exportfs
drwxrwxr-x 2 1003 1003 4096 Nov 12 12:24 jffs2
drwxrwxr-x 2 1003 1003 4096 Nov 12 12:24 nfsd
drwxrwxr-x 2 1003 1003 4096 Nov 12 12:24 squashfs
drwxrwxr-x 2 1003 1003 4096 Nov 12 12:24 ubifs



#### 外置硬盘盒

$ dmesg |grep umass
umass0: <Norelsys NS1066, class 0/0, rev 2.10/1.00, addr 2> on usbus6
umass0:  SCSI over Bulk-Only; quirks = 0x0100
umass0:6:0:-1: Attached to scbus6
(probe0:umass-sim0:0:0:0): REPORT LUNS. CDB: a0 0 0 0 0 0 0 0 0 10 0 0
(probe0:umass-sim0:0:0:0): CAM status: SCSI Status Error
(probe0:umass-sim0:0:0:0): SCSI status: Check Condition
(probe0:umass-sim0:0:0:0): SCSI sense: ILLEGAL REQUEST asc:20,0 (Invalid command operation code)
da0 at umass-sim0 bus 0 scbus6 target 0 lun 0

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


### SATA


$ dmesg | grep ada
ada0 at ata4 bus 0 scbus2 target 0 lun 0
ada0: <ST3160815AS 3.ADA> ATA-7 SATA 2.x device
ada0: 300.000MB/s transfers (SATA 2.x, UDMA5, PIO 8192bytes)
ada0: 152587MB (312500000 512 byte sectors: 16H 63S/T 16383C)
ada0: Previously was known as ad8
ada1 at ata5 bus 0 scbus3 target 0 lun 0
ada1: <ST2000DL003-9VT166 CC3C> ATA-8 SATA 3.x device
ada1: 300.000MB/s transfers (SATA 2.x, UDMA5, PIO 8192bytes)
ada1: 1907729MB (3907029168 512 byte sectors: 16H 63S/T 16383C)
ada1: Previously was known as ad10
Trying to mount root from ufs:/dev/ada0s1a [rw]...

$ gpart show /dev/ada1
=>        34  3907029101  ada1  GPT  (1.8T)
          34           6        - free -  (3.0k)
          40         128     1  freebsd-boot  (64k)
         168    16777216     2  freebsd-ufs  (8.0G)
    16777384  3886022656     3  freebsd-ufs  (1.8T)
  3902800040     4229094     4  freebsd-swap  (2.0G)
  3907029134           1        - free -  (512B)

$ sudo mount /dev/ada1p3 /mnt/ada1
mount: /dev/ada1p3 : Operation not permitted


BIOS 配置好打开对应的 SATA 接口,
进入系统后:
$ gpart show /dev/ada1
=>        34  3907029101  ada1  GPT  (1.8T)
          34           6        - free -  (3.0k)
          40         128     1  freebsd-boot  (64k)
         168    16777216     2  freebsd-ufs  (8.0G)
    16777384  3886022656     3  freebsd-ufs  (1.8T)
  3902800040     4229094     4  freebsd-swap  (2.0G)
  3907029134           1        - free -  (512B)

$ ls /dev/ada*
/dev/ada0     /dev/ada0s1   /dev/ada0s1a  /dev/ada0s1b  /dev/ada1
/dev/ada1p1   /dev/ada1p2   /dev/ada1p3   /dev/ada1p4

这是系统盘:
$ gpart show /dev/ada0
=>       63  312499937  ada0  MBR  (149G)
         63  312475590     1  freebsd  [active]  (149G)
  312475653      24347        - free -  (11M)

$ sudo mount /dev/ada1p3 /mnt/ada1
mount: /dev/ada1p3 : Operation not permitted

这就不明白了,,,
目测是 UFS 格式也有不同的?!



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
######################################################################## 100.0%
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



### XFS




# Changelog

- 140127 单立文章追踪
