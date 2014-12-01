Title: 十大早该知道的Python技巧
Date: 2014-11-26
Tags: Pythonic,FW,idioms,tutorial
Slug: top10-Py-idioms-wish-learned-earlier


原文: [prooffreader plus: Top 10 Python idioms I wish I'd learned earlier](http://prooffreaderplus.blogspot.ca/2014/11/top-10-python-idioms-i-wished-id.html)

`Top 10 Python idioms I wish I'd learned earlier`

 
I've been programming all my life, but never been a programmer. Most of my work was done in Visual Basic because it's what I was most comfortable with, plus a smattering of other languages (R, C, JavaScript, etc... Pascal, Applescript, Hypertext and BASIC, which I learned in 1979, if you go far back enough). A couple of years ago, I decided to use Python exclusively so that I could improve my coding. I ended up re-inventing many wheels -- which I didn't mind too much, because I enjoy solving puzzles. But sometimes it's good to have a more efficient, Pythonesque approach, and time after time I found myself having "aha!" moments, realizing I'd been doing things the hard, excessively verbose way for no reason. Here is a list of ten Python idioms that would have made my life much easier if I'd thought to search for them early on.
 
Missing from this list are some idioms such as list comprehensions and lambda functions, which are very Pythonesque and very efficient and very cool, but also very difficult to miss because they're mentioned on StackOverflow every other answer! Also ternary x if y else z constructions, decorators and generators, because I don't use them very often.
 
There's also an 
[IPython notebook nbviewer version](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/top_10_python_idioms.ipynb) of this document if you prefer.

 
## 1. Python 3-style printing in Python 2

One of the things that kept me from concentrating on Python was this whole version 2 - version 3 debacle. Finally I went with Python 2 because all the libraries I wanted were not 3-compatible, and I figured if I needed to, I would laboriously adjust my code later. 
 
But really, the biggest differences in everyday programming are printing and division, and now I just import from future. Now that almost all the libraries I use heavily are v3-compliant, I'll make the switch soon.

```
mynumber = 5

print "Python 2:"
print "The number is %d" % (mynumber)
print mynumber / 2,
print mynumber // 2

from __future__ import print_function
from __future__ import division

print('\nPython 3:')
print("The number is {}".format(mynumber))
print(mynumber / 2, end=' ')
print(mynumber // 2)
```


    Python 2:
    The number is 5
    2 2

    Python 3:
    The number is 5
    2.5 2

Oh, and here's an easter egg for C programmers:
```
from __future__ import braces
  File "<ipython-input-3-2aebb3fc8ecf>", line 1
    from __future__ import braces
SyntaxError: not a chance
```


## 2. enumerate(list)

It might seem obvious that you should be able to iterate over a list and its index at the same time, but I used counter variables or slices for an embarrassingly long time.
```
mylist = ["It's", 'only', 'a', 'model']

for index, item in enumerate(mylist):
    print(index, item)
```


    0 It's
    1 only
    2 a
    3 model

## 3. Chained comparison operators

Because I was so used to statically typed languages (where this idiom would be ambiguous), it never occurred to me to put two operators in the same expression. In many languages, 4 > 3 > 2 would return as False, because (4 > 3) would be evaluated as a boolean, and then True > 2 would be evaluated as False.

```
mynumber = 3

if 4 > mynumber > 2:
    print("Chained comparison operators work! \n" * 3)
```

    Chained comparison operators work! 
    Chained comparison operators work! 
    Chained comparison operators work! 


## 4. collections.Counter

The collections library is, like, the best thing ever. Stackoverflow turned me on to ordered dicts early on, but I kept using a snippet to create dicts to count occurrences of results in my code. One of these days, I'll figure out a use for collections.deque.

```
from collections import Counter
from random import randrange
import pprint
mycounter = Counter()
for i in range(100):
    random_number = randrange(10)
    mycounter[random_number] += 1
for i in range(10):
    print(i, mycounter[i])
```

    0 10
    1 10
    2 13
    3 6
    4 6
    5 11
    6 10
    7 14
    8 12
    9 8

## 5. Dict comprehensions

A rite of passage for a Python programmer is understanding list comprehensions, but eventually I realized dict comprehensions are just as useful -- especially for reversing dicts.

```
my_phrase = ["No", "one", "expects", "the", "Spanish", "Inquisition"]
my_dict = {key: value for value, key in enumerate(my_phrase)}
print(my_dict)
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)
```

    {'Inquisition': 5, 'No': 0, 'expects': 2, 'one': 1, 'Spanish': 4, 'the': 3}
    {0: 'No', 1: 'one', 2: 'expects', 3: 'the', 4: 'Spanish', 5: 'Inquisition'}

## 6. Executing shell commands with subprocess

I used to use the os library exclusively to manipulate files; now I can even programmatically call complex command-line tools like ffmpeg for video editing
 
(And yes, I use Windows, so do all of my clients. But I have the good grace to be embarrassed about it!)
 
Note that the particular subprocess I picked would be much better done with the os library; I just wanted a command everyone would be familiar with. And in general, shell=True is a VERY bad idea, I put it here so that the command output would appear in the IPython notebook cell. Don't try this at home, kids!

```
import subprocess
output = subprocess.check_output('dir', shell=True)
print(output)
 Volume in drive C is OS
 Volume Serial Number is [REDACTED]
 Directory of C:\Users\David\Documents\[REDACTED]
```

    2014-11-26  06:04 AM    <DIR>          .
    2014-11-26  06:04 AM    <DIR>          ..
    2014-11-23  11:47 AM    <DIR>          .git
    2014-11-26  06:06 AM    <DIR>          .ipynb_checkpoints
    2014-11-23  08:59 AM    <DIR>          CCCma
    2014-09-03  06:58 AM            19,450 colorbrewdict.py
    2014-09-03  06:58 AM            92,175 imagecompare.ipynb
    2014-11-23  08:41 AM    <DIR>          Japan_Earthquakes
    2014-09-03  06:58 AM             1,100 LICENSE
    2014-09-03  06:58 AM             5,263 monty_monte.ipynb
    2014-09-03  06:58 AM            31,082 pocket_tumblr_reddit_api.ipynb
    2014-11-26  06:04 AM             3,211 README.md
    2014-11-26  06:14 AM            19,898 top_10_python_idioms.ipynb
    2014-09-03  06:58 AM             5,813 tree_convert_mega_to_gexf.ipynb
    2014-09-03  06:58 AM             5,453 tree_convert_mega_to_json.ipynb
    2014-09-03  06:58 AM             1,211 tree_convert_newick_to_json.py
    2014-09-03  06:58 AM            55,970 weather_ML.ipynb
                  11 File(s)        240,626 bytes
                   6 Dir(s)  180,880,490,496 bytes free


## 7. dict .get() and .iteritems() methods

Having a default value when a key does not exist has all kinds of uses, and just like enumerate() for lists, you can iterate over key, value tuples in dicts
 
```
my_dict = {'name': 'Lancelot', 'quest': 'Holy Grail', 'favourite_color': 'blue'}

print(my_dict.get('airspeed velocity of an unladen swallow', 'African or European?\n'))

for key, value in my_dict.iteritems():
    print(key, value, sep=": ")
```

    African or European?

    quest: Holy Grail
    name: Lancelot
    favourite_color: blue

## 8. Tuple unpacking for switching variables

Do you know how many times I had to use a third, temporary dummy variable in VB? c = a; a = b; b = c?

```
a = 'Spam'
b = 'Eggs'

print(a, b)

a, b = b, a

print(a, b)
```

    Spam Eggs
    Eggs Spam

## 9. Introspection tools

I was aware of dir(), but I had assumed help() would do the same thing as IPython's ? magic command. It does way more. (This post has been updated after some great advice from reddit's /r/python which, indeed, I wish I'd known about before!)

```
my_dict = {'That': 'an ex-parrot!'}
    
help(my_dict)
```
Help on dict object:

```
class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __cmp__(...)
 |      x.__cmp__(y) <==> cmp(x,y)
 |  
 |  __contains__(...)
 |      D.__contains__(k) -> True if D has a key k, else False
 |  
 |  __delitem__(...)
 |      x.__delitem__(y) <==> del x[y]
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 
[TRUNCATED FOR SPACE]

 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
 |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
 |      In either case, this is followed by: for k in F: D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> list of D's values
 |  
 |  viewitems(...)
 |      D.viewitems() -> a set-like object providing a view on D's items
 |  
 |  viewkeys(...)
 |      D.viewkeys() -> a set-like object providing a view on D's keys
 |  
 |  viewvalues(...)
 |      D.viewvalues() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
 |  
 |  __new__ = 
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
```


## 10. PEP-8 compliant string chaining

[PEP8](https://www.python.org/dev/peps/pep-0008)
is the style guide for Python code. Among other things, it directs that lines not be over 80 characters long and that indenting by consistent over line breaks.
 
This can be accomplished with a combination of backslashes \; parentheses () with commas , ; and addition operators +; but every one of these solutions is awkward for multiline strings. There is a multiline string signifier, the triple quote, but it does not allow consistent indenting over line breaks. 
 
There is a solution: parentheses without commas. I don't know why this works, but I'm glad it does.

```
my_long_text = ("We are no longer the knights who say Ni! "
                "We are now the knights who say ekki-ekki-"
                "ekki-p'tang-zoom-boing-z'nourrwringmm!")
print(my_long_text)
```

We are no longer the knights who say Ni! We are now the knights who say ekki-ekki-ekki-p'tang-zoom-boing-z'nourrwringmm!



## 是也乎

## Changelog

- 141130 move into Pelican as zoomquiet.io
