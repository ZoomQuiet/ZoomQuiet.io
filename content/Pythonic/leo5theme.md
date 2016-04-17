Title: Leo 5.2 theme custom
Date: 2016-04-15
Tags: python,howto,leo,theme
Slug: leo5theme


[TOC]

# EN

thanks guys in `leo-editor@googlegroups.com` :

- Terry Brown
- john lunzer

make me know how to custom Leo theme step by step:

- old versions `myLeoSettings.leo` appended buttons :
    - at `leo/myLeoSettings.leo#Startup-->Local buttons`
    - need copy from  `leoSettings.leo` 
* so my custome flow as:
    * try edit some node
    * click `reload-styles`
    * open other `.leo` , check effect
    * close it
    * loop up steps

finally all i custom in  `~/.leo/myLeoSettings.leo` :

- appended help menus:
    + `#@settings-->Menus-->@menus-->@menu &Help-->@item open-myLeoSettings-leo`
- bigger cursor:
    + `#@settings-->Qt Gui Misc settings-->@int qt-cursor-width = 6`
- font changed:
    + `#@settings-->Appearance (change these first)-->Qt Gui settings-->Fonts-->Basic Fonts (change these first)-->@string font-family = Input, Droid Sans Mono, DejaVu Sans Mono`
- body-bg dark:
    + `#@settings-->Appearance (change these first)-->Qt Gui settings-->Colors-->Body pane colors-->@color body-bg = #2F3337` 
- close Gutter:
    + `#@settings-->Appearance (change these first)-->Qt Gui settings-->Margins & borders-->Gutter-->@bool use-gutter = False`
- custom border-focus-color:
    + `myLeoSettings.leo#@settings-->Appearance (change these first)-->Qt Gui settings-->Colors-->Border colors-->@color focused-border-focus-color = #85C2FF`
- Python syntax coloring:
    + `#@settings-->Syntax coloring-->Language-specific colors-->Python`

appended nodes:

    @color blank_color = grey
    @color tab_color = red
    @color label_color = red
    @color keyword1_color = #268bd2
    @color keyword2_color = #2aa198
    @color keyword3_color = #859900
    @color keyword4_color = #268bd2
    @color literal1_color = #cb4b16
    @color literal2_color = #b58900
    @color literal3_color = #dc322f
    @color literal4_color = #859900
    @color markup_color = #2aa198
    @color comment1_color = #557755
    @color comment2_color = #557755
    @color comment3_color = #557755
    @color comment4_color = #557755
    @color operator_color = #bbbbbb
    @color function_color = #cb4b16


- `self` with coloring
    + fixed `path/2/installed/leo/modes/python.py`
    + appended `"self": "keyword4",`




# 是也乎
~ 老问题新解决

## 背景
[Leo](http://leoeditor.com/leo_toc.html) ![Leo4](http://leoeditor.com/_static/Leo4-80-border.jpg)

- 参考: [LeoEnvironment - Woodpecker Wiki for CPUG](http://wiki.woodpecker.org.cn/moin/LeoEnvironment)
- 从 05 年开始使用
- 从笔记到工程管理,都用的非常欢实
- 是 令德华([Edward K. Ream](http://leoeditor.com/ekr.html)) 独立创建并长期维护的,完备的文学化编辑环境
- 09年从 Tk 迁移到 Qt 后平滑的跟随俺转战 M$/Ubuntu/MAC 所有桌面系统
- 嗯哼,完全基于 Python 开发的...
- 详细介绍,参考 [PyConChina2013-EKR-final-v2](http://zoomq.qiniudn.com/pychina/PyCon2013China/PyConChina2013-EKR-final-v2.mp4) ~ 老令公 在 PyCon2013China 大会上分享的视频

## 问题
但是,使用最性感的编辑器 sublime text 后, 对 Leo 默认的界面就万般难以忍受了...

终于决心折腾一下样式!

- Leo 基于几个配置文件:
    + 默认配置 `path/2/installed/Leo/config/leoSettings.leo`
    + 用户配置 `~/.leo/myLeoSettings.leo`
- 俺从 3.1 版本开始使用 Leo, 现在的稳定版本是 5.2
- 所以, `~/.leo/myLeoSettings.leo` 和官方的默认有较大偏差
- 那么如何解决:
    + 启用[Leo 4.11](http://leoeditor.com/what-is-new.html#what-s-new-in-leo-4-11) 开始有的 `sublime Text 2, a dark colorizing theme`?
    + 如何令 `self` 也有语法颜色?
    + 如何改变默认的 `cursor` 尺寸?

## 过程

简单的说,手上的配置文件有这几种:

- `~/.leo/myLeoSettings.leo` 混杂了增补多年配置的可能不兼容配置
- `path/2/installed/Leo/config/leoSettings.leo` 5.2 最新版本配置
- `path/2/installed/Leo/config/exampleSettings.leo` 5.2 内置配置示例
- `path/2/installed/Leo/config/themes.leo` 5.2 内置 theme 定制示例

先后进行的尝试:

- 在 `exampleSettings.leo` 基础上
    + 先完成积累的习惯配置
    + 再进行 theme 配置
    + 失败! 原先的配置点太多:
        * 快捷键
        * 窗口布局
        * 字体
        * 颜色
        * 菜单...
- 在 `leoSettings.leo` 基础上
    + 先完成积累的习惯配置
    + 再进行 theme 配置
    + 失败! 原因同上
- 最终只好一边询问社区列表,一边基于 `~/.leo/myLeoSettings.leo` 进行配置
    + 从 `leoSettings.leo` 复制相应最新配置树过来
    + 参考原先的进行对应配置

## 要点
~成功将 ![leoeditor](http://leoeditor.com/screen-shots/render-svg-sources.png)
变成:
![leo5.2_darktheme](http://zoomq.qiniudn.com/ZQCollection/snap/leo/leo5.2_darktheme.png)


- `myLeoSettings.leo` 的控制按钮:
    - 来自 `leo/myLeoSettings.leo#Startup-->Local buttons`, 要从  `leoSettings.leo` 复制
    - 这样进行之后的配置尝试时的流程才能固化为:
        - 进行对应 node 的修订
        - 点击 `reload-styles`
        - 打开另外一个 `.leo` 观察效果
        - 关闭
        - 重复以上

相关 `~/.leo/myLeoSettings.leo` 的配置点:

- 追加帮助菜单:
    + `#@settings-->Menus-->@menus-->@menu &Help-->@item open-myLeoSettings-leo`
- 光标加粗:
    + `#@settings-->Qt Gui Misc settings-->@int qt-cursor-width = 6`
- 字体指定:
    + `#@settings-->Appearance (change these first)-->Qt Gui settings-->Fonts-->Basic Fonts (change these first)-->@string font-family = Input, Droid Sans Mono, DejaVu Sans Mono`
- 编辑窗口底色:
    + `#@settings-->Appearance (change these first)-->Qt Gui settings-->Colors-->Body pane colors-->@color body-bg = #2F3337` 
- 关闭行数:
    + `#@settings-->Appearance (change these first)-->Qt Gui settings-->Margins & borders-->Gutter-->@bool use-gutter = False`
- 修订窗格激活提醒框
    + `myLeoSettings.leo#@settings-->Appearance (change these first)-->Qt Gui settings-->Colors-->Border colors-->@color focused-border-focus-color = #85C2FF`
- Python 语法颜色自定:
    + `#@settings-->Syntax coloring-->Language-specific colors-->Python`

逐一追加 node:

    @color blank_color = grey
    @color tab_color = red
    @color label_color = red
    @color keyword1_color = #268bd2
    @color keyword2_color = #2aa198
    @color keyword3_color = #859900
    @color keyword4_color = #268bd2
    @color literal1_color = #cb4b16
    @color literal2_color = #b58900
    @color literal3_color = #dc322f
    @color literal4_color = #859900
    @color markup_color = #2aa198
    @color comment1_color = #557755
    @color comment2_color = #557755
    @color comment3_color = #557755
    @color comment4_color = #557755
    @color operator_color = #bbbbbb
    @color function_color = #cb4b16


- `self` 非关键词追加语法颜色
    + 修订 `path/2/installed/leo/modes/python.py`
    + 追加 `"self": "keyword4",`


感谢 `leo-editor@googlegroups.com` 列表中好人的大力帮助:

- Terry Brown
- john lunzer

## timing

```
+ 1.5h 根据记忆折腾
+ .5h 官方列表提问
+ 2h 使用官方配置折腾
+ 1h 使用列表提示检验
+ .5h 完成心目中的配置

~ 6h 才完成...
```

- 140909 才算完成一个可以看的版本
- 140711 完成所有功能,启动文档回顾

## TODO

- subl theme 到 Leo theme 的转换脚本
- 进一步的样式化:
    + 髙亮当前行
    + 提纲界面的 dark theme
    + log 界面的 dark theme
    + find 界面的 dark theme
    + ...
- 参考颜色: [Leo Color Map](http://leo-editor.github.io/snippets/colormap.html)

   
