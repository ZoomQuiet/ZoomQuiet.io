Title: How to install Leo under M1 chip macOS 12.*
Date: 2022-05-29
Tags: python,howto,leo,install
Slug: leo-install-m1mac-summary


[TOC]


## Background
base [Installing Leo — Leo 6\.6\.2 documentation](http://leoeditor.com/installing.html#installing-leo-on-macos-10-7-lion-and-later) 
can not installing Leo on MacOs 12.4 with M1max chip:


![screenfetch](https://ipic.zoomquiet.top/2022-05-29-220529-screenfetch.jpg)

## Upgrade
> only for M1 chip Mac Book Pro

base ARM support Homebrew, check version:


    $ abrew --version
    Homebrew 3.4.11
    Homebrew/homebrew-core (git revision b8f03171990; last commit 2022-05-27)
    Homebrew/homebrew-cask (git revision 7cd05aa248; last commit 2022-05-27)

> PS: 

base alias for Intel and ARM verions (`~/.bash_profile`):

    alias abrew='/opt/homebrew/bin/brew '
    alias ibrew='/usr/local/bin/brew '


install moniconda:

    $ abrew install miniconda

initialization it:

    $ conda init bash

SEE: [Deep dive: conda init and activate — conda 4\.13\.0\.post1\+0adcd595 documentation](https://docs.conda.io/projects/conda/en/latest/dev-guide/deep-dive-activation.html)

will `~/.bash_profile` fund like:

    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    __conda_setup="$('/opt/homebrew/Caskroom/miniconda/base/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
    else
        if [ -f "/opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh" ]; then
            . "/opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh"
        else
            export PATH="/opt/homebrew/Caskroom/miniconda/base/bin:$PATH"
        fi
    fi
    unset __conda_setup
    # <<< conda initialize <<<


install PyQt:

    $ abrew install PyQt@5

base `conda info` check miniconda is working;
and create Leo special environment:

    $ conda create  -n leo3912 python=3.9.12

check result:

    $ conda env list
    conda env list
    /opt/homebrew/Caskroom/miniconda/base/lib/python3.9/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils.
      warnings.warn("Setuptools is replacing distutils.")
    # conda environments:
    #
    base                  *  /opt/homebrew/Caskroom/miniconda/base
    leo3912                  /opt/homebrew/Caskroom/miniconda/base/envs/leo3912


copy PyQt packets from brew to miniconda:

such as:
    + from `/opt/homebrew/Cellar/pyqt@5/5.15.6/lib/python3.9/site-packages/` 
    + to `/opt/homebrew/Caskroom/miniconda/base/envs/leo3912/lib/python3.9/site-packages/`

need all of them:

    PyQt3D-5.15.5.dist-info
    PyQt5
    PyQt5-5.15.6.dist-info
    PyQt5_sip-12.9.0-py3.9.egg-info
    PyQtChart-5.15.5.dist-info
    PyQtDataVisualization-5.15.5.dist-info
    PyQtNetworkAuth-5.15.5.dist-info
    PyQtPurchasing-5.15.5.dist-info


and download Leo Source code release from [Latest](https://github.com/leo-editor/leo-editor/releases/latest) 

deploy into right path, such as `/opt/bin/leo`

and into conda environment install leo:

    $ conda activate leo3912
    $ pip install leo

will got some error, but is ok, can suto install these:

- Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.1 alabaster-0.7.12 astroid-2.11.5 attrs-21.4.0 babel-2.10.1 dialite-0.5.3 dill-0.3.5.1 docutils-0.17.1 fastjsonschema-2.15.3 flexx-0.8.4 future-0.18.2 imagesize-1.3.0 importlib-metadata-4.11.4 isort-5.10.1 jsonschema-4.5.1 jupyter-core-4.10.0 lazy-object-proxy-1.7.1 leo-5.9 mccabe-0.7.0 nbformat-5.4.0 platformdirs-2.5.2 pscript-0.7.7 pyflakes-2.4.0 pylint-2.13.9 pyrsistent-0.18.1 pytz-2022.1 six-1.16.0 snowballstemmer-2.2.0 sphinx-4.5.0 sphinxcontrib-applehelp-1.0.2 sphinxcontrib-devhelp-1.0.2 sphinxcontrib-htmlhelp-2.0.0 sphinxcontrib-jsmath-1.0.1 sphinxcontrib-qthelp-1.0.3 sphinxcontrib-serializinghtml-1.1.5 tomli-2.0.1 tornado-6.1 traitlets-5.2.1.post0 typing-extensions-4.2.0 webruntime-0.5.8 wrapt-1.14.1 zipp-3.8.0

notice: for some reason, installed is leo-5.9, one old verion;
so means , 
now under conda environment need can call leo with hand deploy verion:

```
(conda: leo3912)
$ python /opt/bin/leo/launchLeo.py

setting leoID from os.getenv('USER'): 'zoomq'
PYLINTHOME is now '/Users/zoomq/Library/Caches/pylint' but obsolescent '/Users/zoomq/.pylint.d' is found; you can safely remove the latter
duplicate, (not conflicting) key bindings in myLeoSettings.leo
all    Alt+) move-past-close
all    Alt+) move-past-close
duplicate, (not conflicting) key bindings in myLeoSettings.leo
all    Alt+} forward-paragraph
all    Alt+} forward-paragraph-extend-selection
duplicate, (not conflicting) key bindings in myLeoSettings.leo
all    Ctrl+( add-comments
all    Ctrl+( add-comments
duplicate, (not conflicting) key bindings in myLeoSettings.leo
all    Ctrl+) delete-comments
all    Ctrl+) delete-comments
all    Ctrl+) delete-comments
duplicate, (not conflicting) key bindings in myLeoSettings.leo
all    Ctrl+{ promote
all    Ctrl+{ promote
duplicate, (not conflicting) key bindings in myLeoSettings.leo
all    Ctrl+} demote
all    Ctrl+} demote
Leo 6.6.2
Python 3.9.12, PyQt version 5.15.3
darwin

...

```


![Leo 6.6.2](https://ipic.zoomquiet.top/2022-05-29-zshot%202022-05-29%2022.10.10-1.jpg)


suggest define alias for daily, 
`~/.bash_profile` add:

    alias leo6lanch="python /opt/bin/leo/launchLeo.py >> /dev/null 2>&1 &"


finally start-up leo need two commands:

    $ conda activate leo3912
    $ leo6lanch


## Summary
> only for macOS 12.* with M1 chip


- base installed arm Homebrew, and miniconda
- usage brew install Qt and PyQt
- usage conda create environment for Leo
- ATTENTION:
    + copy PyQt packets from brew to conda an first
    + so usage pip install leo in auto
- download latest Leo from github
- finally from conda environment's Python call the `launchLeo.py`


## logging

- 220529 publish as blog
- 220528 miniconda + abrew can work
- 220527 error mix, had to try again
- 220506 try again, not fix yet
- 220401 try re-install PyENV, not work
- 211113 jump into M1max , fund some chaos








