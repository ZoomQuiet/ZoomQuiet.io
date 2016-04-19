Title: 如何在 Leo 中协作?!
Date: 2016-04-17
Tags: EKR,Leo,pythonic
Slug: how2collaborate-with-leo

[TOC]

# Leo?
~ 嗯哼

研究什么是 Leo ? 非要一句话说清查的话,只能是:

- `纯 Python 构建的文学化编辑环境`
    + 好吧, 那什么是 `文学化编辑` ?
    + 这事儿, 俺就没办法说清楚了....
    + 根据俺一向的宣称: `教不会别人的,一定也是自己并不真正理解的`
- 这点,俺认!
    + 参考: [LeoEnvironment - Woodpecker Wiki for CPUG](http://wiki.woodpecker.org.cn/moin/LeoEnvironment)
    + 以及 [ZqStudy/MyLearningSkill - Woodpecker Wiki for CPUG](http://wiki.woodpecker.org.cn/moin/ZqStudy/MyLearningSkill#Leo)
- 就知道, 俺从 05 年上了船...就一直反复的四处宣传 Leo 的舒爽...
    + 可惜,一直就没有找到一个真正 `直指人心` 的 文学化编辑/程 的描述姿势


好吧,再次尝试一下:

## Literate Programming
~ [文学编程](http://wiki.woodpecker.org.cn/moin/LiterateProgramming)

先请出 [Leo](http://leoeditor.com/leo_toc.html) 创始人 令德华([Edward K. Ream](http://leoeditor.com/ekr.html)) 

~ 老令公 在 PyCon2013China 大会上分享的视频 [PyConChina2013-EKR-intro-Leo](http://zoomq.qiniudn.com/pychina/PyCon2013China/PyConChina2013-EKR-final-v2.mp4)

不那么简单的说就是:

- 文学化编程, 超脱具体编程语言的语法规定
- 以人的思维结构为记述形式, 进行好象文学创作一样的编程!
- 其具体现实:
    + 利用类似 `<<此处有惊喜>>` 的结构标注符
    + 在源代码中,替代各种级别的代码块
    + 将程序的编写和源文件的储存格式分离了
        * 在代码撰写界面中,面对的是完全个性化的抽象结构描述
        * 同时,又可以随时进入自定逻辑区间内, 填充标准语法的源代码
        * 最后,自动将所有 结构标注符 在输出的源文件中展开
    + 这样,同时兼顾了人的自然思维表述,和严格语法要求的源代码形式 
- 是的, 这一思想源自 ![Donald E. Knuth](http://www-cs-faculty.stanford.edu/~knuth/chop.gif), 他原创的 WEB 语言最早实现了 文学化编程
- Leo 则是 Python 实现的,可能是最易用的 文学化编辑/程 环境!


![Leo4](http://leoeditor.com/_static/Leo4-80-border.jpg)


## collaborate problem
~ 如果前述解释看不懂,那就对了!

但是,不影响,俺的故事分享...

Leo 包含的编程思想这么 bigger ,一般人在 IDE 环境中,当然是无法理解,
也没有动力尝试的...
所以, 早在 2013 年, Leo 列表中, EKR 就有相应思考

    from:   Edward K. Ream <edreamleo@gmail.com>
    reply-to:   leo-editor@googlegroups.com
    to: leo-editor@googlegroups.com
    date:   Thu, Oct 24, 2013 at 5:33 PM
    subject:    How to collaborate using Leo

为了讨论时,更加友好,老令公 创造了两个人事

- 能享受文学化编程的 Leo 用户 称为 Leonine (L Leo users, Leonard ...)
- 还没有理解 Leo 的其它程序猿 称为 Nancy (N non-Leo users)

当时,大家一致的共识:

- 为了 Leo 良好工作, 最终源代码中包含的 结构注释(Sentinels) 是必须的
- 但是, 对于 Nancy 而言 Sentinels 是无意义的混乱字符
- 所以,若要 Leonine 们能和 Nancy 们愉快的一起工作,必须解决这一矛盾!

三年前,俺提议的是:

- 利用类似 hg/git 仓库的 hooks 机制
- 在提交仓库前,通过 hooks 脚本,自动的完成 L->N 两型代码的互转化
- 确保, Leonine 们在 Leo 中,有正确的团队代码,以及自己的结构记述
- 同时, Nancy 们永远不知道 Leo 的存在!

问题在:

- 版本管理系统很多,每种都有自个儿的 hooks 机制
- 要想真正实用化这种自动机制, Leo 社区要维护越来越多的 hooks 脚本
- 同时,还得想办法减少每次进行个团队仓库时的配置工作
- 嗯哼,想想都是越来越多的任务...
- 所以,当年 老令公 曰:
    + 此法妙
    + 然俺无空
    + 谁想上,谁上...

PS:
所谓 `结构注释` 其实就是标准注释,类似:

    #@+<<imports>>
    #@+node:zoomq.20160416174346.3: ** <<imports>>
    #@+others
    #@+node:zoomq.20160416174346.4: *3* in-build
    #@+node:zoomq.20160416174346.5: *3* 3party

虽然吻合对应语言的注释约定 (嗯哼, Leo 可以进行任何语言的编程,不仅仅是 Py);
其实,就是将 Leo (.leo 文件本身其实就是 xml) 中,树形节点的结构描述,
转化为线性注释而已.


## terror story
~ 于是, 发生了这样的恐怖故事...

之前,俺知道 Leo 中有种 `@shadow` 指令

- 在 Leo 中,标注在文件节点名前
- 形如: `@shadow path/2/foo.py`
- 进行保存时,将自动作以下操作:
    + 在 `path/2/` 中建立 `path/2/.leo_shadow` 隐藏目录
    + 在其中输出 `path/2/.leo_shadow/xfoo.py` 包含 `结构注释` 的源代码文件
    + 同时输出 `path/2/foo.py` 干净的,不包含 `结构注释` 的源代码文件
- 这样,通过 git 工具提交到团队仓库时
    + Leonine 通过 `.leo_shadow` 中的文件确保 Leo 中结构树的可用
    + Nancy 们继续用 IDE 环境维护自然的干净的只有语法结构而没有思维结构的源代码文件

所以,在团队代码仓库中,俺自信的将 .leo 文件也放了进来,
并对管理的所有代码节点, 前缀了`@shadow`

某天, 快乐的部署了 `git-flow` 然后,基于 `hotfix` 流程,进行每天的开发...

杯具就这样种下了:

- 在俺完成了全天的开发,高兴的将上千行代码 `git flow hotfix finish` 提交时
- 顺利的话应该是:
    + 自动合并 `hotfix/我的修订` 到 `develop` 以及 `master` 分支
    + 然后杀掉 `hotfix/我的修订` 分支
    + 最后,人工切换到 `master` 分支, `git push` 就好
- 残念的是:
    + git 无法自动合并,
    + 因为 .leo 文件在几个分支中差异冲突!
- 好吧, 这是必然的,,,虽然没有人修订 .leo 文件,但是,为了尝试各种代码
    + 过程中,进行了大量的节点调整
    + 另外, Leo 文件是无法共同维护的
    + 因为,每个人对代码内在逻辑结构的理解是不同的,不能强求
    + 所以, Leo 文件并不必须在仓库中管理
- 所以, 俺自然的想到移走 .leo 文件, 再议尝试 `hotfix finish` 就好的哪!
    + 恐怖的是,打开 Leo 文件,一片空白!
    + 一激动按了保存,连外部的 `.leo_shadow` 中以及仓库中所有源代码文件也都清空了!

傻了几分钟后, 开始补救:

- 当前被 git-flow 自动跳回了 `develop` 分支
- 先用 `git reset --hard` 恢复工作区状态
- 然后, 切换到 `hotfix/我的修订` 分支
- 将所有 `@shadow` 变成 `@nosent`, 再保存 .leo 文件
    + 这才想起来 `@shadow` 后, Leo 文件中本身就不包含代码文本了
    + 完全依赖 `.leo_shadow` 中包含 `结构注释` 的影子文件
    + `@nosent` 则相反,输出的文件是干净的,所有信息都在 Leo 文件中
        * 主要问题在, 这是单向的
        * 如果代码在外部,由其它人员修订了
        * Leo 是无从得知的,只能人工逐点合并进来
        * 当然 `@shadow` 也有相同问题
- 再移出 .leo 文件, 修订其中的目录声明
- 再次 `git flow hotfix finish` 提交
- 呜乎, 一切正常了...

## clean all
~ 惊魂稍定,想起来当年的讨论...

先回顾文档,发现:

- [Programming with Leo — Leo 5.2 documentation](http://leoeditor.com/tutorial-programming.html#summary-clean-vs-file) 也详细阐述了团队中协同的建议:
    + 如果全体都用 Leo 那么所有文件节点用 `@file` 声明
    + 否则,强烈建议 Leonine 用 `@clean` 
- 因为, 去年刚刚完成了 [mulder/ream 更新算法](http://leoeditor.com/appendices.html#the-mulder-ream-update-algorithm)
    + 原来, Leo 一直使用内置的 `difflib` 模块
        * 基于 `Bernhard Mulder` 实现的文本差异算法
        * 自动将包含 `结构注释` 文件的差异,还原入 Leo 中的节点树
    + 现在, 在以往的基础上, EKR 意识到,这种差异不一定非要在实际文件中记述!
    + 所以,现在的 `@clean` 指令进行如下神妙的处理:
        * 首先,用原先 `@file` 指令算法将当前最新节点输出为包含 `结构注释` 的文件
        * 再用相同算法,从外部对应文件读入,解析为 包含 `结构注释` 的文件
        * 最后,用内置的 `difflib` 模块对比以上两个文件
        * 获得好似原先,都用 `@file` 指令进行协同时的差异恢复序列
        * 将外部差异,从 无 `结构注释` 的文件合并回来!

`ರ_ರ` ! 
这比,俺之前建议的,通过版本系统的 hooks 进行预处理,要更加无感知哪!
老令公的脑洞依然给力哪!

## historic
~ [History of Leo — Leo 5.2 documentation](http://leoeditor.com/history.html#genesis-of-clean)

![EKR](https://d262ilb51hltx0.cloudfront.net/max/700/1*yKVZtcJyfh-FHNEtXrqjPw.jpeg) 

- 1980 接触了 CWEB
- 1995 决心实现类似软件
- 1996~98 在 Apple 的 YellowBox 中尝试
- 1999~2001 在 Borland C++ 中折腾
- 2001 遇到 Python,快速基于 Tk 完成了软件原型!
- 2002 使用 `@file` 指令来完成代码的汇入/出
- 2003 迁移工程进入 SourceForge,正式发行 Leo
- 2004 4.2发布 解决部分 gnx (Global Node Index) 和 uA (User Attributes) 同步问题
- 2008 增强了几百种功能
- 2009 终于和 Tk 友尽,全面迁移到 Qt 平台
- 2014 5.0 发布! 能和 Vim 玩在一起了
- 2015 5.1 发布, 这年一月的 `Aha` 事件,激发了 `@clean` 的诞生
    + Leo 就此能真正流行开来了!

以及: [The Leonine World — Leo 5.2 documentation](http://leoeditor.com/leonine-world.html)

# summary

i store up this mail in gmail, but never try to fixed code flow EKR's point. 
thanks for EKR's Aha, 3 years question, fixed in Leo 5.2 !
notice this, just after terror story:

- i always use Leo to develop complex scripts
    + when start PyQt4 coding, also base Leo
    + but, this time under git-flow
- even upgrade into Leo 5.2, but my skill stan as 4.0
    + as one Leonine, for Nancy in teams
    + i had usage @shadow
    + and of course put .leo into git repository too
- so in the beginning:
    + after 4 hours coding, happy finished one feature develop
    + base git-flow input:
        * $ git flow hotfix finish BIG-FEATURE
    + as normal git-flow will:
        * Latest objects have been fetched from 'origin'
        * Hotfix branch has been merged into 'master'
        * The hotfix was tagged 'BIG-FEATURE'
        * Hotfix branch has been back-merged into 'develop'
        * Hotfix branch 'hotfix/BIG-FEATURE' has been deleted
    + BUT!!! because .leo also in git
        * and can not Auto-merging with old version
        * the git-flow hotfix flow break
- terror start:
    + try move .leo out git repository, and change @path
    + wants re-write all scripts, merge again
    + BUT! i forgot @shadown node NOT save data for code
    + so, after cmd+s, i got empty .py and .leo_shadow/*.py
- CAN MOVE minutes for so terror:
    + luck remember git keep all verion in breach
    + so revert develop breach
    + change back 'hotfix/BIG-FEATURE'
        * into .leo change all @shadow to @nosent
        * move .leo out git repository
        * chnage @path
    + re-try `$ git flow hotfix finish BIG-FEATURE`
- kill the terror time

through this, i learned:

- .leo is too personal , need not put into git repositry
- @shadow is not strong enough
- nust use new directive

so review leo document, largh in Aha time ;-) 
and recheck : [Appendices — Leo 5.2 documentation](http://leoeditor.com/appendices.html#the-mulder-ream-update-algorithm)
    
notice @clean, and make confirm in:
Summary: @clean vs @file -> [Programming with Leo — Leo 5.2 documentation](http://leoeditor.com/tutorial-programming.html#summary-clean-vs-file)
    

for working with Nancy, i need @clean forever!

BUT the new leo-flow with git-flow is lost one command?

- how to updating @cloean nodes in Leo? need not to restart Leo?
- in my test:
    + edit .py out leo, make conflict
    + try cmd+s, leo alert:

... .py
 has changed outside Leo.
Overwrite the outline node?

- but try all kind of command in file menus
- not found withch one make Leo :
    + read out .py
    + base The Mulder/Ream algorithm updaing nodes
- so i had to clode all Leo windows
- restart Leo, so the "Recovered Nodes" auto generated


# 是也乎
~ 参考俺的有关演讲幻灯: [Leo](http://s5rst.qiniucdn.com/131101-leo-china/index.html) 
令老爷子,长达42年的编程经历,在不少成品问世,但是,除了维持生计的商业软件,
就是 Leo 这一非常冷门的编辑器软件,
从意动,到越来越易用,坚持了 35 年! 独自坚持完善,改进!

![ekr-github-leo-graphs](http://zoomq.qiniudn.com/ZQCollection/snap/leo/ekr-github-leo-graphs.png)

08年初,工程迁移到 github ([leo-editor/leo-editor](https://github.com/leo-editor/leo-editor/graphs/contributors))至今, 12,815 次提交中,
依然绝大多数是 EKR push 的! 

也就是说,还没有另外一位程序猿,能替代已经至少60岁的 令德华([Edward K. Ream](http://leoeditor.com/ekr.html)), 老令公 !!!

![ekr2](http://leoeditor.com/ekr2.gif)

只能祝 **LL&P** 了

`live long and prosper`


- 160417 整理分享
- 160416 惊悚故事
- 131024 发愿
