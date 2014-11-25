Title: How to argue for Python's use
Date: 2014-07-18 
Tags: Brett,Pythoneer,Zh 
Slug: 140718_Brett_Cannon-How2argue4Python-use

[TOC]

[How to argue for Python's use](http://nothingbutsnark.svbtle.com/how-to-argue-for-pythons-use)

 
Recently I wrote a blog post about how I don't worry about Python losing users. Within minutes I had people asking about Python's usage, which the post was not about and is a very different thing to worry about. See, it looks like the number of people using Python will continue to be high into the future, but whether Python will be used for as many projects is not guaranteed; the number of users is great and seems secure, but the number of uses of Python in projects is not nearly as certain.

This blog post is meant to help show how Python is still very much viable for most software projects out there. I'm not going to worry about selling Python to people going up against other dynamic languages like Ruby as I think those battles tend to come down to personal taste. What this is meant for is people dealing with teammates trying to sell statically typed languages. Specifically, this post is going to be geared towards arguing against Go, but it could be any statically typed language.

"Why Go?", you might ask. Well, because Go is actually gaining users at Python's expense. Ever since Python's growth trajectory went hockey stick starting between 2003-2005, Python itself has not been the king of the hill to unseat; it was the underdog. Traditionally Python has captured users from languages like Java and then kept them (I'm not going to argue about C++ users because typically they are have severe performance needs, need a systems language, or performance addicts and need to go into rehab). But things are different with Go. Python is now one of the top languages in terms of use out there, taking away our underdog stance. And for once there is another language out there coming from the statically typed programming language community whose productivity/performance tradeoff is good enough to convince some Python programmers to choose Go over Python.

## Go, today

I should start out saying that Go is currently my second favourite language. If I were asked to start a new project today and I couldn't convince people to use Python I would argue for Go's usage instead. Do not read this blog post as me saying that Go is a bad language. The key point of this blog post is to convince others that Python is very much a viable alternative to Go in the productivity/performance tradeoff game, not that Go is bad. Read this blog post as anti-Go and you're taking something personally that you shouldn't.

I should mention that I use Go at work on occasion and try to follow the language's community somewhat. Now this does not make me an expert in Go by any stretch of the imagination, but I'm not pulling knowledge out of docs and blogs posts alone either. But I am on the Python development team, so do realize that no matter how fair I try to be, inherent bias will be there to some extent.

So, with those caveats out of the way, let's look at what Go offers a programmer.


### Productivity

The way I like to view Go is take your favourite dynamic programming language, start removing features that make speeding it up hard, and you end up with Go. Static typing is kept to to a minimum as it is typically only in your face at API boundaries. Structural typing also makes things easier to work with (think of it much like duck typing). The syntax isn't heavy-handed (although it does use curly braces). Don't view Go as C/C++ with unsafe features removed and some productive bits added on or else you will end up frustrated (e.g. "why can't I use the make() built-in or have varying return value counts like the map type?" is the wrong way to view the language; this is a reason why C++ programmers have not switched to Go). Really fast compile times also makes the development cycle feel more like a dynamic language than a compiled one. And some people actually prefer the verbosity gained from not having exceptions as it forces you to deal with exceptional cases instead of (accidentally) ignoring them (this is an instance of Go's initial systems programming design showing through). Add on that the language itself is rather small and fits in your head and has strict forward-compatibility requirements for itself (you are not getting generics any time soon), and coding in Go is basically pleasant to work with.

Being statically typed, Go gets to have tooling support fairly cheaply (it also helps the language was somewhat designed for it early on). In a shrewd move, Go made sure the core tooling needs actually come with Go itself. go fmt enforces Go's style guidelines and also allows for refactorings through custom rules (which also make the whole "use tabs for indent" thing a non-issue since it means you set up your editor to represent tabs however you want and then go fmt makes it universally tabs for your VCS). go fix updates code to meet changes made to the language since the last release. go get fetches dependencies and installs them.

The last productivity perk of Go is that it statically compiles everything, making deployment simpler. This isn't quite a big deal, though, if you are using containerization for your development and deployment. This is a big deal, though, if distribute a command-line tool as it becomes just a single file to ship instead of a collection of dependencies plus your code.

### Performance

In terms of raw performance, Go does well. It's hard to point to any one benchmark that definitely shows that Go is always the fastest choice since even the The Computer Language Benchmarks Game show some benchmarks where CPython 3 is faster. But in general you should consider Go fast enough for your needs no matter the work.

But where Go really shines is with concurrency. Now do realize that concurrent code does not mean parallelized code which is a common misconception; concurrent code can still be single-threaded, it just makes task switching easier/better. Go has goroutines which make it dead simple to fire off code to execute concurrently. The language provides communication channels which allows for very clean message-passing style of concurrent programming if you don't want to go down the shared memory route which is also supported. And with all of this integrated into the language it makes it second nature to write concurrent code where (easily) possible. In other words Go programs can be fast and the language tries to empower you to do that in a reasonable fashion.

## Python, today

Hopefully I have convinced you that Go is a good programming language, if for any other reason it will help dispel some people from thinking I poorly portrayed Go in this whole discussion. But let's now discuss how the productivity/performance tradeoff looks for Python.

### Productivity

First and foremost, Python is very easy to learn. There's a reason why Python is currently the top choice for a teaching language at top-rated US universities. That equates to a steady stream of new programmers already versed in the language as well as showing it's easy to teach other programmers. I also don't think it's hard to convince people that you can definitely get a lot done in a few lines of Python code (the Go/Python 3 comparison shows that Python can accomplish solutions in less code than Go every time). So I would argue no one should disagree that you can be highly productive in Python, even compared to Go.

Where people typically start to argue against Python is in tooling support. But if you look at the various tools I pointed out for Go – fmt, fix, and get – there is a Python equivalent found from the community. For style formatting that follows PEP 8, there is pep8 for commit-check time or autopep8 if you want more go fmt style automatic rewriting. For go fix or go fmt for refactoring you could argue that 2to3 performs the same function. As for go get, Python has pip. And instead of statically compiled binaries we have venv/virtualenv or code freezing like cx_Freeze (on top of containerization like anything else). There's even code analysis through projects like pylint. Arguing that Python can't work for large projects due to the lack of tooling support has always seemed like a shallow argument to me.

And if there is one place where Python definitely does well, it is in the breadth and depth of the third-party libraries and tools available as seen on PyPI (I'm sure someone somewhere is snickering that "not all of those run on Python 3", which is true but the support is pretty darn good for Python 3 and simply continues to improve so I don't worry about that argument, plus you can code targetting Python 2/3 simultaneously and then really not care about which version you aim for). While looking at godoc.org shows that Go is not exactly lacking in community support, Python's age alone guarantees it has more third-party libraries available to it and will continue to do so.

### Performance

Because Python has been around for so long and become so big, simply saying "Python is fast enough" doesn't tell the whole story thanks to the various implementation options and speed-ups that are available. But before diving into VM-level options, it should be mentioned that Python's stdlib offers options to gain speedups. For instance, concurrent.futures a dead-simple way to execute embarrassingly parallel code concurrently. And the new asyncio makes writing asynchronous code in Python 3.3 and newer much easier. While it might not be integrated into the language like it is with Go, concurrent programming in Python is doable and not necessarily in a painful way.

But one of the biggest ways you can influence the performance of your Python code is in your selection of VM.

### CPython + Cython

If you are working with a C extension module, then CPython is your best option (and if you don't know the nomenclature, CPython is the interpreter you get at python.org). Performance is at least reasonable for most things – for some reason some people think the Python development team doesn't care about performance which is a lie – and it is obviously going to have the newest features as CPython also acts as the language specification.

If you do find yourself wanting a bit more speed for some inner loop code, Cython is an option with CPython. Cython will transpile your Python code into C extension code as best as possible. There are supported ways to make it allow for better C code, so it all depends on how Cython-specific you want to get. Cython also makes it easier to write C extension modules (but keep reading for an alternative that supports more than CPython).

### PyPy + cffi

If you are not reliant on a pre-existing C extension module, then PyPy will give you the best overall performance. Its JIT is great and the team welcomes the challenge of code that runs faster in CPython as they hate being slower as shown by speed.pypy.org. Honestly, unless PyPy doesn't support a version of Python you really want to use – since PyPy typically lags behind by 2 versions, e.g. pypy3 currently supports Python 3.2 while 3.4 is the latest CPython release; they are always looking for donations to help with this – I would only consider not using PyPy because you rely on a pre-existing C extension module (numpy is a common reason, but even there PyPy is looking for donations to fix that problem).

That doesn't mean, though, that if you need to wrap some C code you can't use PyPy. The PyPy project has another project called cffi which is meant to facilitate the wrapping of C code for use by Python code. The key benefit to using cffi is that if you use it then the C code can be used in CPython and PyPy (IronPython and Jython I believe are also working on adding support for cffi). So if you are wrapping C code I would strongly suggest you look at cffi over a hand-crafted C extension module or Cython so you can have better Python implementation support and be able to use PyPy.

## Numba

If you're doing numeric work, then Numba is an option you should definitely consider. Economists are noticing its performance when it comes to scientific computing. While it won't necessarily help out when it comes to general Python programming, Numba's use of LLVM to perform JIT does help when using things such as numpy or other module in Python's very strong scientific computing stack.

## Python, tomorrow

With all of that taken into account, Python is definitely not standing still (nor is Go, e.g. they are busy rewriting their compiler in Go and shifting things out of the linker into the compiler for even faster compilation speed). Python's future continues to look bright.

### Productivity

Python is an evolving language. Unlike Go, Python is willing to change the language, even in ways that won't be backwards-compatible forever. This means Python can become even more productive over time at a faster rate than Go typically can (although until a Go 2 begins development it is unknown what kind of stance the Go team will take for language evolution).

On the tooling front, there is work to standardize a set of function annotations for declaring types. This came up during the PyCon 2014 language summit where there was agreement that enough projects were now wanting a way to declare the expected types for function parameters and return values that using function annotations to think about standardizing on something that could maybe end up in the stdlib would be useful. The discussions have not started yet on the pytypedecl mailing list, but I know a PEP is about to be started. This could be beneficial to not just projects like Cython and Numba where the type information could be used, but also in tooling like code analysis, refactoring, etc.

### Performance

Long-term, there are two projects that could help with Python's performance. One is a new Python VM called Pyston. It's very new, but its goal is to use LLVM's JIT (yes, this sounds like Unladen Swallow, but LLVM's JIT is better than it was back in 2009 so there's hope the project will lead to some good results).

But the project that really has me excited is the PyPy-STM project. The "STM" stands for "software transactional memory" and it basically allows Python to ditch the GIL. The performance is now 1.2x-3x slower than PyPy which is very respectable. They are currently looking for donations to continue the work to reach the goal of pypy-stm with 2 threads is universally worth running over vanilla PyPy.

## Making the choice at least murky

Hopefully one comes out of this blog post realizing that Go is not the end-all, be-all answer to the productivity/performance tradeoff. Python definitely has great productivity perks and it is no slouch in the performance realm either, making it still my language of choice. If you find yourself potentially choosing something other than Python for a project, please make sure to stop and think about the productivity loss from not using Python and then look at the various options you have for making Python execute quickly so that you make an informed choice as to whether Python will work for your project.

## Changlog

- 1406?? 
- 140728 偶遇抄转
 
