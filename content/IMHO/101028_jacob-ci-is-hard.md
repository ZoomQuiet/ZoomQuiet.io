Title: CI is hard!
Date: 2010-10-09 
Tags: Jacob,Pythoneer,Zh 
Slug: 101028_jacob-ci-is-hard

[TOC]

[Buildbot](http://buildbot.net/), 
the venerable Python 
[continuous integration](http://en.wikipedia.org/wiki/Continuous_integration)
server, has the reputation of being complex and difficult to set up.

After spending a couple of weeks deep in Buildbot land, I've come to the conclusion that this reputation, while true, is only partially deserved. That is, Buildbot is complex, but only if you're trying to view it as an out-of-the-box CI solution. Buildbot suddenly starts to make much more sense if you view it as a framework for creating your own CI solution, not a CI server in its own right.

You won't find this revelation anywhere in the Buildbot docs, nor in any of the books or online material that cover the tool. There are some good tutorials out there showing how to set up a simple Buildbot instance – Jeff Younker's 
[Foundations of Agile Python Development](http://www.amazon.com/dp/1590599810/?tag=jacobian-20)
has the best one I've run across – but none of these examples make much sense when setting up a complex buildfarm with complicated requirements.

So I'm here to fill that gap. In this series of posts – I think I'm looking at five parts – I'll explain this "Buildbot is a CI framework" view, delve into Buildbot's architecture, and then walk through the complicated-but-worth-the-effort CI sever I've built for Django.

By way of disclaimer I should mention I'm anything but a Buildbot expert. I'm almost certainly Doing Things Entirely Wrong. I may or may not be using public APIs as I've simply trolled through Buildbot's source until I found something that did what I wanted. However, what I've got here on the other side makes me pretty damn happy, and I want to show it off.

Here, then, is

## Part 1: Background

We've been looking for a CI solution for Django for quite some time. Over the years we've tried a bunch of different tools: Buildbot, 
[CruiseControl](http://cruisecontrol.sourceforge.net/)
, 
[Hudson](http://hudson-ci.org/), and even some home-grown solutions.

Nothing's worked out. That is, nothing's been able to provide the "continuous" part: builds only continue working as long as there's someone dedicated around to babysit the system. This sucks: it's meant that at times Django's been broken on supported platforms simply because nobody's been bothering to run the tests.

A few weeks ago a few of us started banging on this problem again, determined to get it right this time. Eric set up a new Hudson instance (modeled after the one he'd been using at work), and I dove headlong into Buildbot again. I'm not really going to talk much about Hudson here, but I'll note that it's actually been really instructive working on two different systems in parallel. It's forced us to really think through and formalize our CI needs.

This led me to my first big CI revelation: 
    
    CI is hard. 

There's any number of "simple" CI tools out there...  and they appear to work for exactly two projects (the project the tool was built to test, and the CI server itself, natch). The general purpose tools – Hudson, Buildbot, CruiseControl, etc. – are big, complicated, and heavily opinionated. This is a clear sign that we're in a space where even the basic tenets of the problem can't be agreed upon by all parties. CI is one of those problems that's hard because there really isn't a good core set of needs to be abstracted. Nearly every project has very different CI needs.

[This is part of what makes Buildbot so complicated: I think it's actually trying pretty hard to be completely agnostic and allow any kind of continuous integration system you could think up. If Buildbot was more opinionated it could drop some of the layers of abstraction, but because it's trying so hard to be everything to everyone it ends up being crazy complex. I've not decided if this is admirable or crazy. Both, perhaps.]

So what are Django's needs? What make CI hard for us?

- Django's big. The test suite is around 40,000 lines of code in something like 3,000 individual tests. We work constantly to speed up the test suite, but best case it still takes about 5 minutes to run.

This means that our CI absolutely needs to be distributed – a single test server won't cut it.

- Our test suite isn't just unit tests; in fact, it's mostly integration tests. We run most tests against real databases and attempt to simulate as much of the HTTP request/response cycle as we can.

This means that our build system needs to be heterogeneous: since we test against real databases, we need to have lots of different ones to test against. We can't just run a farm of Linux buildslaves running Python 2.6 and SQLite. Since slaves are heterogeneous, the build system needs to be highly targeted. We can't treat each build slave identically, but we'll need to target certain types of tests to the slaves that support 'em.

- We're ambitious in what we support: Django supports four versions of Python (2.4, 2.5, 2.6, and 2.7), three Python implementations (CPython, Jython, and PyPy), four database engines (PostgreSQL, MySQL, SQLite, and Oracle), multiple versions of each database (for example, we support six versions of PostgreSQL: 8.0, 8.1, 8.2, 8.3, 8.4, and 9.0), and a bunch of OSes (Mac OS X, Windows, and most Linux and BSD flavors).

We need the capability to run all sorts of crazy combinations. In an ideal world, we'd actually be able to test against every single unique python/db/os combination.

This means that our build system needs to be capable of getting really big, potentially spanning dozens or even hundreds of machines. We're clearly talking cloud computing here: there's no way a bunch of volunteers can afford the money and time to keep a rack of dozens of heterogeneous hardware all running smoothly.

- As I mentioned, we're all volunteers. Nobody gets paid to babysit the CI server, which means it needs to be highly autonomous. Builds need to happen without any intervention. Most critically, build servers can't disappear, go "stale" or break because /tmp gets full.

After a bunch of playing with these requirements, I sketched out a dream system that looked something like this:

- We've got a bunch of (dormant) VM images for a cloud computing service or platform.
- Each image "knows" which kinds of configs it can build. For example, one image might have Python 2.4 and SQLite, while another might have Python 2.7 and PostgreSQL 9.0.
- When new requests are made the build master spins up some VMs, hands them build jobs (based on the types of builds the VM can support).
- When no more builds are in the queue for a particular VM, the build master shuts down the image and saves us money.

Every out-of-the-box CI system I examined failed to give me that workflow. Most failed on the "heterogeneous" requirement. That includes Buildbot. I knew, however, that a few projects – PyPy, Chrome, and Python itself – were using Buildbot to some success against similar issues, and I knew that Buildbot had recently gained the ability to deal with cloud computing. Finally, since Buildbot's written in Python I was fairly confidant in my own ability to hack it to pieces if necessary.

Well, a couple of weeks later, I'm there: I have a Buildbot-based system that's doing exactly what I described above. I'm still not 100% sure this is the solution, but it's a solution, and it's working.

The rest of this series will dive into the code. Next time, we'll look at an overview of Buildbot's architecture and configuration, and I'll explain my Buildbot-is-a-framework revelation in more detail.


## Changlog

- 1406?? 
- 140618 偶遇抄转
 
