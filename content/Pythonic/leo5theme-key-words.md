Title: Leo 5.4 theme custom
Date: 2016-11-17
Tags: python,howto,leo,theme
Slug: leo5theme-key-words


[TOC]

## 背景

[Leo 5.2 theme custom](http://blog.zoomquiet.io/leo5theme.html)

Leo 是灵活的完全 Pythonic 的可定制 `文学化编辑环境` ...

所以,其定制的进展是无限的...

## 现象

- 在完成了基本的 theme 定制后发现
- 默认语法元素的颜色,不太理想
- 特别是: [<<Sections>>](http://leoeditor.com/cheatsheet.html#id13)
    + 可以将下层节点放置在任何想放置的地方的引入点声明
    + 但是,这里 `<<...>>` 两端符号的颜色是默认兰色
    + 在暗色背景中看不清楚
- 可能一时没能找到配置处

## 解决

- 通过社区列表咨询
    + 2天后收到各种建议
- 才知道是俺使用 Leo 的配置文件过老
    + 导致新版本的全局 theme 定义节点
    + `lThemes: copy to last top-level setting in myLeoSettings.leo-->Common to all themes-->Colors for Leo constructs (all themes)`
    + 没有部署在 `@setting` 下
- 立即复制过去
    + `@color section_name_brackets_color = orange`
    + 就将对应符号颜色定义为 橙色 了...


## 记要

- 要有信心,可配置的
- 要认真向社区咨询
- 要大胆的实验
- 毕竟,编辑环境任何一点的改进,都对编程过程带来无法衡量的心理支持

## logging

- 160921 感觉到问题
- 161011 有空尝试解决
- 161111 通过社区解决
- 161201 才有空补全

