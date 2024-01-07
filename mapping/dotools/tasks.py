#!/usr/bin/env python
# -*- coding: utf-8 -*-

from invoke import task, call, Responder, Collection
import os
import shutil


VERSION = "19.4.17"
DOTPATH = "../dot"
PUBPTH = "../public"

@task()
def gen2dot(s, week):
    '''
    generate png. map from dot
    '''
    print("\n-------------------------------")
    src = "../dot/map101camp1py_ch{}".format(week)
    cmd = "dot -Tjpeg {}.dot -o {}.png -Tcmapx -o {}.map".format(src, src, src)
    print(cmd)
    s.run(cmd)


@task()
def gen2dot2py(s):
    '''
    generate png. map from dot
    '''
    print("\n-------------------------------")
    src = "../dot/map101camp2py"
    cmd = "dot -Tjpeg {}.dot -o {}.png -Tcmapx -o {}.map".format(src, src, src)
    print(cmd)
    s.run(cmd)


@task
def gen2html2py(s):
    '''
    generate html
    '''
    src_dir = "../dot/"
    src_base = src_dir + "map101camp2py"

    cmd = 'python gen2htm4io101camp.py ' \
          '-t tpl_idx.htm -i ' \
          '"py.101.camp -mapping" ' \
          '-d {}.dot ' \
          '-o {}.html'.format( src_base, src_base)
    print(cmd)
    s.run(cmd)

@task
def gen2html(s, week):
    '''
    generate html
    '''
    src_dir = "../dot/"
    src_base = src_dir + "map101camp1py_ch{}".format(week)

    cmd = 'python gen2htm4io101camp.py ' \
          '-t tpl_idx.htm -i ' \
          '"py.101.camp ch{}-mapping" ' \
          '-d {}.dot ' \
          '-o {}.html'.format(week, src_base, src_base)
    print(cmd)
    s.run(cmd)

@task
def _copy2pub(s, week):
    '''copy files to public
    '''
    course = "map101camp1py_ch{}".format(week)

    shutil.copyfile(os.path.join(DOTPATH, course+".dot"),
                    os.path.join(PUBPTH, course + ".dot"))
    shutil.copyfile(os.path.join(DOTPATH, course+".html"),
                    os.path.join(PUBPTH, course + ".html"))
    shutil.copyfile(os.path.join(DOTPATH, course+".html"),
                    os.path.join(PUBPTH, "index.html"))
