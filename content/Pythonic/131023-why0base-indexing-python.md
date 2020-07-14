Title: Python 列表为毛从0开始索引?
Date: 2019-03-23
Tags: guido,python,gplus
Slug: 131023-why0base-indexing-python


[TOC]


[I was asked on Twitter why Python uses 0\-based indexing,...](https://plus.google.com/115212051037621986145/posts/YTUxbXYZyfi)

老爹当年也很是积累使用 G+ 的,
公开回答了很多价值问题...
能看一眼少一眼了...


## 背景

>>> Google+ 帐号将于 2019 年 4 月 2 日关停. 下载 Google+ 内容可能需要一些时间,因此请在 2019 年 3 月 31 日之前开始下载. 

## 发现
> Guido van Rossum
>> 公开
>>> 2013年10月23日

I was asked on Twitter why Python uses 0-based indexing, with a link to a new (fascinating) post on the subject (http://exple.tive.org/blarg/2013/10/22/citation-needed/). I recall thinking about it a lot; ABC, one of Python's predecessors, used 1-based indexing, while C, the other big influence, used 0-based. My first few programming languages (Algol, Fortran, Pascal) used 1-based or variable-based. I think that one of the issues that helped me decide was slice notation.

Let's first look at use cases. Probably the most common use cases for slicing are "get the first n items" and "get the next n items starting at i" (the first is a special case of that for i == the first index). It would be nice if both of these could be expressed as without awkward +1 or -1 compensations.

Using 0-based indexing, half-open intervals, and suitable defaults (as Python ended up having), they are beautiful: a[:n] and a[i:i+n]; the former is long for a[0:n].

Using 1-based indexing, if you want a[:n] to mean the first n elements, you either have to use closed intervals or you can use a slice notation that uses start and length as the slice parameters. Using half-open intervals just isn't very elegant when combined with 1-based indexing. Using closed intervals, you'd have to write a[i:i+n-1] for the n items starting at i. So perhaps using the slice length would be more elegant with 1-based indexing? Then you could write a[i:n]. And this is in fact what ABC did -- it used a different notation so you could write a@i|n.(See http://homepages.cwi.nl/~steven/abc/qr.html#EXPRESSIONS.)

But how does the index:length convention work out for other use cases? TBH this is where my memory gets fuzzy, but I think I was swayed by the elegance of half-open intervals. Especially the invariant that when two slices are adjacent, the first slice's end index is the second slice's start index is just too beautiful to ignore. For example, suppose you split a string into three parts at indices i and j -- the parts would be a[:i], a[i:j], and a[j:].

So that's why Python uses 0-based indexing.

## 是也乎

> 简单说, 就是为了切片时的语义合理性...
