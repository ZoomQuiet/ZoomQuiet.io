Title: 如何配置 rIME 支持 GitChat 规范?
Date: 2019-02-01 10:42
Tags: MAC,Livin,SCM,markdown
Slug: rime4gitchat

[TOC]

## BG

- 新年了, 发现有 `长徦式学习症` , 很多不敢肥家被逼婚的程序猿, 宁可呆在公司一边值班一边刷课
- 同时, GitChat 也空降新领导, 启动叕一波作者鼓动
- 所以, 响应号召, 尝试分享这年几点感触
- 只是, 没想到, 对提交文章, 有了细致要求, 任何一点不达标, 直接退稿, 不允许发布
- 虽然, 申述说:
    + 通过配置输入法, 已经有15年从来不用中文标点了
    + 不仅在编程时杜绝了因为中文标点引发血案
    + 同时, 也促使行文更加国际化, 也从来没因为标点而引发误解
    + 但是, GitChat 方面不认为这是读者可以接受的
    + 其它作者也劝:"从了吧, 您就..."

> 所以...

## goal

- 找到配置, 恢复全角标点输入
- 同时兼容以往全部半角标点输入习惯
- 进一步, 是否可以用工具来完成自动化修改?


## logging
> 快速记录应对嗯哼


### sed

- [i hate Chinese symbol\! so usage: zhmark2en\.sh pwd FILEexNAME](https://gist.github.com/ZoomQuiet/53439dd21c60a935e793)
- 早年开始实行全半角标点后, 自然的基于 bash 编写了小工具
    + 可以自动用自己指定规则
    + 替换批量文本文件中所有全角标点
- 自然首先尝试基于之, 反转规则:
    + 还用之前输入习惯
    + 只是提交前, 用工具自动替换所有半角标点为编辑们渴望和依赖的中文标点

> 结果->放弃

- 首先, 中文标点有很大一批是成对却不同形状 `""　"　"`
    + 原先工具替换时是统一替换为同一形状
    + 比如,无论 `"` 或是 `"` 都嗯哼为 `"`
    + 现在想相反, 远没那么简单
- 另外, 原先替换的目标字符在 ASCII 范畴, 无论什么编码都兼容
    + 现在则不同, 中文标点只存在少数几种编码中
    + 用 shell 脚本强行修改后
    + 引发编码混乱, 文本直接乱码了
    + 强行转换回 UTF-8 依然有很大比例有吞字现象


### rIME
> 只能回到输入法本身来定制了

好在 [RIME - 中州韻輸入法引擎](https://rime.im/) 本身就是高度可定制的

- 参考: [ZqBXM/Rime\-Squirrel at master · ZoomQuiet/ZqBXM](https://github.com/ZoomQuiet/ZqBXM/tree/master/Rime-Squirrel)
- 发现当年关键几处配置
- 小心尝试几次, 便搞定

:

    /Users/zoomq/Library/Rime/
        +- alternative.yaml  ~ 全/半角标点声明
        +- ... 
        +- bxm4zq2mac.custom.yaml ~ 私制 表形码 输入法定制配置
        +- bxm4zq2mac.schema.yaml ~ 私制 表形码 输入法行为配置
        +- ...
        `- user.yaml ~ 通用输入行为配置


- 其它配置都不用动
- 单单在 `user.yaml` 中
    + `ascii_punct: true` 
    + `full_shape: false`
    + 这两个配置反转就好
    
## GitChat-style
> 饭桶式写作输入

- 原先 rIME 配合私制 `表形码` 进行写作和编程时, 行为很简洁:
    + `control+空格`　切换到 `鼠鬚管` (中州韻 输入法平台 macOS 版本代号)
        * 随便输入就好...
    + 如果有大段英文输入, 不想触发中文选字
        * `shift` 切换状态, 或 `option+~` 选择输入状态
    + 以上
- 现在, 为了兼容编辑们的期待, 行为就业务性冗余了:
    + 输入正文时, 必须:
        * `shift` 切换为中文输入模式
        * 再用 `shift+空格` 切换为到 `全角` 标点
        * 此时, 所有标点是`中文式`的
    + 输入 markdown 相关结构字符时, 又必须:
        * `shift` 切换为中文输入模式
        * 再用 `shift+空格` 切换为到 `半角` 标点
        * 此时, 类似 `+ - >` 以及空格/tab 都是 ASCII 式, markdown 可理解的
    + 输入英文单词/术语时, 又必须:
        * `shift` 切换为中文输入模式
        * 再用 `shift+空格` 切换为到 `半角` 标点
        * 再用 `shift` 切换为 en 输入模式
        * 此时, 才能输入正常 ASCII 字符
        * 否则是类似 `ＡＳＣＩＩ`　全角英文

综上, rIME 支持灵活丰富的输入模式:

- 可是为了灵活, 不得不劳累用户显式指令切换模式
- 同时, 从法理上不同输入模式中, ASCII 字符形态是不兼容
- 而 GitChat 编辑又要求在同一篇文章中:
    + 不同格式标点,空格
    + 和不同形式字符
    + 又必须 `合理? 美观? 合规?` 并举
- 导致至少多出一倍毫无必要的击键操作
- 以及, 和以往主要输入行为完全不同的心智判定损耗
- 可以说, 是 `GitChat 式工伤`

## refer

- [Chat 发布与写作指南](https://gitbook.cn/books/5c47da3ef79c0c1f90492403/index.html)
- [中文排版需求](http://w3c.github.io/clreq/zh/)
    + [从"中文排版规范"开始](http://devrel.zoomquiet.top/data/20150402184838/index.html)
    + 对比: [Requirements for Japanese Text Layout](https://www.w3.org/TR/jlreq/)
- [中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.md#%E7%A9%BA%E6%A0%BC)
    + [vinta/pangu.js: 為什麼你們就是不能加個空格呢?](https://github.com/vinta/pangu.js?utm_source=www.appinn.com)
- [全角半角碎碎念 - The Type](https://mp.weixin.qq.com/s/Vu-20r7_LCTToyaOeli7tg)
    + `...可见,中文的标点符号既可以是'全宽'的也可以是'半宽'的,'中文＝全角'完全是技术问题导致的误解. `
    + [全角和半角 \- 维基百科,自由的百科全书](https://zh.wikipedia.org/wiki/%E5%85%A8%E5%BD%A2%E5%92%8C%E5%8D%8A%E5%BD%A2)

## Sayeahooo

- h 资料搜索理解
- 2d gitlab 尝试/生效
- 4h github 嗯哼
    + 3h 域名迁移尝试
- 2h 截屏,文档嗯哼...
