Title: 寻路ing Guido van Rossum 
Date: 2014-09-21 13:13:13 
Tags: DAMA, Pythoneer, Guido
Slug: guido-finding-his-way

[TOC]

[Guido van Rossum on finding his way — Dropbox Makers — Medium](https://medium.com/dropbox-makers/guido-van-rossum-on-finding-his-way-e018e8b5f6b1)

~ The Python creator and Dropbox engineer reflects on his early days in programming

Guido van Rossum is the creator and benevolent dictator for life (a.k.a. BDFL) of the Python programming language. Here he reflects on his path and shares what he’s been working on since joining Dropbox. Read on for this and a hint at what’s next for Dropbox, for Python, and for the BDFL himself.

## You were an electronics hobbyist before becoming a programmer. How did you get started in electronics?

Okay, we’re going waaaay back. I don’t know exactly why I got into electronics as a kid. I remember that from the last grade in elementary school and probably through my second year in university, electronics kits and my own designs were one of my big passions.

It wasn’t always an easy path. In elementary school, I took one of the first projects I built into class as a show and tell project. There was no one who understood what it was or why it was interesting or cared. It’s a very vague memory. I just know that I took it in, and it fell flat.

## Was there a time when you eventually found your people?

In high school, I hung out with a few other guys who had similar hobbies. We were all the geekiest kids in class.

I remember our physics teacher really encouraging us. The three of us worked together to build a large electronic device that was then used in demonstrations in front of the classroom. That was very satisfying.

Throughout high school, I had a very vague idea of what kinds of careers would be open to me. My general idea was that I was good at both sciences and languages and not so good in social areas. I ended up choosing mathematics.

## How did you go from electronics to programming?

I went to the University of Amsterdam and enrolled in the mathematics department and started taking math classes there. Some of the classes turned out to be programming classes. As part of the class, you got access to a large mainframe computer that was in the basement of the building. I almost instantly discovered that was my passion.

![AOw_zZbFbtEJAzwRQ](https://d262ilb51hltx0.cloudfront.net/max/700/1*5Z4e-AOw_zZbFbtEJAzwRQ.jpeg)
Guido gave a talk on Python 3 during Hack Week 2014 at Dropbox in San Francisco. / Photo by Dan Stroud

## What interested you about computer science?

Having progressed through hobby electronics, from very simple analog circuits to somewhat complex digital circuits made with small integrated circuits—this was the early seventies—I was very excited to suddenly have access to a mainframe computer, even though initially I had to enter my programs using punch cards. It was a very slow and tedious process, but it was incredibly exciting to learn how it worked.

I very quickly gave up on all the electronics stuff because the computer stuff was so much more interesting. In my second year in university, I already started realizing that programming was incredibly exciting and interesting. I was also very good at it, but the core of mathematics—whether it was Calculus or Algebra, or certainly any of the more advanced, “real” mathematical topics—were not really my thing.

Then I somehow managed to change my curriculum—they were incredibly flexible about it—to a mixture of math and computer science. I took all the programming and computer science-related topics that were on offer.

Then I applied for a part-time position at the university data center, and it turned out that there was a group there that had a very small number of openings for talented students. They instantly hired me, and I spent more than five years working there while I was still studying.

I was actually close to dropping out.

## Oh my gosh! Why?

The job was so fun, and studying for exams wasn’t. Fortunately, my manager at the data center, as well as one of my professors, cared enough about me to give me small nudges in the direction of, “Well, maybe it would be smart to graduate, and then you can do this full-time!” (laughing)

And that worked. I did graduate, and I had a job lined up at a research institute, also in Amsterdam, doing programming right away.

## On Twitter, you once wrote, “In America, I’m Dutch, but around Dutch folks I’m American. #conflicted.” Where do you feel most at home?

Well, I would say, I just feel most at home in my own house with my family. (laughing)

My wife is American; my son has both nationalities, but he speaks English. I’ve lived in the US for eighteen years now. I actually don’t imagine I would ever go back to Europe for a long period of time. I expect I’ll spend most of the rest of my life in the US—probably in the Bay Area, because it’s such a great place.

## What are you working on lately at Dropbox?

I’ve completed a new feature that we’ve needed for the 
[Datastore API](https://www.dropbox.com/developers/datastore)
for a long time. It’s the ability to 
[share datastores](https://www.dropbox.com/developers/blog/107/new-datastore-features-shared-datastores-local-datastores-and-datastore-webhooks) with other users. It launches today.

![NMJBScQgtLZE0zmeOA1nJw](https://d262ilb51hltx0.cloudfront.net/max/800/1*NMJBScQgtLZE0zmeOA1nJw.png)

Is this something you’re working on with a team, or are you working more independently?

For this particular datastores feature, I’ve done most of the work independently, with two other people contributing, mainly in the form of code reviews. The datastore project as a whole has included a large team of contributors, including several talented interns.

## When you joined Dropbox, you specified that you would be a regular engineer, as opposed to a manager or a technical lead. Why was that distinction important to you?

I think it was because I enjoy doing actual engineering work, and I don’t enjoy as much the formal aspect of management. In the past, I was thrown into such a role for a small team, and it never really worked out. I never really felt comfortable in that type of role. I was always much more comfortable just writing code. Over time, that has included technical leadership, but I like to be part of the work and not just tell people what to do or how to do it.

## How do you balance your two roles as Dropbox engineer and Python BDFL?

In terms of time management, they overlap and compete. I don’t set aside a particular time of my day or my week or my year for Python BDFL stuff versus Dropbox stuff.

What happens in practice is that sometimes one thing requires a lot of attention and focus, and then I reduce my activity on the other front, and vice versa.

![AriSTNW_leEP85c7r](https://d262ilb51hltx0.cloudfront.net/max/1200/1*AriSTNW_leEP85c7r-wcew.jpeg)
Guido introduces Dropbox datastores at DBX 2013. / Photo by Doug Cody

## What do you like most about working at Dropbox?

One of the most satisfying things here is to see such a large group of people being so enthusiastic about the products and the features, and being so creative; to see everybody working together and owning their mistakes and having fun going through all this stuff and being incredibly focused. It’s just very exciting to see this group be so productive and enthusiastic and powerful and capable.

## What did you work on for your Hack Week project?

Static typing for Python. It’s based on the PhD thesis of one of our engineers, Jukka Lehtosalo. He wrote a static typing tool for Python, and essentially what he did for his thesis work was a prototype. During Hack Week, with a group of seven people—including three guests and two interns—we improved the prototype, added a number of tools, did a whole bunch of integration work.

There’s even more stuff to do, of course. We didn’t produce an end product, but we did a lot of work on the tool, and we have a couple of very interesting ideas on how to move this forward.

## Why did you choose static typing for your project?

I think that at least adding static typing as an optional part of Python is a good thing for the distant future. I also think that this particular tool may be able to help Dropbox convert our own Python 2-based codebase to Python 3.

![yemdZovwCmvm7b2Dkm6SRQ](https://d262ilb51hltx0.cloudfront.net/max/800/1*yemdZovwCmvm7b2Dkm6SRQ.png)

The first lines of Dropbox code were written in Python, and Python Bees have featured at DBX and previous Dropbox hack weeks.

## How do you balance the more immediate needs and requests from programmers with a long-term vision for Python?

Python has a large group of core developers who do a lot of the work and review even more of the work that goes into Python. The Python developer community has its own processes for evolving the language. Over more than twenty years of working on the language together as a community, we’ve learned some constraints on how we can evolve this particular programming language.

If you change the language too fast, you leave your users behind, or your users complain that their programs are always broken by every new version. If you change too slowly, you get complaints from users that either their bugs don’t get fixed or their feature request never get executed. That’s a tricky balance, because one person’s mind-boggling speed is another person’s snail’s pace.

Over time, there’s a whole body of knowledge around what, in general, is a good idea to add to the language or to the library, and what things are better left as open source projects that people can install as needed.

Learning all that has been an incredible experience for me. I’m currently at a point where I’m pretty comfortable that if I decided to retire from that community, the rest of the developers understand the process and understand the reasons why we do things and how to have discussions that result in decisions on a reasonable timescale.

## Do you ever think about retiring from the Python community, and what you would do with your time then?

(laughing) That is a very good combo of questions because I definitely think about retirement and what that would mean for me and what I would do then, what it would mean for my family. So far, I’m just thinking about it.

## Do you ever get nervous about new programming languages popping up and getting a lot of attention?

I find it an interesting phenomenon. It doesn’t make me nervous. It tends to make the more recent converts to a language nervous because they see that they spent three weeks or six weeks or two years becoming an expert at some level that is important to them. And then, with their limited experience, they might imagine that next year, everything they learned about Python will be useless and they’ll have to start over.

I’ve seen cycles like that of the popularity of systems and languages and software. Things come and go. I don’t know where Python will be five years or fifteen years from now, but I’m not worried that Python will suddenly disappear. I expect that Python still has a large path ahead of it, where it will absorb new ideas and adapt to new environments. I also expect that, at some point, something else will happen that gradually takes over, maybe borrowing ideas from Python but putting them into a different shape or combining them differently with ideas from other languages.

![omEEAJapdc0XY9IfR](https://d262ilb51hltx0.cloudfront.net/max/1200/1*omEEAJapdc0XY9IfR-mFlA.jpeg)
~ Guido teamed up with Dropbox CEO Drew Houston in the DBX 2013 Python Bee. / Photos by Doug Cody

![4saVabl5aGfdTVuPLBNBCQ](https://d262ilb51hltx0.cloudfront.net/max/1200/1*4saVabl5aGfdTVuPLBNBCQ.jpeg)

![ziwbjd1WMkmuuoFK9q0Q](https://d262ilb51hltx0.cloudfront.net/max/1200/1*w-ziwbjd1WMkmuuoFK9q0Q.jpeg)

## In your [letter to a young programmer](http://neopythonic.blogspot.com/2013/10/letter-to-young-programmer.html), you wrote that you hoped they would dream big. But one of the challenges for programmers now is that there are so many big dreams to be had, so many opportunities competing for their attention. Do you have any advice for finding direction early on?

中译: [Letter to a young programmer](http://blog.zoomquiet.io/guido-letter-2-young.html)


Early in their careers? Well, I would not be the expert on that myself, because I took a long time to settle in my career. Looking back—I’m obviously very happy with how everything turned out—but I do think I was probably too passive in choosing what I wanted.

I’ve almost never applied for a job. I’ve always waited until someone asked me. And while that worked out well for me, I think in general that may not be the best strategy.

But don’t stress out too much about being in control of everything. There’s so much that you can’t possibly know. There’s something called the “fear of missing out.” And there are so many people who feel that if they don’t control every aspect of their curriculum, they’re not going to get the super job they want.

Well, it turns out that those people who do all those things aren’t any happier than the people who make some mistakes. So I think it’s good to realize that when it comes to your long-term career, you can’t be completely in control. If you pick a particular thing too soon, you may miss an opportunity for an unexpected left turn.

...

## Changlog

- 140921 官方通知邮件引发直觉思考
 