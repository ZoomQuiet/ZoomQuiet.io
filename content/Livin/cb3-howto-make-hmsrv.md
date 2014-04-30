Title: 如何基于CB3构建家庭服务器
Date: 2014-01-27 23:48
Tags: MAC,CT,Cubier,CubieBoard,Howto
Slug: cb3-howto-make-hmsrv

[TOC]


[CBInstallfest 的体验](http://blog.zoomquiet.io/cbi-zq-install.html)
之后,总是要一步步完成心目中的 家服务器

## Issue

CB3 lununtu-server-VGA

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


### 数据迁移

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




### 外置硬盘盒

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


### 重新外置

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


## 系统硬盘

$ sudo fdisk -l /dev/sda

Disk /dev/sda: 1000.2 GB, 1000204886016 bytes
255 heads, 63 sectors/track, 121601 cylinders, total 1953525168 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disk identifier: 0x00000000

Disk /dev/sda doesn't contain a valid partition table


### fdisk
- [使用fdisk命令对linux硬盘进行操作 - Linux/Unix - 刘苏平的博客](http://www.liusuping.com/ubuntu-linux/linux-fdisk-disk.html)
- [多硬盘分区管理fdisk-张丹-leonarding-ITPUB博客](http://blog.itpub.net/26686207/viewspace-765782/)




### etx4
[linux下的文件系统选型 | shell's home](http://floss.zoomquiet.io/data/20110828225725/index.html)

$ sudo mkfs.ext4 /dev/sda3


### 自动挂接

    zoomq @ cubietruck in /mnt
    $ ll
    total 20
    drwxr-xr-x 2 root root 4096 Jan 27 16:44 bk2wk
    drwxr-xr-x 2 root root 4096 Feb 24 15:26 data
    drwxr-xr-x 2 root root 4096 Jan 27 16:44 dl4p2p
    drwxr-xr-x 4 root root 4096 Jan 11 17:48 nandc
    drwxr-xr-x 2 root root 4096 Feb 24 15:22 sda3

/dev/sdb2 -> bk2wk
/dev/sdb3 -> dl4p2p
/dev/sda3 -> data
/dev/nandc -> nandc

sudo mount /dev/nandc /mnt/nandc
sudo mount /dev/sda3 /mnt/data
sudo mount /dev/sdb2 /mnt/bk2wk
sudo mount /dev/sdb3 /mnt/dl4p2p


#### fatab

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


[Cubieboard 开箱和入门 | Name5566](http://name5566.com/4398.html)
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

[求助，CT如何给nand分区，获得8G空间？ - 上手问题 - Cubieboard中文论坛 - Powered by Discuz!](http://forum.cubietech.com/forum.php?mod=viewthread&tid=1772)

通过nand-part --help查看命令帮助
得到nand-part的使用方法:
nand-part nand设备 起始位置 '分区名称 长度' '分区名称2 长度2'
直接运行nand-part，会得到分区信息
bootloader 起始位置32768 长度131072
rootfs 起始位置163840 长度4194304
UDISK 起始位置4358144 长度10584064

其中这些数字，都是以512字节为单位。
其中rootfs就是系统文件分区，而UDISK就是那5G多，而我们的目的就是把这5G的空间，合并到rootfs中，重新计算了一下，得到的命令就是：

nand-part /dev/nand 32768 'bootloader 131072' 'rootfs 14778368'


意思就是把/dev/nand重新分区，bootloader 的起始位置和长度必须保持不变，不然后果就是重新刷系统吧。
这样的话，rootfs的起始位置也是原来的位置，所要修改的就是它的长度，为14778368。
容量计算一下就是：14778368*512/1024/1024=7216MB，也就是7G，
当然因为前面有bootloader分区，以及bootloader之前空出的一块，所以nandb自然是得不到完整的8G

命令成功执行，reboot，再
resize2fs /dev/nandb

就真的成功了



2 partitions
partition  1: class =         DISK, name =   bootloader, partition start =    32768, partition size =   131072 user_type=0
partition  2: class =         DISK, name =       rootfs, partition start =   163840, partition size = 14778368 user_type=0

write new partition tables? (Y/N)
y
Failed rereading partition table: Device or resource busy

verifying new partition tables:
check partition table copy 0: mbr: version 0xb6fd14fc, magic
magic          is not softw411
check partition table copy 1: mbr: version 0xb6fd14fc, magic
magic          is not softw411
check partition table copy 2: mbr: version 0xb6fd14fc, magic
magic          is not softw411
check partition table copy 3: mbr: version 0xb6fd14fc, magic
magic          is not softw411
all partition tables are bad!
rereading partition table... returned -1

[求救：释放CB2 NAND 剩余空间 - 解决 - 上手问题 - Cubieboard中文论坛 - Powered by Discuz!](http://forum.cubietech.com/forum.php?mod=viewthread&tid=1454&extra=page%3D2)

## 你不能在当前挂载着的分区上扩容的


[Cubieboard - Part 1](http://www.bango29.com/cubieboard-part-1/)
/dev/sda1    /media/ext  ext4    defaults    0   2

/dev/nandc    /mnt/nandc  ext4    defaults    0   2
/mnt/nandc/swapfile    none    swap    sw  0   0
/dev/sda3    /mnt/data  ext4    defaults    0   2
/dev/sdb2    /mnt/bk4wk  exfat    rw,async,umask=0   0   0
/dev/sdb3    /mnt/dl4p2p  exfat    rw,async,umask=0   0   0


$ agi  -y exfat-fuse exfat-utils

/dev/sdb2: LABEL="bk4wk" UUID="52E4-78FF" TYPE="exfat"
/dev/sdb3: LABEL="dl4p2p" UUID="52E4-7901" TYPE="exfat"

/dev/sda1 /media/usbdrive exfat rw,async,umask=0 0 0
/dev/sda1 /home/cubie/sda1 ntfs defaults,utf8,umask=0000,uid=1001,gid=1002,0 0

zoomq:x:1001:1002:Zoom.Quiet:/home/zoomq:/bin/bash

- [Cubieboard自动挂载TF卡fstab设置方法 | OPENERP-从零开始!](http://00-00-00-00.com/2013/08/13/cubieboard%e8%87%aa%e5%8a%a8%e6%8c%82%e8%bd%bdtf%e5%8d%a1fstab%e8%ae%be%e7%bd%ae%e6%96%b9%e6%b3%95/)

### samba
$ agi -y samba

### MAC 共享

#### netatalk->Time Machine
/etc/netatalk/AppleVolumes.default


/mnt/data/timemachine   "TimeCapsule"  options:tm
/mnt/data     "data"
/mnt/bk2wk     "bk2wk"
/mnt/dl4p2p     "dl4p2p"

创建文件 /etc/avahi/services/afpd.service
<service-group>
  <name replace-wildcards="yes">%h</name>
  <service>
    <type>_afpovertcp._tcp</type>
    <port>548</port>
  </service>
  <service>
    <type>_device-info._tcp</type>
    <port>0</port>
    <txt-record>model=Xserve</txt-record>
  </service>
</service-group>

<?xml version="1.0" standalone='no'?><!--*-nxml-*-->
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
    <name replace-wildcards="yes">%h</name>
    <service>
        <type>_afpovertcp._tcp</type>
        <port>548</port>
    </service>
    <service>
        <type>_device-info._tcp</type>
        <port>0</port>
        <txt-record>model=TimeCapsule</txt-record>
    </service>
</service-group>


### 系统整顿
[Ubuntu卸载Apache+Mysql+PHP - 徐航的个人页面 - 开源中国社区](http://my.oschina.net/sherwayne/blog/108685)

 1、卸载Apache2都几个命令

sudo apt-get --purge remove apache2
sudo apt-get --purge remove apache2.2-common

或直接使用一条命令
sudo apt-get autoremove apache2

2、卸载Mysql
sudo aptitude purge mysql-server mysql-server-5.0

sudo apt-get autoremove php5 

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

#### apache2

同理删除 Apache2 这一大恐龙!!!

  $ sudo apt-get --purge remove apache-common
  $ sudo apt-get --purge remove apache
  $ sudo apt-get autoremove



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




### MLDonkey
$ agi -y mldonkey-server


### 家庭影院

### 远程维护

IP



# Changelog

- 140127 单立文章追踪
