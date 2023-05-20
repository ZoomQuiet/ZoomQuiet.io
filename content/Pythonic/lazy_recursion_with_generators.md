Title: 带生成器的惰性递归
Date: 2023-03-22
Tags: pythonic,python,translation
Slug: lazy_recursion_with_generators


[TOC]


## background

原文: [Lazy recursion, with generators](https://tushar.lol/post/recursive-generators/)

来自 [蠎周刊 PyCoder 569 ~蠎周刊 ~汇集全球蠎事儿 ;-)](https://weekly.pychina.org/issue/issue-569.html) 的推荐


## 快译

此文, 准备研究 Python 的生成器,
并用之来也又和并递归代码的内存使用;


### 当代码调用自己时
> When the code calls itself

你知道什么是递归;
就是函数调用自己,
如果要复习一下, 先看个示例:


```python
def factorial(n):
    # base case
    if n == 1:
        return 1

    # recurse
    return n * factorial(n-1)
```

要理解调用自身是如何工作的,
这是 factorial(5) 过程分解:

```python
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1
= 120
```

1 的值来自 factorial(1),
然后返回调用栈时继续乘以 2,3 等等;


### 何必呢?
> Why bother?

以上递归当然可以宑成 for 循环:

```python
def factorial(n):
    product = 1
    for i in range(2, n+1):
        product = product * i

    return product
```

那为什么要费心写成递归呢?

事实上, 某些逻辑本质上就是递归的;
一个很好的实例就是打印出文件夹中所有路径,
就象 find 指令作的那样;
这是我一个项目中相关代码:

```shell
$ find ./src
./src
./src/pylox
./src/pylox/tokens.py
./src/pylox/utils
./src/pylox/utils/__init__.py
./src/pylox/utils/visitor.py
./src/pylox/utils/ast_printer.py
./src/pylox/__init__.py
./src/pylox/lexer.py
./src/pylox/__main__.py
./src/pylox/expr.py
./src/pylox/py.typed
./src/pylox/parser.py

```

find 工作原理相当简单;
以下是把不即出文件夹所有内容的流程:

- 打印文件夹路径
- 获得文件夹中所有东西
- 对于文件夹中每个项目:
    - 如果是个文件, 就打印出文件的路径
    - 我哪来就是文件夹, 打印出这个子文件夹中的所有内容

请注意, 最后一条指令(打印子文件夹中的所有内容)
只是原始任务的一小部分;
递归就非常适合此类任务;

### 编程时间
> Time to code

让我们将这些指令转化为代码;
将使用一个假设的文件结构进行检验;

模拟以下树形结构:

```shell
$ tree /
/
├── etc
│   ├── passwd
│   └── shadow
└── usr
    ├── bin
    │   ├── cat
    │   └── ls
    └── lib
        ├── my_lib
        └── gcc
            └── x86_64-linux-gnu
```

Python 代码的话:

```python
file_tree = ['', [
    ['etc', ['passwd', 'shadow']],
    ['usr', [
        ['bin', ['cat', 'ls']],
        ['lib', [
            'my_lib',
            ['gcc', ['x86_64-linux-gnu']]
        ]]
    ]]
]]

def print_paths_recursive(folder, path=()):
    name, contents = folder
    path = (*path, name)

    print('/'.join(path))

    for item in contents:
        if isinstance(item, str):
            # This is a file, print out its path
            print('/'.join((*path, item)))
        else:
            # This is a folder, recurse
            print_paths_recursive(item, path)

print_paths_recursive(file_tree)
```

以及输出:

```shell
$ python find.py

/etc
/etc/passwd
/etc/shadow
/usr
/usr/bin
/usr/bin/cat
/usr/bin/ls
/usr/lib
/usr/lib/my_lib
/usr/lib/gcc
/usr/lib/gcc/x86_64-linux-gnu
Fairly straightforward.
```

转折点来了:
你会如何让这个函数返回所有路径呢?

### 递归和集合
> Recursion and collection


浰不编写递归代码来收集一些数据是很常见的;
必须收集所有文件大又得那而不是将其打印出来就是一个明显的实例;

为此,我们嘦进行相当小的更改:


该函数现在将返回路径列表;
这是递归的一个重要区别,
因为,函数之前没有返回任何东西;
我们将追加到路径列表, 而不是打印出内容;
这就将接收子路径作为返回值,
而不是仅仅进行递归调用,
并将所有返回追加到最终答案数据集中;

这是修改后的代码:

```python

def get_paths_recursive(folder, path=()):
    paths = []

    name, contents = folder
    path = (*path, name)

    paths.append('/'.join(path))

    for item in contents:
        if isinstance(item, str):
            # This is a file, append its path
            paths.append('/'.join((*path, item)))
        else:
            # This is a folder, recurse and append all subpaths
            for subpath in get_paths_recursive(item, path):
                paths.append(subpath)

    return paths

paths = get_paths_recursive(file_tree)
print(paths)
```

输出:


```shell


$ python find.py

['', '/etc', '/etc/passwd', '/etc/shadow', '/usr', '/usr/bin',
'/usr/bin/cat', '/usr/bin/ls', '/usr/lib', '/usr/lib/my_lib',
'/usr/lib/gcc', '/usr/lib/gcc/x86_64-linux-gnu']
```

### 问题来了
> The problem


如果收集很多文件夹, 问题就出现了;
如果你的目录中有数千或是数百万个文件和文件夹,
将所有文件和文件夹存储在一个列表中, 
可能就很麻烦, 原因有两个:

- 你的内存使用会随机飊升;列表可以增长到多大是没有限制的,因此,从技术上讲, 你甚至可能耗尽内存;
- 如果你只关心文件中的几个项目,那你就不走运了 --- 算法会找出每个子文件夹,然后,你才能对结果数据作些其它事儿;

本质上,这是种急性评估的算法;
避免存储所有数据的唯一方法就是直接在函数内部执行任务,
就像我们在直接打印时作的那样;
但是, 这又强烈的将我们的代码和业务进行了耦合;


### 解决方案
> The solution

所以,总结一下我们的问题:
我们想要对任意文件路径运行任意需要的执行任何代码;

任务可能是将其打印出来,又或是将其存储到列表中或是其它:


```python
def get_paths_recursive(folder, path=()):
    name, contents = folder
    path = (*path, name)

    ## Do something with the `path` here,
    ## Example: print(path), or paths.append(path)

    for item in contents:
        if isinstance(item, str):
            ## Do something with the `path + item` here...
        else:
            for subpath in get_paths_recursive(item, path):
                ## Do something with the `subpath` here...

    return paths
```

Python 已经为我们提供了一个非常强大的结构来解决这一问题,
就是生成器;

可以可能在其它一些上下文中听说过生成器,
例如:

```python
def gen():
    yield 10
    yield 20
    yield 10

for item in gen():
    print('Got:', item)

# Got: 10
# Got: 20
# Got: 10
```

但是, 关于生成器有一个鲜为人知的事实:
人家可以在代码中两点间移动你的 evaluation;

我的意思是这样的:


```python
def gen():
    print("Start!")
    yield 1

    print("Now we're calculating stuff in gen()")
    value = sum(range(10))
    yield value

    print("Last value!")
    yield 42
    print("Done.")


for item in gen():
    print(f"Doing things with {item}...")
```

你可以看到执行是如何在 gen() 和 for 循环间来回进行的:


```shell

$ py a.py
Start!
Doing things with 1...
Now we're calculating stuff in gen()
Doing things with 45...
Last value!
Doing things with 42...
Done.
```

这正是我们在本例中需要的:
每当我们有新路径时, 我们都需要执行上下文返回给主代码;
所以, 我们可以将生成器的控制权交给循环:

```python
def get_paths_generator(folder, path=()):
    name, contents = folder
    path = (*path, name)

    yield '/'.join(path)

    for item in contents:
        if isinstance(item, str):
            yield '/'.join((*path, item))
        else:
            for subpath in get_paths_generator(item, path):
                yield subpath
```

现在, 最好的部分来了,
我们可以创建原始用例, 打印和储存列表都很容易:



```shell
$ python -i find.py
>>> for path in get_paths_generator(file_tree):
...     print(path)

/etc
/etc/passwd
/etc/shadow
/usr
/usr/bin
/usr/bin/cat
/usr/bin/ls
/usr/lib
/usr/lib/my_lib
/usr/lib/gcc
/usr/lib/gcc/x86_64-linux-gnu

>>> list(get_paths_generator(file_tree))
['', '/etc', '/etc/passwd', '/etc/shadow', '/usr', '/usr/bin',
'/usr/bin/cat', '/usr/bin/ls', '/usr/lib', '/usr/lib/my_lib',
'/usr/lib/gcc', '/usr/lib/gcc/x86_64-linux-gnu']
```

这种解决方案要灵活的多,
并且, 永远不会像原先方案那样出现急切求值问题;


### 奖励: yield from
> Bonus: yield from

原先使用 append 来存储路径的代码可以进行一儿改进:
你可以使用 list.extend, 而不是编写一个 for 循环来逐一追加每个子路径:


```python
    # ...
    for item in contents:
        if isinstance(item, str):
            paths.append('/'.join((*path, item)))
        else:
            ## REPLACING THIS LOOP:
            # for subpath in get_paths_recursive(item, path):
            #     paths.append(subpath)
            paths.extend(get_paths_recursive(item, path))

```
两样的事儿, 可以在我们的生成器解决方案中完成, 
使用 yield from gen():


```python
def get_paths_generator(folder, path=()):
    name, contents = folder
    path = (*path, name)

    yield '/'.join(path)

    for item in contents:
        if isinstance(item, str):
            yield '/'.join((*path, item))
        else:
            yield from get_paths_generator(item, path)
```

yield from 将产另外一个生成器中所有的值, 一个接一个;

### 脚注
> Footer

以上, 希望你发现使用生成器来改进 Python 中新(和旧)递归代码;
另外, James Powell 有过一个很给力的演讲:
[Python Generators || James Powell - YouTube](https://www.youtube.com/watch?v=XEn_99daJro)


有关生成器如何拓展出更多的想法,
如果你有兴趣的话, 值得看看;


## refer.

每一位认真的技术 blogger 都有很多值得精读的积累,比如这位[Tushar Sadhwani](https://snippets.live/)的:

- [Understanding all of Python, through its builtins](https://tushar.lol/post/builtins/ "Understanding all of Python, through its builtins")
- 
