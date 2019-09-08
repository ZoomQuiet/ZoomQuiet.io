Title: 为毛俺不担心所谓Python用户流失
Date: 2014-07-11
Tags: BRETT,Leo,PyConChina,Zh
Slug: why-i-dont-worry-about-pythons-popularity


## Why I don't worry about Python losing users

I just had a need to read two files that were line-delimited lists of domains, consolidate the data, and then output the domains sorted and all lowercased to a new file. It took me 10 lines of Python code and worked perfectly on the first try.

Out of curiosity and to make sure I keep learning Go (my team at work uses it whenever possible), I decided to re-implement the same functionality. That took 
[56 lines in Go](https://gist.github.com/brettcannon/a2a37cc5aadbc91c02ad)
. When I went back and refactored the Python code to match the abstractions I used in the Go code it grew to 
[17 lines](https://gist.github.com/brettcannon/82c4fe68bac30f4ed653)
.


And this sort of thing is exactly why I do not worry about Python's popularity (at least in terms of users). While languages like Go compete with Python on a performance:productivity comparison, when you compare Python to almost any other language based purely on productivity it trounces the competition. And this shouldn't shock anyone when you think about the history of Python. The language was initially created to script 
[a distributed operating system](http://en.wikipedia.org/wiki/Amoeba_(operating_system))
. This is why in the '90s and early 2000s the comparison was always Python vs. Perl and then Python vs. Ruby. Only in the 2000s and later did Python get compared to Java or very recently to Go or JavaScript.

And this productivity view of Python also ties into education. With 
[Python now the most popular intro teaching language at the top U.S. universities](http://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-us-universities/fulltext)
, many people are learning how to program using Python. But exposure early on to a language does not guarantee future usage by someone; I for one did not use Scheme after my intro course. But because Python is such a productive language, the language becomes a staple in one's toolkit of programming. If people learn Python first, then when they need to write a quick script like I did today they will most likely reach for Python than Java or Go or some other language they may be using for their work.

All of this is why I don't worry about Python's demise due to lack of users. People might switch to Go at work because the performance:productivity ratio is very good for their project or team. Or maybe people got frustrated with the Python 2/3 transition and didn't want to base their project at work on Python anymore. It really doesn't matter in terms of the number of users of Python because I'm willing to bet those people still reach for Python when they need a one-off script to solve a problem. And I bet these people still recommend Python when they are asked what people's first programming language should be. In other words I don't worry about our great-for-teaching, highly productive scripting language ever lacking users; Python will always be useful.



## Changelog

- 161203 是也乎,(￣▽￣)
    + 发现没有必要全文翻译,观点很清晰
    + 就生产力方面,当前世界无出其右
    + 嘦是人类创建的软件工程,必然有一个很长时期的混乱期
    + 这个期间,临时的/一次性的 检验/验证/实验性 脚本是必须的
    + 那么通用的 Python 语言简直是无法放弃的
- 140728 从周刊中发现,决定翻译
