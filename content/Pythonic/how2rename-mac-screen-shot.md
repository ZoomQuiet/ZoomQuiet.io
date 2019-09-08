Title: 如何自在定义 macOS 截屏文件名?
Date: 2019-02-13 22:42
Tags: MAC,Livin,SCM
Slug: how2rename-mac-screen-shot

[TOC]

## BG

- 默认系统截屏工具输出图片是:
    + 到桌面
    + 文件名: `屏幕快照 2019-02-13 17.17.32.png`

## goal
- 当年在 Linux 中,是可以自由定义输出的, 俺期望是:
    + `screenshot_190213-17.17.32.jpg`
- 现在怎么作到?

## logging
> 记要尝试过程


### 格式

    $ defaults write com.apple.screencapture type jpg
    $ killall SystemUIServer

以上即可

### 命名

    $ defaults write com.apple.screencapture name screenshot
    $ killall SystemUIServer

以上只能变成:

    screenshot 2019-02-13 17.17.32.jpg

### ScreenCapture.strings
以往可以进行的

    sudo su
    cd /System/Library/CoreServices/SystemUIServer.app/Contents/Resources/Spanish.lpro 
    plutil -convert xml1 ScreenCapture.strings
    vim ScreenCapture.strings

在 macOS Sierra 10.12.6 中失败:

- 无论是否是 root 身份
- 都说系统没有权限

### Automator

另外一种思路是用内置自动脚本来刷指定目录中指定文件名的文件名:

- 但是, 尝试后发现, 这种可视化编程限制太多
- 而且调整困难, 根本无法有效完成设想


### bash

经检测:

    screencapture -io ~/Desktop/screenshot_`date '+%y%m%d-%H.%M.%S'`.jpg

可以满足所有构想,可是:

- 先要打开终端
- 运行, 无论是配置为别名, 还是部署为指定 .sh 脚本
- 然后才能进行截屏
- 相比原先随时 `cmd+shift+4` 进入截屏, 还是多了一层, 不方便

问题变成如何可以用原有快捷键调用 bash 指令?

- alfred 复杂
- HotKey 只能绑定 .app 使用自定快捷键
    + 那么问题进一步变成: `如何快速将一个 shell 脚本变成标准 mac app?`
    + 果然有很多方式, 脚本,编译,应用...
    + 试用 Platypus 一下子就形成了无界面后台运行的 app
- 配合 HotKay 达成目标效果 ;-)

![screenshot_190213](https://ipic.zoomquiet.top/2019-02-13-screenshot_190213-23.03.43.jpg)


## refer

- [TIP: Change default screen shot filenames, format and location | Snow Leopard Tips](http://snowleopardtips.net/tips/everything-you-need-to-know-about-screen-captures.html)
    + [The Complete Guide to Mac OS X Screenshots - TekRevue](https://www.tekrevue.com/tip/how-to-customize-screenshot-options-in-mac-os-x/)
    + [uti - Changing the default screenshot filename - Ask Different](https://apple.stackexchange.com/questions/27729/changing-the-default-screenshot-filename)
    + ...
- [macos \- How to create an OSX Application to wrap a call to a shell script? \- Ask Different](https://apple.stackexchange.com/questions/200125/how-to-create-an-osx-application-to-wrap-a-call-to-a-shell-script)
    + [macos \- Run AppleScript from bash script \- Ask Different](https://apple.stackexchange.com/questions/103621/run-applescript-from-bash-script)
    + [macos \- Converting a Shell Script Into a \*\.app File \- Stack Overflow](https://stackoverflow.com/questions/30792569/converting-a-shell-script-into-a-app-file)
    + [Creating Mac Applications from Shell Scripts \- Christopher Su](https://christopher.su/2012/creating-mac-applications-shell-scripts/)
    + [Platypus \- Create Mac apps from command line scripts \|](https://sveinbjorn.org/platypus)

## Sayeahooo

- 1.5h 资料搜索理解
- 2h 嗯哼
- .5h 截屏,文档嗯哼...
