Title: What to write
Date: 2009-11-10 
Tags: Jacob,Pythoneer,Zh 
Slug: 091110_jacob-what2write

[TOC]


Tech docs can take a bunch of different forms ranging from high-level overviews, to step-by-step walkthroughs, to auto-generated API documentation. Unfortunately, no single format works for all users; there's huge differences in the way that people learn, so a well-documented project needs to provide many different forms of documentation.

At a high level, you can break down the different types of documentation you need to provide into three different formats:

- step-by-step tutorials,
- overviews and topical guides to the various conceptual areas of your project, and
-low-level, deep-dive reference material.

Let's look at each in turn.

## Tutorials

Good tutorials are a must as they're usually the first thing someone sees when trying out a new piece of tech. First impressions are incredibly important: that rush of success as you work through a good tutorial will likely color your future opinions about the project.

Django's tutorial is frankly a bit musty at this point and is probably due for at least a light refresh, but it hits all the important points. A good tutorial should:

- `Be quick.` At some conference or another I heard someone – I think it was [Kathy Sierra](http://headrush.typepad.com/) – say that, as a rule of thumb, a new user should be able to experience success within thirty minutes. That's a great rule: thirty minutes is nothing – think "half a lunch hour." If your project can give new users the warm fuzzies that quickly, they'll come away wondering about all the awesome successes a deeper dive might give.

- `Be easy.` Remember: you want success to be the outcome of the tutorial. This means you need to playtest the tutorial under all sorts of different circumstances, making sure that it always works (even on Windows).

- `But not too easy.` There's always going to be a class of users who aren't really qualified to use your project. Someone who's never written any code before isn't going to get very far with Django; those types of users should fail quickly. Don't get them through the tutorial only to run into a wall later on.

Another similar anti-pattern is glossing over bad choices made in the interest of expediency. Django's tutorial makes this mistake: we gloss over the project/app distinction in a way that bites users later on. (It'll get fixed soon, I promise!)

The best way of thinking about a tutorial's ease is that it's the on-ramp onto your project's learning curve. This means the slope can be more gradual than later tasks, but no so much so that things suddenly get much much harder after the tutorial's finished.

- `Demonstrate how your project "feels."` More than anything, people are using your tutorial to get a sense of how your project is going to "feel" in the long term. This means you that it should be pretty cross-sectional; a good tutorial should show off most of the different areas of the project.

A couple of projects with really good tutorials to check out for inspiration are 
[LOVE](http://love2d.org/documentation?page=documentation) and 
[Lamson](http://lamsonproject.com/docs/getting_started.html).

## Topical guides

This is the meat of your documentation. Once somebody's learned (from a tutorial) the high-level concepts, they're going to need to dive into the details of some area or another. Any documentation worth its salt is going to have a whole bunch of these – Django's got about 35 different topical guides, covering each conceptual area (e.g. models, sessions, testing, etc.)

These don't need to cover every single configuration option or function argument – that's what reference material is for – but each guide (or section, or chapter, depending on how things are organized) needs to take a pretty deep dive into its respective area.

The main goal for topical coverage should be `comprehensiveness`. The reader ought to come away from a close read feeling very comfortable with the topic in question. They should feel that they know the vast majority of the possible options, and more importantly they should understand how all the concepts fit together.

Unfortunately there aren't a lot of projects that do these very well. Most have reasonable tutorials, many have okay-to-good reference material, but most seem to leave the topical guides to books.

While it's true that books shine in the "topical guide" area, they're not really a great substitute for guides as part of the official documentation. Official docs, even when done poorly, are usually much more up-to-date; books, even when done well, are often out of date the day they hit the shelves.

Books-as-guides can be done well – the 
[Subversion Book](http://svnbook.red-bean.com/)
is a great example – but only when the book is continuously maintained available for free.

There's a particularly pernicious anti-pattern in documentation where tutorials are provided for free but the real documentation is only available for purchase. At best that's lazy and sloppy; at worst it's downright evil. Free software needs free documentation. If you've got otherwise you should be ashamed of yourself.

## Reference

Finally, you need complete reference for all the public APIs your project provides. These should be designed for those who already know how to use some API, but need to look up the exact arguments some function takes, or how a particular setting influences behavior, etc.

It's important to point out that reference material is not in any way a substitute for good tutorials and guides! Great reference material on the foo.baz package does readers no good whatsoever if they don't know the name of the package they're looking for.

[Python's documentation](http://docs.python.org/)

is a perfect case in point. The individual standard library modules tend to have incredibly good documentation, but there's no high-level overviews to help you discover which module you might actually want! Take for example the 
[collections](http://docs.python.org/library/collections.html)
module: it's great reference material, explaining exactly what's in the module, how to use it, and what all the options are. But if you don't know that Python ships with a 
[deque](http://en.wikipedia.org/wiki/Double-ended_queue)
implementation in collections.deque you'll probably end up missing the library entirely.

Think of guides and reference as partners: guides give you the "why," and reference gives you the "how." Following the deque example, some sort of "guide to data structures in Python" could give an overview of all the different types of data structures in Python (be they built-in or standard library), linking off to the documentation for each module and type for the complete details.

It's really tempting to use an auto-documentation tool like Javadoc or RDoc for reference material.

## Don't.

Auto-generated documentation is almost worthless. At best it's a slightly improved version of simply browsing through the source, but most of the time it's easier just to read the source than to navigate the bullshit that these autodoc tools produce. About the only thing auto-generated documentation is good for is filling printed pages when contracts dictate delivery of a certain number of pages of documentation. I feel a particularly deep form of rage every time I click on a "documentation" link and see auto-generated documentation.

There's no substitute for documentation written, organized, and edited by hand.

I'll even go further and say that auto-generated documentation is worse than useless: it lets maintainers fool themselves into thinking they have documentation, thus putting off actually writing good reference by hand. If you don't have documentation just admit to it. Maybe a volunteer will offer to write some! But don't lie and give me that auto-documentation crap.

## What's next

Now that I've covered what to write, I'll move into how to write. Tomorrow I'll start going into the actual mechanics of writing good, readable technical prose.


## Changlog

- 1406?? 
- 140618 偶遇抄转
 
