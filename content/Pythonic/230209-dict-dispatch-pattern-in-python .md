Title: Python 中的字典调度模式
Slug: 230209-dict-dispatch-pattern-in-python 
Date: 2023-02-09 18:42
Summary: Pythonic/ 字典的神奇功能
Tags: Python,translate,Pythonic
Author: ZoomQuiet
Status: published


[TOC]

原文: [Dictionary Dispatch Pattern in Python | Martin Heinz | Personal Website &amp; Blog](https://martinheinz.dev/blog/90)

是否曾经写过一堆 if/else 或是一个巨大的 match/case ,
其中所有语句只是为了匹配一值, 想知道如何将这种事儿简洁又可读嘛?

如果这种场景,那么 字典调度模式 可能就是适合的工具;
通过字典分派,可以通过简单的查找 Python 的字典来替代任何条件组,
而且有很多姿势可以搞...

If so, then dictionary dispatch pattern might be a tool for you. With dictionary dispatch we can replace any block of conditionals with a simple lookup into Python's dict- here's how it works...

## 使用 Lambda 函数

字典分派的整个思想是我们可以根据变量的值运行不同的函数,
而不是对每个值使用条件语句来指向不同函数;

如果没有字典调度, 我们将不得不使用 if/else 或是 match/case 判别块:

```python
x, y = 5, 3
operation = "add"

if operation == "add":
    print(x + y)
elif operation == "mul":
    print(x * y)

# ---------------

match operation:
    case "add":
        print(x + y)
    case "mul":
        print(x * y)

```

虽然这样在 if 或是 case 数量少感觉还成,
但是,随着选项数量的增加, 可能就变得冗长难以阅读和维护了;

作为替代,我们可以进行以下转化:

```python
functions = {
    "add": lambda x, y: x + y,
    "mul": lambda x, y: x * y
}


print(functions["add"](5, 3))
# 8
print(functions["mul"](5, 3))
# 15
```


实现字典分派最简单方式就是使用 lambda 函数;
在原来的, 我们将每个 lambda 函数分配给字典的一个键;
然后, 就可以通过查找键名并选择性的传入参数来调用到该函数(行内匿名声明的);

当你的操作可以用单行代码表示时,
使用 lambda 是合适的, 但是, 通常使用适当的 Python 函数才是可行的...

(`是也乎`:

不过,也不一定,参考: [flatliner-src: 将 Python 程序转换为一行代码](https://pycoders.com/link/10308/web)

真的有项目可以自动将任何函数一键转化为由 lambda 串接的一行代码.

)


## 使用适当的功能

lambda 函数非常适合简单的情况,
但是, 你可能希望分派需要多行代码的函数:


```python
def add(x, y):
    return x + y

def mul(x, y):
    return x * y

functions = {
    "add": add,
    "mul": mul,
}

print(functions["add"](5, 3))
# 8
print(functions["mul"](5, 3))
# 15
```

使用适当函数时, 唯一的区别是必须在字典之外定义,
毕竟 Python 暂时不允许内联函数定义;
虽然, 这看起来有点儿烦, 可读性也差,
但是, 在我看来, 这也迫使你编写更加清晰/可测试的代码;


## 默认结果

如果你使用此东西方来模拟 match/case 语句,
那么应该考虑在字典键不存在时使用默认值:


```python
from collections import defaultdict

cases = defaultdict(lambda *args: lambda *a: "Invalid option", {
    "add": add,
    "mul": mul,
})

print(cases["add"](5, 3))
# 8
print(cases["_"](5, 3))
# Invalid option
```

这段代码利用了 defaultdict,
第一个参数指定了 "默认工厂",
这是一个在找不到匹配键时调用的函数;
你也可能注意到在此,使用了两个 lambda 函数 --- 第一个是用来捕获传递过来的任意数量参数,
第二个是因为我们需要返回一个可以调用的函数;

This snippet leverages defaultdict, who's first argument specifies the "default factory", which is a function that will be called when key is not found. You will notice that we used 2 lambda functions here - first is there to catch any number of arguments passed to it, and the second is there because we need to return a callable.

## 传参

我们已经在前述所有示例中看到,
将参数传递给字典中的函数非常简单,
得是不是,如果你想在将参数传递给函数之前对其进行操作应该如何呢?



```python
def handle_event(e):
    print(f"Handling event in 'handler_event' with {e}")
    return e

def handle_other_event(e):
    print(f"Handling event in 'handle_other_event' with {e}")
    return e

# With lambda:
functions = {
    "event1": lambda arg: handle_event(arg["some-key"]),
    "event2": lambda arg: handle_other_event(arg["some-other-key"]),
}

event = {
    "some-key": "value",
    "some-other-key": "different value",
}

print(functions["event1"](event))
# Handling event in 'handler_event' with value
# value
print(functions["event2"](event))
# Handling event in 'handle_other_event' with different value
# different value
```

第一个选项是用 lambda 函数, 
允许我们 -- 例如 -- 在参数载荷(payload)中查找特定键, 如上所示;

另一种选择是使用 parital 来"冻结"参数,
但是, 这要求你在定义字典之前拥有参数/载荷(payload):


```python
event = {
    "some-key": "value",
    "some-other-key": "different value",
}

functions = {
    "event1": partial(handle_event, event["some-key"]),
    "event2": partial(handle_other_event, event["some-other-key"]),
}

print(functions["event1"]())
# Handling event in 'handler_event' with value
# value
print(functions["event2"]())
# Handling event in 'handle_other_event' with different value
# different value
```


## 真实世界

到目前为止,我们只实验了类似 hallo-world 级别的示例;
字典分派在现实世界中有很多用例,
所以, 让我们游览一些:


```python
# parse_args.py
import argparse

functions = {
    "add": add,
    "mul": mul,
}

parser = argparse.ArgumentParser()

parser.add_argument(
    "operation",
    choices=["add", "mul"],
    help="operation to perform (add, mul)",
)
parser.add_argument(
    "x",
    type=int,
    help="first number",
)
parser.add_argument(
    "y",
    type=int,
    help="second number",
)

args = parser.parse_args()
answer = functions.get(args.operation,)(args.x, args.y)

print(answer)
```

首先是解析 CLI 参数;
这里我们使用内置的 argparse 模块来创建一个简单的 CLI 应用程序;
此处的得碊主要包含定义字典和为 CLI 设置 3 个可能的参数;

从 CLI 调用时,我们将获得以下内容:


```python
python parse_args.py
# usage: parse_args.py [-h] {add,mul} x y
# parse_args.py: error: the following arguments are required: operation, x, y

python parse_args.py add 1 2
# 8

python parse_args.py mul 5 3
# 15
```

如果指定了操作(add 或是 mul)以及 2 个数字参数,
则参数将解析到 args 变量中;
然后, 从字典调用函数时,使用这些秋粮和 args.operation ,
最后将其结果分配给 answer 变量;

另外一个使用字典调度的实际案例,
是对许多不同的传入事件作出反应 -- 例如 -- 来自 webhook,
又或是来自 GitHub 的拉取请求事件:

Another practical example of using dictionary dispatch is reacting to many different incoming events - for example - from a webhook, such as pull request events from GitHub:

```python
event = {
  "action": "opened",
  "pull_request": {
    "url": "https://octocoders.github.io/api/v3/repos/Codertocat/Hello-World/pulls/2",
    "id": 2,
    "state": "open",
    "locked": False,
    "title": "Update the README with new information.",
    "user": {
      "login": "Codertocat",
      "id": 4
    },
    "body": "This is a pretty simple change that we need to pull into master.",
    "sender": {
      "login": "Codertocat",
      "id": 4
    }
  }
}
```

GitHub 拉取事件可以指定许多不同的操作,
例如: assigned,edited, labeled, 等等;
这里, 我们尝试实现 4 种最常见的字典调度:


```python
def opened(e):
    print(f"Processing with action 'opened': {e}")
    ...

def reopened(e):
    print(f"Processing with action 'reopened': {e}")
    ...

def closed(e):
    print(f"Processing with action 'closed': {e}")
    ...

def synchronize(e):
    print(f"Processing with action 'synchronize': {e}")
    ...

actions = {
    "opened": opened,
    "reopened": reopened,
    "closed": closed,
    "synchronize": synchronize,
}

actions[event["action"]](event)
# Processing with action 'opened': {'action': 'opened', 'pull_request': {...}, "body": "...", ... }
```

我们为每个动作类型定义一个单独的函数,
以便我们可以分别处理每个案例;
在此示例中,我们直接将整个有效载荷传递给所有函数,
但是,我们可以在传递事件载荷之前对其进行操作,
正如前述所示:

## 访问者模式

最后, 虽然简单的字典通常足够了,
但是, 如果你需要更加健壮的解决方案, 可以应用 `访问者模式`:


```python
class Visitor:
    def visit(self, action, payload):
        method_name = f"visit_{action}"
        m = getattr(self, method_name, None)
        if m is None:
            m = self.default_visit
        return m(payload)

    def default_visit(self, action):
        print("Default action...")


class GithubEvaluator(Visitor):

    def visit_opened(self, payload):
        print(f"Processing with action 'opened': {payload}")

    def visit_reopened(self, payload):
        print(f"Processing with action 'reopened': {payload}")


e = GithubEvaluator()
e.visit("opened", event)
# Processing with action 'opened': {'action': 'opened', 'pull_request': {...}, "body": "...", ... }
```

该东西方是通过首先构建一个具有访问功能的 Visitor 父类来实现的;
此函数自动调用名称匹配模式为 `visit_<ACTION>` 的函数;
然后,
这些单独的功能由子类实现, 其中每个功能本质上都充当了 "字典" 里其中一个 "键";
最后, 要使用这个模式/类,
嘦调用 visit 方法, 并让类测定调用哪个函数就好;


## 小结

避免条件判定是使事情变得简单可靠的方法,
但是, 这并不意味着我们应该尝试将字典分派硬塞到需要条件判定的每段代码中;

其实,这种模式有很好的用例, 比如说非常长的条件语句链;
又如果, 你因为某些原因无法使用不支持 match/case 的 Python 版本;

此外, 字典本身是可以动态改变的,
比如,通过追加键或是更改值(函数),这是普通条件语句无法实现的;

最后, 即便你不想使用字典(表)调度,
熟悉这一模式也是好的,
因为,在某些时候你很可能会遇到使用这一模式的代码,
那时你能看得懂, 就很不错呢. 😉


## PS:

一般都是在对一组相似场景中要进行不同决策时,
需要使用 字典分派, 
而且, 直接使用, 比用 访问者模式 的类要来的简洁,
而且也节省内存;

经验中, 唯一要注意的, 就是这组函数, 最好能有统一的参数形式,
否则, 调试起来很容易出问题;

另外, match/case 毕竟是语言级别的内建语法,
比手工用 字典来进行分派要流畅的多,
能用还是多用;





