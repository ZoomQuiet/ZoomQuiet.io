Title: 天然样循环
Date: 2016-05-31
Tags: pythonic,pythoneer,loop,coder
Slug: nedbat-loop-iter


[TOC]

来自 @nedbat 的分享:

[Ned Batchelder: Loop Like A Native](http://nedbatchelder.com/text/iter.html)


## 迭代基础

C样:

    i = 0
    while i < len(my_list):
        v = my_list[i]
        print v
        i += 1

偏门:

    for i in range(len(my_list)):
        v = my_list[i]
        print v


蠎样:

    for v in my_list:
        print v


模式:

    for name in iterable:
        statements


- 可 `iterable` 的对象可以生成值流
- 对迭代对象的每次操作
- 由对象决定是什么值
- Python 中太多对象可以直接迭代的...

### list ⇒ elements


    for e in [1, 2, 3, 4]:
        print e

    1
    2
    3
    4

### Strings ⇒ characters

    for c in "Hello":
        print c

    H
    e
    l
    l
    o

### Dicts ⇒ keys

    d = { 'a': 1,  'b': 2,  'c': 3 }
     
    for k in d:
        print k

    a
    c
    b


- 当然顺序是没有的
- 以及:
    + `for v in d.itervalues():`
    + `for k,v in d.iteritems():`
    + 专用形式

### Files ⇒ lines

    with open("gettysburg.txt") as f:
        for line in f:
            print repr(line)

    'Four-score and seven years ago,\n'
    'our fathers brought forth on this continent\n'
    'a new nation,\n'
    'conceived in liberty,\n'
    'and dedicated to the proposition\n'
    'that all men are created equal.\n'

### 标准库中有趣的迭代

正则表达式:

    for match in re.finditer(pattern, string):
        # once for each regex match...

文件系统:

    for root, dirs, files in os.walk('/some/dir'):
        # once for each sub-directory...

迭代工具:

    for num in itertools.count():
        # once for each integer... Infinite!

    from itertools import chain, repeat, cycle
    seq = chain(repeat(17, 3), cycle(range(4)))
    for num in seq:
        # 17, 17, 17, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, ...

### 其它的迭代形式

    new_list = list(iterable)

    results = [f(x) for x in iterable]

    total = sum(iterable)

    smallest = min(iterable)
    largest = max(iterable)

    combined = "".join(iterable)


## 基本设问


### Q: 如何获得索引号?

别:

    for i in range(len(my_list)):
        v = my_list[i]
        print i, v

赞:

    for i, v in enumerate(my_list):
        print i, v


#### enumerate() 制造好用的值对

    names = ["Eiffel Tower", "Empire State", "Sears Tower"]
    list(enumerate(names))

    [(0, 'Eiffel Tower'), 
     (1, 'Empire State'), 
     (2, 'Sears Tower')]

    for num, name in enumerate(names):
        print num, name

    0 Eiffel Tower
    1 Empire State
    2 Sears Tower

#### 迭代 vs 索引

受限:

    for i in range(len(my_list)):
        v = my_list[i]    # indexing!
        print i, v

更强:

    for i, v in enumerate(iterable):
        print i, v

    for linenum, line in enumerate(f, start=1):
        #...


C样坏形:

    i = 0
    for v in iterable:
        print i, v
        i += 1

### Q: 如何对两个列表循环?

    names = ["Eiffel Tower", "Empire State", "Sears Tower"]
    heights = [324, 381, 442]
     
    for i in range(len(names)):
        name = names[i]
        height = heights[i]
        print "%s: %s meters" % (name, height)

    Eiffel Tower: 324 meters
    Empire State: 381 meters
    Sears Tower: 442 meters


#### zip() 生成弱对关系循环

将一对循环,变成一个流循环:

    for name, height in zip(names, heights):
        print "%s: %s meters" % (name, height)

    Eiffel Tower: 324 meters
    Empire State: 381 meters
    Sears Tower: 442 meters

#### dict() 是接收一对流的

    names = ["Eiffel Tower", "Empire State", "Sears Tower"]
    heights = [324, 381, 442]
     
    dict(zip(names, heights))

    {'Empire State': 381, 
     'Sears Tower': 442, 
     'Eiffel Tower': 324}


#### 最赞

    tall_buildings = {
      "Empire State": 381, "Sears Tower": 442,
      "Burj Khalifa": 828, "Taipei 101": 509,
      }

    >>> print max(tall_buildings.values())
    828

    >>> print max(tall_buildings.items(), key=lambda b: b[1])
    ('Burj Khalifa', 828)

    >>> print max(tall_buildings, key=tall_buildings.get)
    'Burj Khalifa'


## 自制迭代

### 生成自有迭代

    nums = [88, 73, 92, 72, 40, 38, 25, 20, 90, 72]
    for n in nums:
        if n % 2 == 0:
            do_something(n)

    def evens(stream):
        them = []
        for n in stream:
            if n % 2 == 0:
                them.append(n)
        return them
     
    for n in evens(nums):
        do_something(n)

### 生成器

函式返回一个值 --> 生成器生成一个流

    def hello_world():
        yield "Hello"
        yield "world"
     
    for x in hello_world():
        print x

    Hello
    world

#### Evens generator


    def evens(stream):
        for n in stream:
            if n % 2 == 0:
                yield n

    for n in evens(nums):
        do_something(n)

#### 对迭代提炼
~ Abstracting your iteration

    f = open("my_config.ini")
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            # A comment line, skip it.
            continue
        if not line:
            # A blank line, skip it.
            continue
     
        # An interesting line.
        do_something(line)

自制生成器:

    def interesting_lines(f):
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue
            if not line:
                continue
            yield line

    with open("my_config.ini") as f:
        for line in interesting_lines(f):
            do_something(line)
     
    with open("my_other.dat") as f2:
        for line in interesting_lines(f2):
            do_something_else(line)

### Q: 如何从两层循环中退出?

    for row in range(height):
        for col in range(width):
     
            value = spreadsheet.get_value(col, row)
            do_something(value)
     
            if this_is_my_value(value):
                break   # ← ???

#### A: 合并循环

    def range_2d(width, height):
        """Produce a stream of two-D coordinates."""
        for y in range(height):
            for x in range(width):
                yield x, y

    for col, row in range_2d(width, height):
        value = spreadsheet.get_value(col, row)
        do_something(value)
     
        if this_is_my_value(value):
            break

#### Better: 单元迭代

    for cell in spreadsheet.cells():
        value = cell.get_value()
        do_something(value)
     
        if this_is_my_value(value):
            break


## 底层迭代

- 可迭代: 能生成迭代 Iterable: produces an iterator
- 迭代器: 生成一个值流 Iterator: produces a stream of values

    iterator = iter(iterable)  # iterable.__iter__()
    value = next(iterator)     # iterator.next() or .__next__()
    value = next(iterator)
    ...

迭代器仅有一个操作: `next()`


### 迭代基层操作

有时很有用:

    with open("blah.dat") as f:
        # Read the first line
        header_line = next(f)
     
        # Read the rest
        for data_line in f:
            # ...

### 构造自制对象可迭代

    class ToDoList(object):
        def __init__(self):
            self.tasks = []
     
        def __iter__(self):
            return iter(self.tasks)

    todo = ToDoList()
    ...
    for task in todo:
        # ...


- 仅仅需要定义 `__iter__()`

#### __iter__ 生成器

    class ToDoList(object):
        def __init__(self):
            self.tasks = []
     
        def __iter__(self):
            for task in self.tasks:
                if not task.done:
                    yield task
     
        def all(self):
            return iter(self.tasks)
     
        def done(self):
            return (t for t in self.tasks if t.done)


## (￣▽￣)

- 迭代无处不在
- Python 内置了干净强大的模型支持迭代
- 抽象和定制你的迭代吧!





## 是也乎

- 160613 空先发
- 160531 动念
