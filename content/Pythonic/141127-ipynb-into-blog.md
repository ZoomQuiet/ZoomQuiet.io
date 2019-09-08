Title: 如何将 ipynb 发布到 blog 中?
Date: 2014-11-27
Tags: Pythonic,FW,ipynb,tutorial
Slug: 141127-ipynb-into-blog


原文: [prooffreader plus: How to quickly turn an IPython notebook into a blog post](http://prooffreaderplus.blogspot.ca/2014/11/how-to-quickly-turn-ipython-notebook.html)

IPython notebooks are great for many things, but they're a little awkward to embed in blog post platforms like Blogger, Wordpress, etc. When the nbconvert feature was a standalone command-line tool, there was a blog export template, but that seems to have disappeared now that nbconvert has been folded within IPython.

Out of the box, nbconvert just has two html export options:

    --html

which includes a lot of CSS that interferes with a blog's CSS, and:

    --html --template basic

which has no CSS and so pretty much negates the benefit of using an IPython notebook. However, it does have CSS classess in the text.

My solution was to whip up a quick CSS stylesheet that could be included in the blog post. It seems to work pretty well; you can have a look at:

- an [IPython notebook in nbviewer](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/top_10_python_idioms.ipynb) of a recent blog post of mine
- the [blog version](http://prooffreaderplus.blogspot.ca/2014/11/top-10-python-idioms-i-wished-id.html) after applying this stylesheet.

Note that, for aesthetic reasons, I removed all the

    In [1]

-style tags because of the narrow columns on this blog. Your mileage may vary.


## 1. Convert .ipynb notebook to HTML

In the terminal, navigate to the folder containing the .ipynb file and type:

    ipython nbconvert --to html --template basic filename.ipynb

## 2. Paste HTML in blog

Note: if you're using the Blogger platform, never switch back to the Compose interface after you use the HTML interface, it changes all your tags.

## 3. Add CSS to blog HTML

This seems to reproduce the native syntax highlighting of IPython.

```
<style type="text/css">
.highlight{background: #f8f8f8; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .1em;padding:0em .5em;border-radius: 4px;}
.k{color: #338822; font-weight: bold;}
.kn{color: #338822; font-weight: bold;}
.mi{color: #000000;}
.o{color: #000000;}
.ow{color: #BA22FF;  font-weight: bold;}
.nb{color: #338822;}
.n{color: #000000;}
.s{color: #cc2222;}
.se{color: #cc2222; font-weight: bold;}
.si{color: #C06688; font-weight: bold;}
.nn{color: #4D00FF; font-weight: bold;}
</style>
```

## 是也乎
原来... `IPy[:] notebook` 天然就内置了这种能力!

## Changelog

- 160322 @TANG ZhiXiong 提醒:
    + 其实放在 GitHub,然后分享一个 Jupyter 链接是最好的
    + `是也乎` 这的确是 2015-7 之后更好的解决方案了 ;-)
- 140107 move into Pelican as zoomquiet.io
- 131106 pub. [EKR to Chinese programmer — I. M. H. O. — Medium](https://medium.com/i-m-h-o/9520fee0b59f)
