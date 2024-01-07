#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Changelog:

    - 181230 append utteranc.es
    - 130812 append Disqus
    - 130326 append v2.ta.qq
    - 11.10.27 fixed gen path
    - 10.9.8 fixed for options judge
    - 10.9.7 fixed for zqlog
    - 10.9.2 fixed as ZqLib
    - 9.11.03 for KUP++ mapping fixed
    - 9.05.16 for kup.s.kingsoft.net/map as root
    - 9.04.21 for deep dir gen html
    - 9.03.12 for KUP.rdev dot mapping gen html
'''
VERSION = "11.10.27"
SETFONT="fontname='WenQuanYi Micro Hei'"
ARGDOT="-G%(SETFONT)s -N%(SETFONT)s -E%(SETFONT)s" % locals()
#DOROOT = "/opt/homebrew/bin"
DODOT = "/opt/homebrew/bin/dot %s "+ARGDOT+" -Tpng -o %s.png -Tcmapx -o %s.map "
DOFDP = "/opt/homebrew/bin/fdp %s "+ARGDOT+" -Tpng -o %s.png -Tcmapx -o %s.map "
DOCIR = "/opt/homebrew/bin/circo %s "+ARGDOT+" -Tpng -o %s.png -Tcmapx -o %s.map "
DONEA = "/opt/homebrew/bin/neato %s "+ARGDOT+" -Tpng -o %s.png -Tcmapx -o %s.map "
DOTWO = "/opt/homebrew/bin/twopi %s "+ARGDOT+" -Tpng -o %s.png -Tcmapx -o %s.map "

IMGTYPE = "png"

#dotPageTitle dotPageStyle imgame mapname map4dot
DEFEXPORT = "stdout"
DEFTITLE = "mapping base .dot"
MAPID = "SomeGraph"
DOTXT = "%s.dot"%MAPID
TPLidxHTM='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN" lang="zh-CN">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" >
  <title>%(pageTitle)s</title>
	<link rel="icon" href="zqstudio.ico" type="image/gif">
	<link rel="shortcut icon" href="zqstudio.ico" type="image/gif">
<style type="text/css">
%(styleData)s
</style>
</head>
<body>
<!--Sticky Footer Solution  http://www.cssstickyfooter.com-->
<div id="wrap">
    <div id="main" class="clearfix">
        <img src="data:image/%(picType)s;base64,%(mainMapURI)s" 
            usemap="#%(mainMap)s"
            id="%(mainMap)s" alt="%(mainMap)s"/>
        %(mainImageMap)s

	</div><!-- cssstickyfooter::id="main" class="clearfix"-->
</div><!-- cssstickyfooter::id="wrap"-->
'''

'''
        <img src="data:image/%(picType)s;base64,%(legendMapURI)s" 
            usemap="#%(legendMap)s"
            id="%(legendMap)s" alt="%(legendMap)s"/>
        %(legendImageMap)s
'''

TPLidxHTM+='''
<div id="footer" class="footbar">

<a href="http://browsehappy.com/why/">
<img
 src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAAPCAMAAABEF7i9AAABlVBMVEUeitkghtohhNghkN0if9UigtkikN4ikd8ik98ileAil+AimeEimuAje8wjhNwjh90jitwjj98kh9klh90lid8liuAli+AlouQmh94mitgmitsnpuYqj9crk+Qrq+YtouEususxi88znug0p+I1r904jc4+ktQ+qOo/vulBotREyu9Uk85YtONlz+xmZmZoxe1qp9hvrdtzvNh1y+Z6qst7v9yAt96Es9uEtN6GzeWJoMeMrc+NwdmOutuPw+WQud2Rxd6T0OWWe5qazeWcyOmfz+mf2O2iutWmx+Soz+Kpy+ap2uyryuWtkqyt2Omvy+Svy+Wwy+Wwzuay0OK42u270ea82ei+3+vA3OrCorLF2OrJxNTL4PDN4PHO3OnP4e3W4uzc7PPi6/Pi7/bn8PboHybt9fnuIynv9Pfx9fn0Jyr0+Pr2+Pn2+fv2+fz2+vv4+vv6w8X7eXr7/P38/P39LS39/v7+/v7/AAD/AgL/ExP/Li7/QED/YWH/fHz/i4v/mpr/trb/x8f/6ur/9fX//Pz////7om9CAAABKElEQVR42q2TVW/DQBCEXWZuU2amlJmZmZmZKdnYTuI4zvzuSidbp0ayKsWel9m5h0+j2zvBabMEJ5h8ksr8bffg0YfIZQAVieC62FudGr/F0Y/CzigCGUBNVEETXa1NFeW9r+cfomYV6PfiaYA6G8ryU2Lan+H1WwXKASz0DNPM9Wh8VvYhArIBBHEycz3yAeCBA8Wgq3urppqW54scuf0IihzIzAD+TTDMCBzoCX2fNhYnCxSVkZ7TgZDHtCFPgG46MKwhRlKTSo5PaGN988ysIbd/G8qBl8rEhMzF9zUqbNk3v0Oe2MSBQPiWd2rrHHlxadFVNPtlw5Y1caXvsjm2oLS+bYmgWn+HUO4G3Q9DY9PbV26QpMAyEJ83k3P3bFIli3/ZZv0CIEnzewB06Q4AAAAASUVORK5CYII=" 
    id="noIE!" alt="noIE!"/>
</a>
powered by:
    <a href="http://www.python.org/">Python</a>
    ,<a href="http://leoeditor.com/">Leo</a>
    ,<a href="http://www.graphviz.org/About.php">graphviz</a>
<!--
    ,<a href="http://developer.qiniu.com/">七牛</a>
-->
    ,<a href="http://www.catb.org/hacker-emblem/">Hacker</a>
    ,<a href="http://wenq.org/" title="文泉驿">
    <img src="https://ipic.zoomquiet.top/2022-06-22-powered_by_wqy_14px.png" alt="文泉驿提供动力"/>
 </a>

{
<a href="http://creativecommons.org/licenses/by-sa/2.5/cn/">
<img
 src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAAPCAIAAAD8q9/YAAAABGdBTUEAANbY1E9YMgAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAIySURBVHjaYmAYYYARiP///z9SfMvIyAJhrdm0Glliz669M6fO7OjoKC8vx9Tm6up66tSptu5WcQlxIFdeVsHVyfXjh4+D3LeQeGXClHj54uXyxctx+RYIdu/ebWZmNrl/CoT74eOHwoLCoRLJWDy8fMkKYWFhXL6FAGBw3Lxxc8PajUD2x08fPHw8vH28h6qHL128lJ6eDmScPXtWWVkZmO6Bafj9+/dAEsgGigDFjY2NXVxcrl29BjWFiQnIRUs/EICcnDDZ+LXQonBhwvDt5c+fPgP9A2SHhYUBGUBbgWRnZyfQn+/evQPG/L1794CyQME7t+/AUzUwkWOWEEAAcTScASSBbKy+ZYQBZC7V/Yzu4a9fvgBJQUFBYJQCPQbxOTABA9lKSkpA8bS0tNDQUFgRD3X6z58/GFkYscYY3HsQ18O5aPEJkUVLCPSIYW4eHiAJ9C3Qb0AfAmMVUiwDuUA/A8UrKipmzZqFljjZ2Tn+//mPJ4ax1hDw+MSqHk2WVh7W09fl5eWF+BMYsXv27AHaCvQ5kA2MbSEhIaAIJLueOXNGUVkRokuAXwBYUeGPYYJ1BknqKW14INfDfV39z58+v3//Ph5twBAxMTGJjosOCPYHcmWl5Zobmrdu2TrI62FgaGIppaPjot6+fQOMUjyay8rKVFSVIb7l5xPYsWXHIPctvmoJ2H5KzUytrKxsb2/HqsfJ2en69esFJQXw9Nw/oX+0LT1I29IjrbPEABBgAEdwNeO7yfOaAAAAAElFTkSuQmCC" 
    id="(cc)/by-sa/" alt="(cc)/by-sa/"/>
</a>
}


</div><!-- cssstickyfooter::id="footer"-->
<!--Sticky Footer Solution
http://www.cssstickyfooter.com
-->
<script src="http://ajax.microsoft.com/ajax/jquery/jquery-1.4.2.min.js" type="text/javascript"></script>
<script type="text/javascript">
%(jsActions)s
</script>



<!-- DISCUS like.. -->
<script src="https://utteranc.es/client.js"
        repo="101camp/io"
        issue-term="url"
        theme="github-dark"
        crossorigin="anonymous"
        async>
</script>

</body>
</html>
'''
TPLcssURI='''#%(dataID)s {
    margin-left: %(imgWidth)spx;
    background-image: url('data:image/%(picType)s;base64,%(dataURI)s') top left no-repeat;
}
'''
TPLcssZIP='''
%(cssEmbed)s

%(uriEmbed)s
'''

DEFLEGEND="zoomquiet_org_idx_legend"



def __chkPath(path,log):
    '''检验路径，如果为空，设为 . 以便统一使用 "%s/%s"%(path,file) 形式
    '''
    if 0 == len(path):
        return "."
    else:
        return path


import os
import sys
import fnmatch
import subprocess

# for OptionParser chinese help
from optparse import OptionParser,OptionGroup
from datetime import datetime

#from importlib import reload
#reload(sys)
#sys.setdefaultencoding('utf-8')


class zqlog():
    '''z quickly logging,export all kinds of log as stderr
    usage:
        log = zqlog()
        log.info
        log.debug
        log.error
        log.warning

        log.info("info!")
        log.debug("debug!")
        log.error("error!")
        log.warning("warning")
    配合CL参数: -Q|V|N|D 过滤不同等级的输出
    mdebug|verbose|mquiet|mnotdo
    '''
    def __init__(self,optionValues):
        '''初始化日志输出句柄
        '''
        self.tformatter = "%y%m%d %H:%M:%S,%f"
        self.lformatter = "[%(asctime)s]- %(levelname)-8s - %(message)s\n"
        self.hdlr = sys.stderr
        self.ov = optionValues

    def __logit(self, levelname,message):
        '''日志输出行动函式
        datetime.datetime.now().strftime("%y%m%d %H:%M:%S,%f")
        '''
        asctime = datetime.now().strftime(self.tformatter)
        levelname = levelname.upper()
        self.hdlr.write(self.lformatter%locals())
    def __getattr__(self, levelname):
        #print self.ov
        if self.ov.mnotdo:
            # -N 仅仅INFO
            if levelname == "info":
                self.__dict__[levelname] = lambda message:self.__logit(levelname,str(message))
            else:
                self.__dict__[levelname] = lambda message:None
        elif self.ov.verbose:
            # -V 仅不输出 DEBUG
            if levelname == "debug":
                self.__dict__[levelname] = lambda message:None
            else:
                self.__dict__[levelname] = lambda message:self.__logit(levelname,str(message))
        elif self.ov.mdebug:
            # -D 输出一切
            self.__dict__[levelname] = lambda message:self.__logit(levelname,str(message))
        else:
            # 默认情况同 -Q
            self.__dict__[levelname] = lambda message:None

def gen2html(ov,log):
    """usage dot exp png+img map,auto usage html tpl writ out idenx page!
    #dotPageTitle dotPageStyle imgame mapname map4dot
    考虑通用的参数组合处理:
        +-- 工作流方式
        +-- 图转换?
    #ov:   默认 dotscript expage 三条件,
    组合:
        empty:
            +-- 内置dot文本
            +-- 输出到脚本所在目录
        仅dotscript
            +-- 指定dot文本
            +-- 输出到dot脚本所在目录
        仅expage
            +-- 内置dot文本
            +-- 输出到指定页面所在目录
        dotscript and expage
            +-- 指定dot文本
            +-- 输出到指定页面所在目录
    """
    #options_as_dict = eval(str(ov))
    #options_as_set = set(options_as_dict.items())
    global HTMTPL,DOTXT,MAPID,DEFEXPORT
    SCRIPT = os.path.basename(sys.argv[0])
    # 默认情况以自身所在目录为准输出
    pathSelf = __chkPath(os.path.dirname(sys.argv[0]),log)
    log.debug('DEFEXPORT:\t%s'%DEFEXPORT)
    log.debug('IMGTYPE:\t%s'%IMGTYPE)
    if DEFEXPORT == ov.expage and "battery" != ov.dotscript:
        #仅 -d
        pathDotxt = __chkPath(os.path.dirname(ov.dotscript),log)
        RELPATH = pathDotxt
        DOTXT = ov.dotscript
        MAPID = os.path.basename(ov.dotscript[:-4])
    elif DEFEXPORT != ov.expage and "battery" == ov.dotscript:
        #只 -o
        pathExport = __chkPath(os.path.dirname(ov.expage),log)
        RELPATH = pathExport
        DEFEXPORT = ov.expage
    elif DEFEXPORT != ov.expage and "battery" != ov.dotscript:
        #都有 -o|-d
        pathExport = __chkPath(os.path.dirname(ov.expage),log)
        MAPID = os.path.basename(ov.dotscript[:-4])
        RELPATH = pathExport
        DOTXT = ov.dotscript
        DEFEXPORT = ov.expage
    else:
        #默认 无参数时
        RELPATH = pathSelf
        DOTXT = "%s/%s"%(pathSelf,DOTXT)
    log.debug("RELPATH:\t%s"%RELPATH)
    EXPAS = "%s/%s"%(RELPATH,MAPID)
    log.debug("EXPAS:\t%s"%EXPAS)


    # --fdp 响应:切换dot 生成命令
    if ov.fdp:
        DOTORDER = DOFDP
    elif ov.circo:
        DOTORDER = DOCIR
    elif ov.neato:
        DOTORDER = DONEA
    elif ov.twopi:
        DOTORDER = DOTWO
    else:
        DOTORDER = DODOT
    #DODOT = "dot %s.dot -Tpng -o %s.png -Tcmapx -o %s.map"
    _DODOT = DOTORDER%(DOTXT,EXPAS,EXPAS)
    #log.info(DOTORDER%(DOTXT,EXPAS,EXPAS))
    #print(DOTORDER%(DOTXT,EXPAS,EXPAS))
    print(_DODOT)
    try:
        #,universal_newlines=True,close_fds=True
        p =  subprocess.Popen(_DODOT #DOTORDER%(DOTXT,EXPAS,EXPAS)
            ,shell=True
            ,stdin=subprocess.PIPE
            ,stdout=subprocess.PIPE
            ,stderr=subprocess.PIPE)
        #i, r, e = (p.pid, p.stdout, p.stderr)
        #log.debug("retcode:\t%s"%retcode)
        log.debug("subID:\t%s"%p.pid)
        #log.debug("stdin:\t%s"%p.stdin.readlines())
        #log.debug("stderr:\t%s"%"".join(p.stderr.readlines()))
        #log.debug("stdout:\t%s"%"".join(p.stdout.readlines()))
    except OSError as e:
        log.debug("OSError:\t%s"%e)

    log.debug("dotmap:\t%s.%s"%(EXPAS,IMGTYPE))
    picType = IMGTYPE
    #print(RELPATH,"%s.%s"%(MAPID,IMGTYPE),log)
    imgDataURI(RELPATH,"%s.%s"%(MAPID,IMGTYPE),log)
    uriEmbed = ""
    '''
    # embded 图例
    dataID = DEFLEGEND
    dataURI = open("%s/%s.%s.b64"%(pathSelf,DEFLEGEND,IMGTYPE),'r').read()
    imgWidth = getJpegInfo(pathSelf,"%s.%s"%(DEFLEGEND,IMGTYPE),log)[0]
    uriEmbed += TPLcssURI%locals()
    # embded 主图谱
    dataID = MAPID
    dataURI = imgDataURI(RELPATH,"%s.%s"%(MAPID,IMGTYPE),log)
    imgWidth = getJpegInfo(RELPATH,"%s.%s"%(MAPID,IMGTYPE),log)[0]
    uriEmbed += TPLcssURI%locals()
    '''
    #log.debug(locals().keys())
    list4cssEmbed = fnmatch.filter(os.listdir("%s/css"%pathSelf),"*.css")
    list4cssEmbed.sort()
    #log.debug(pathSelf)
    #log.debug(list4cssEmbed)
    cssEmbed = "".join([open("%s/css/%s"%(pathSelf,i),'r').read() for i in list4cssEmbed])

    styleData = TPLcssZIP%locals()
    #log.debug("styleData:\n\t%s"%styleData)
    #<title>%(pageTitle)s</title>
    #        <img src="data:image/%(picType)s;base64,%(mainMapURI)s" 
    #            id="%(mainMap)s" alt="%(mainMap)s"/>
    #    %(mainImageMaps)s
    #        <img src="data:image/%(picType)s;base64,%(legendMapURI)s" 
    #            usemap="#%(legendMap)s"
    #            id="%(legendMap)s" alt="%(legendMap)s"/>
    #        %(legendImageMap)s
    #   %(styleData)s
    #   jsActions
    genTime = datetime.now().strftime(log.tformatter)
    pageTitle = "%s {by %s v%s at:%s}"%(ov.title
        ,SCRIPT
        ,VERSION
        ,genTime
        )
    #log.debug("mainMapURI:\t%s.%s.b64"%(EXPAS,picType))
    mainMapURI = open("%s.%s.b64"%(EXPAS,picType),'r').read()
    #log.debug("mainMapURI:\t%s"%mainMapURI)
    mainMap = MAPID
    #log.debug("dotmap:\t%s.map"%EXPAS)
    #log.debug(open("%s.map"%EXPAS,'r').read())
    mainImageMap = open("%s.map"%EXPAS,'r').read()

    legendMap = DEFLEGEND
    legendMapURI = open("%s/%s.%s.b64"%(pathSelf,DEFLEGEND,picType),'r').read()
    legendImageMap = open("%s/%s.map"%(pathSelf,DEFLEGEND),'r').read()

    list4jsEmbed = fnmatch.filter(os.listdir("%s/j"%pathSelf),"*.js")
    list4jsEmbed.sort()
    #log.debug(list4jsEmbed)
    jsActions = "".join([open("%s/j/%s"%(pathSelf,i),'r').read() for i in list4jsEmbed])

    if "stdout" == DEFEXPORT:
        #log.debug("DEFEXPORT:\t sys.stdout")
        sys.stdout.write(TPLidxHTM%locals())
    else:
        #log.debug("DEFEXPORT:\t %s"%DEFEXPORT)
        open(DEFEXPORT,'w').write(TPLidxHTM%locals())
    #log.debug(TPLidxHTM%locals())

def getJpegInfo(pathPic,picName,log):
    '''base Python and the JPEG Image File, Part 1, The Header - Python
    http://www.daniweb.com/forums/thread71188.html
        print out the hex bytes of a jpeg file, find end of header, image size, and extract any text comment
        (JPEG = Joint Photographic Experts Group)
        tested with Python24    vegaseat    21sep2005
    '''
    try:
        # the sample jpeg file is an "all blue 80x80 200dpi image, saved at a quality of 90"
        # with the quoted comment added
        imageFile = '%s/%s'%(pathPic,picName)
        data = open(imageFile, "rb").read()
    except IOError:
        print( "Image file %s not found" % imageFile)
        raise SystemExit
    # initialize empty list
    hexList = []
    for ch in data:
        # make a hex byte
        byt = "%02X" % ord(ch)
        hexList.append(byt)
    #print hexList  # test
    '''
    print
    print "hex dump of a 80x80 200dpi all blue jpeg file:"
    print "(the first two bytes FF and D8 mark a jpeg file)"
    print "(index 6,7,8,9 spells out the subtype JFIF)"
    k = 0
    for byt in hexList:
        # add spacer every 8 bytes
        if k % 8 == 0:
            print "  ",
        # new line every 16 bytes
        if k % 16 == 0:
            print
        print byt,
        k += 1

    print
    print "-"*50

    # the header goes from FF D8 to the first FF C4 marker
    for k in range(len(hexList)-1):
        if hexList[k] == 'FF' and hexList[k+1] == 'C4':
            #print "end of header at index %d (%s)" % (k, hex(k))
            log.debug("end of header at index %d (%s)" % (k, hex(k))
            break
    '''

    # find pixel width and height of image
    # located at offset 5,6 (highbyte,lowbyte) and 7,8 after FF C0 or FF C2 marker
    for k in range(len(hexList)-1):
        if hexList[k] == 'FF' and (hexList[k+1] == 'C0' or hexList[k+1] == 'C2'):
            #print k, hex(k)  # test
            height = int(hexList[k+5],16)*256 + int(hexList[k+6],16)
            width  = int(hexList[k+7],16)*256 + int(hexList[k+8],16)
            #print "width = %d  height = %d pixels" % (width, height)
            log.debug("width = %d  height = %d pixels" % (width, height))
            return (str(width),str(height))
    # find any comment inserted into the jpeg file
    # marker is FF FE followed by the highbyte/lowbyte of comment length, then comment text
    '''
    comment = ""
    for k in range(len(hexList)-1):
        if hexList[k] == 'FF' and hexList[k+1] == 'FE':
            #print k, hex(k)  # test
            length = int(hexList[k+2],16)*256 + int(hexList[k+3],16)
            #print length  # test
            for m in range(length-3):
                comment = comment + chr(int(hexList[k + m + 4],16))
                #print chr(int(hexList[k + m + 4],16)),  # test
                #print hexList[k + m + 4],  # test

    if len(comment) > 0:
        print comment
    else:
        print "No comment"
    '''
def imgDataURI(pathPic,picName,log):
    '''转化图片文件为 DataURI内置数据文本!
    '''
    #from base64 import b64encode
    import base64

    with open("%s/%s"%(pathPic,picName), "rb") as f:
        img = f.read()
    dataURI = base64.b64encode(img).decode()
    #log.debug("__imgDataURI:\t%s/%s"%(pathPic,picName))
    #dataURI = b64encode(open("%s/%s"%(pathPic,picName),'rb').read())
    b64file = "%s/%s.b64"%(pathPic,picName)
    open(b64file,"w").write(dataURI)
    return dataURI


def main(ov,log):
    '''默认主函式,组合响应各种参数,调用实际行为..
    log.error("错误")
    log.info("消息")
    log.debug("调试")
    log.warning("警告")
    log.info("消息2")
    '''
    global HTMTPL,DOTXT,MAPID,DOTORDER
    #--fdp 响应
    if ov.fdp:
        DOTORDER = DOFDP
    else:
        DOTORDER = DODOT
    #ov:    dotscript exptpl title expage 
    #tpl:   dotPageTitle dotPageStyle imgame mapname map4dot
    dotPageStyle = DOTCSS
    if "battery" != ov.exptpl:
        HTMTPL = open(ov.exptpl,"r").read()
    elif "battery" != ov.dotscript:
        DOTXT = open(ov.dotscript,"r").read()
        #log.debug(MAPID)
        MAPID = os.path.basename(ov.dotscript[:-4])
        #log.debug(MAPID)
    elif DEFTITLE != ov.title:
        dotPageTitle = ov.title
    else:
        # all default
        exPage = ov.expage
        mapname = MAPID
        imgname = "%s.png"%MAPID
        map4dot = "<map/>"



    gen2html(ov,log)

if __name__ == '__main__':      # this way the module can be
    '''usage::
    gen4dot2htm.py -t path/2/模板.htm -o path/2/发布.html -i '标题'
    业务参数:
        -t 页面输出模板
        -o 输出页面
        -i 页面标题
    通用参数:
        -N 试用模式:不作为,测试输出相关参数
        -D 调试模式:打印debug信息到屏幕
        -Q 安静模式:不输出任何信息
        -V 运营模式:输出 INFO|WARNING|ERROR 到sys.stderr
        --doctest TDD支持
        -v doctest 详细模式
    '''
    usage = "$python %prog [-V|N|D|Q][--dot|fdp|circo|twopi|neato][-t path/2/templete.htm] [-o path/2/export.html] [-i 'title of page'] -d path/2/foo.dot"
    parser = OptionParser(usage,version="%s {powered by Zoom.Quiet+Leo}"%VERSION)
    gRun = OptionGroup(parser, "Group for Running",
        '''DEFAULT::
    -V False    -N False    -D False    -Q False'''
        )
    gRun.add_option("-V","--verbose",metavar="",help="mod_run: export INFO|WARNING|ERROR ->sys.stderr"
        ,dest="verbose",action="store_true"
        ,default=False
        )
    gRun.add_option("-v",metavar="",help="verbose for doctest"
        ,dest="verbose_doctest",action="store_true"
        ,default=False
        )
    gRun.add_option("-N","--notdo",metavar="",help="mod_try: no realy do,export INFO"
        ,dest="mnotdo",action="store_true"
        ,default=False
        )
    gRun.add_option("-D","--debug",metavar="",help="mod_debug: export DEBUG|INFO|WARNING|ERROR ->sys.stderr"
        ,dest="mdebug",action="store_true"
        ,default=False
        )
    gRun.add_option("-Q","--quiet",metavar="",help="mod_quiet: export NULL"
        ,dest="mquiet",action="store_true"
        ,default=False
        )
    gRun.add_option("--doctest",metavar="",help="mod_test: runnin doctest"
        ,dest="tdd",action="store_true"
        ,default=False
        )
    parser.add_option_group(gRun)

    gIput = OptionGroup(parser, "Group fo Import",
        "them need realy obj.")
    gIput.add_option("-d",metavar="path/2/my.dot"
        ,dest="dotscript",nargs=1,type="string"
        ,default="battery"
        ,help="dot script file with path "
        "e.g: ../tpl/idx.dot"
        "   DEFAULT: battery"
        )
    gIput.add_option("-t","--tmplete",metavar="path/2/tpl.htm"
        ,dest="exptpl",nargs=1,type="string"
        ,default="battery"
        ,help="file name with path "
        "e.g: ../tpl/idx.htm"
        "   DEFAULT: battery"
        )
    gIput.add_option("-o","--output",metavar="path/2/page.html"
        ,dest="expage",nargs=1,type="string"
        ,default="stdout"
        ,help="templet file name with ppath "
        "e.g: ../exp/idx.html"
        "   DEFAULT: index.html"
        )
    gIput.add_option("-i","--title",metavar=""
        ,dest="title",nargs=1,type="string"
        ,default=DEFTITLE
        ,help="Page Title"
        )
    gIput.add_option("--dot",metavar=""
        ,dest="dot",action="store_true"
        ,default=False
        ,help="usage dot gen. mapping"
        "   DEFAULT:dot"
        )
    gIput.add_option("--fdp",metavar=""
        ,dest="fdp",action="store_true"
        ,default=False
        ,help="usage fdp gen. mapping"
        "   DEFAULT:dot"
        )
    gIput.add_option("--circo",metavar=""
        ,dest="circo",action="store_true"
        ,default=False
        ,help="usage circo gen. mapping"
        "   DEFAULT:dot"
        )
    gIput.add_option("--twopi",metavar=""
        ,dest="twopi",action="store_true"
        ,default=False
        ,help="usage twopi gen. mapping"
        "   DEFAULT:dot"
        )
    gIput.add_option("--neato",metavar=""
        ,dest="neato",action="store_true"
        ,default=False
        ,help="usage neato gen. mapping"
        "   DEFAULT:dot"
        )
    parser.add_option_group(gIput)
    (options, args) = parser.parse_args()
    # 检查是否没有参数
    if 1==len(sys.argv):
        parser.print_help()
    else:   
        ov = parser.values
        #初始化日志对象 todo:自动激活...
        log = zqlog(ov)
        log.info
        log.debug
        log.error
        log.warning
        # --doctest 开关
        if ov.tdd:
            log.warning(">>> running doctest")
            import doctest
            doctest.testmod(verbose=ov.verbose_doctest)
        gen2html(ov,log)

    '''
    log.info("消息")
    log.debug("调试")
    log.error("错误")
    log.warning("警告")
    '''

