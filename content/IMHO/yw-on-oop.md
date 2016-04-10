Title: On object-oriented programming 
Date: 2013-12-24 
Tags: YinWang,Pythonner,Zh 
Slug: 131224-yw-on-oop 




[TOC]

# 翻越分享原文 

- via: http://yinwang0.wordpress.com/2013/12/24/on-object-oriented-programming/
- Posted by Yin Wang in [oop](http://yinwang0.wordpress.com/category/oop/),[programming languages](http://yinwang0.wordpress.com/category/programming-languages/)


![yw_dark_age_battle.jpg](http://zoomq.qiniudn.com/ZQCollection/img/yw_dark_age_battle.jpg)


[written at the end of 2013 AD, during the Dark Ages of programming]

The programmer's world is full of fads and superstitions. Every now and then there will be somebody who come up and announce: "I can save the world!" No matter whether the ideas are good or not, there will always be followers, and the ideas soon become their religion. They then develop their community or camp, try to let those ideas dominate the world, and try to make the ideas live forever.

Object-oriented programming (OOP) is such a religion which claimed to be able to save the world from the so-called "software crisis". As a hindsight after so many years since it was introduced, not only didn't OOP save us, it brought us more confusion and harm than benefits. Unfortunately its dogmas and mispractices have become wide-spread and deeply intrenched. In this article, I hope to provide my viewpoint into this matter and try to find out the lessons that we can learn.

Like every article on my blog, the opinions are completely personal and not representing my employers or professors.


## Is everything an object?
"Everything is an object" is the core dogma of OOP and deemed as the highest standards of OO language design. Now let's take a careful look to see if it is true, or if it is a good idea to make things that way.


Many people take "everything is an object" for granted because when this sentence is taken literally it matches their everyday experience. Since the word "object" in English basically means "a thing", how can "everything is an object" be not true? But be careful since the definition of an "object" in OOP has a specific meaning which is very different from what it means in English.

OOP's definition of an 
[object](http://en.wikipedia.org/wiki/Object-oriented_programming)
 is "a combination of 
 [data fields](http://en.wikipedia.org/wiki/Field_(computer_science))
  (attributes that describe the object) and associated procedures known as 
[methods](http://en.wikipedia.org/wiki/Method_(computer_science))
". Can you really fit everything into this model?


First let's look at the real world and see if this definition can capture everything. Cars, trees, animals may sometimes be thought of as objects, but what about a change of the objects' position, its velocity and duration? What methods do they have? Well, you may define classes called Velocity or Time, with methods such as addition, but do velocity and time really contain the things that you call "methods"? They don't. They are just your imagination. You can add the velocities or time, but how can velocities or time contain the addition procedure? This is like saying that the bullets contain the gun.


So the most you can say is that "everything is an object" is a good way of thinking, but that is not true either. The definition of an object implies that a method can only belong to one object, but most of the time it doesn't make sense thinking of functions as belonging to any object. Say we have the expression 1+2, does the operator '+' belong to 1, or does it belong to 2? You have to make some arbitrary choice. Since you can make a choice, this means the '+' operator doesn't really belong to either of them. It is inherently outside of the objects.


So thinking of some things as objects may be helpful, but thinking of 
`everything` as an object is neither true nor useful.  Unfortunately "everything is an object" has been taken as a dogma and the highest standard of OO language design. Some OO languages claim that everything is an object in them. Whenever you notice that something is not an object, somebody will try to make it one. They may succeed in that, but things get very complicated that way, because that's not how things work.


The idealism of "everything is an object" is similar to "everything is a function" in the functional programming world and "everything is a set" in the math world. Before computer science was conceived there was a thing called the 
[lambda calculus](http://en.wikipedia.org/wiki/Lambda_calculus)
. Some people encoded everything including numbers and their operations, various data structures and control structures, ...  all in lambdas. One of the encodings of numbers is called the 
[Church numeral](http://en.wikipedia.org/wiki/Church_encoding)
. Every programming language researcher has played with them during their training. But unlike "everything is an object", "everything is a function" has never become a dogma or marketing phrase. Those formulations sometimes provide mental exercises and inspirations to the researchers but nobody really use them for actual computation, because they are inefficient and they are not really how things work. They are just approximations (models) to some essence of computation that we can't see. If you really use them for practical projects, things become complicated.


Mathematicians have a similar thing: set theory. Some geniuses encoded everything — numbers, operations on numbers, mathematical structures, ...  all in sets. Everything is just sets containing sets containing sets and so on. What's the problem? But when they really tried to do their proofs using those sets, the proofs fell under their own weights. Too complicated. Even with the complexity, set theory is not expressive enough to capture whatever the mathematicians have to say. Many people tried to fix it, but they all failed.


So "everything is an object" is in some sense on the same track of "everything is a function" and "everything is a set". Good thought exercise, but doesn't really work well in practice. I don't think that there is some "one true language", but this model of OOP is too far from correct or practical. It's somewhat like the 
[flat earth theory](http://en.wikipedia.org/wiki/Flat_Earth)
. Until today 
[some people](http://theflatearthsociety.org/)
still believe that the earth is flat and make all kinds of theories to prove it. Some of their arguments look very scientific, but do you believe in their formulas or a picture of the earth from the ISS? When you get the fundamental things wrong and don't throw them away, you have to patch them endlessly with even more complicated theories. And that's what happened to OOP.


![yw_flat-earth.png](http://zoomq.qiniudn.com/ZQCollection/img/yw_flat-earth.png)



## Are functions objects? 

From what I know, the original motivation of putting functions inside objects was to support GUI applications. You click on a button and some function (a callback) will be invoked. For the convenience of referring to the button, the callback takes the triggered object as its first argument. Since the callback does nothing more than this, it seems to be convenient to just store it inside the button. And thus we had an "object" which combines the attributes of the button and a method (the callback). Indeed this is a good idea, but this limited usage case can't really justify a universal notion of "everything is an object", just like a two-mile walk can't prove that the earth is flat.

If you really understand what is abstraction, you may have noticed that even the above story contains a subtle mistake: the callback in the button is not really a method. The true purpose of a method is to provide abstraction to the attributes, but the callback's purpose is not to provide abstraction. It is just a usual function triggered by the button, which happens to take the button as its first argument.

Very few functions should be considered methods of an object. If you look carefully, most of the time the objects just serve as a namespace (or module) in which you can store attributes and functions, but those functions don't logically belong to the objects. They just take the objects as inputs and produce some output. Only the functions that are most intimately connected to the attributes and provide an abstraction layer to them should be considered methods. Most of those are called "getters", "setters" or "iterators".

In some languages such as Scala or Python, functions are also treated as objects. But actually they just wrapped the functions into an object, give them some name such as "apply" or "__call__", so that when the objects are "invoked" you know which functions to call. But putting a function into an object doesn't really mean that functions are also objects, just like inviting friends to your house doesn't make them your family.

Functions are fundamental constructs. They don't belong to objects. They describe a change, transition or transformation of objects. They are not objects and can't be simulated by objects. They are like a base case of an inductive definition. They are where the illusion of "everything is an object" ends.



## The cost of excessive abstraction 
The major appeal of OOP is abstraction (and thus code reusing and DRY), but actually most of those abstraction facilities are already provided by traditional procedural languages and functional languages. Some of them do it even better than OO languages. OO claims its originality by emphasizing abstraction much more strongly than other languages. The result is that OO programmers usually overdo it. Some of them pursue abstraction and code reusing to the degree as if they are everything about programming.

![yw_screen-shot-2014-01-02-at-2-02-38-am.png](http://zoomq.qiniudn.com/ZQCollection/img/yw_screen-shot-2014-01-02-at-2-02-38-am.png)

For the purpose of code reusing, OO encourages a level of abstraction which makes programs hard to understand and hard to analyze. I often see Java programs with multiple levels of inheritance, overloading and design patterns, but actually doing very little. And because there is so much code that doesn't do useful things, it is really hard to find out which part of the code is doing the thing you want. It is like going through a maze. Another nice word for this is "robustness". If I have to go into all this trouble to make code reusable or robust, I'd rather just make copies of the code and modify them, but keep each copy simple and easy to understand.

Whenever you criticize Java or C++ for their verbosity, OO proponents will tell you that they are not authentic OO languages. They would ask you to look at Smalltalk. If Smalltalk's ways are that good, why almost nobody is using Smalltalk now? Because there are real problems in its approach. I think Smalltalk is the origin of over-abstraction and over-complication you find in other OO languages.

The "authentic" OO style of Smalltalk promotes the notion of "extremely late binding", which basically means that the meaning of the program constructs is determined as late as possible. Late binding gives you a chance to swap out the underlying implementation without forcing the upper levels to change, but this also means that you are no longer sure what a piece of code means. When I look at expressions such as '1+2′ and 'if (t) then ...  else ... ' in Java or C++, I at least know for sure that they mean an integer addition and an usual conditional. But I'm no longer sure about this in an "extremely late binding language", because the meaning of '+' and 'if" can be redefined. Giving the programmers the power of defining control structures is a bad idea, because soon your language will be abundant of quirky control structures designed by programmers who try to be clever. It will no longer be the language that you used to know.

An example for this feature is Smalltalk's conditional structure, which looks like this:


    :::smalltalk
    result := a > b
        ifTrue:[ 'greater' ]
        ifFalse:[ 'less or equal' ]


You send a message ifTrue: to a Boolean object, passing as an argument a block of code to be executed if and only if the Boolean receiver is true.

First of all, if you really have a well-designed language, you shouldn't be wanting to define your own control structures. As a seasoned Lisp/Scheme programmer, I have seen many custom-designed control structures (such as the various looping macros) over the years, but none of them turned out to be good ideas. I'd rather write slightly longer and more verbose code in the vanilla language than to learn those weird control structures. Second, if you are really genius enough to have invented another good control structure, the late binding feature of Smalltalk probably won't provide you the necessary power for defining it. The power of functions as an abstraction tool is limited. It is strictly less powerful than Lisp/Scheme's macros. Third, this feature of Smalltalk is not really a novel approach and it has a big problem. A similar but more beautiful conditional construct had been defined in lambda calculus since before computer science was born:


    :::lisp
    TRUE = λx.λy.x
    FALSE = λx.λy.y
    IF = λb.λt.λf.b t f


This is very beautiful and can be done in any functional language, but why none of the functional languages implement conditionals this way? Because when you see an expression IF b t f, you will have no idea whether it is a conditional or not, because IF can be redefined in the program. Also because IF is just a function, it may also accept unexpected values other than TRUE or FALSE. This may happen to make the conditional construct work but cause trouble later on. This is called "unintentional semantics". This kind of bug can be very hard to track down.

This approach also makes compiler and static analysis hard. When the compiler sees IF b t f, it no longer knows that it is a conditional and thus optimize it that way. It has to treat it as a usual function call. Similarly when the type checker sees it, it doesn't know what type to expect for b, because it may not be a conditional at all. The above argument against the lambda calculus can easily be adapted to Smalltalk.

So abstraction is a powerful weapon when used moderately, but when you do it in excess, it backfires. Not only does it make it hard for humans to understand the code, it makes automated analysis tools and compiler optimizations difficult or impossible to make.

## Design patterns, the brain eater

Although OO languages are touted for their ways of abstraction, they are actually not strong in terms of abstraction ability and expressiveness. There are certain things that are very easy to do in traditional procedural languages and functional languages, but was made unnecessarily hard in OO languages. This is why design patterns appeared. Design patterns' origin was mostly due to the dogma of "everything is an object", the lack of high-order functions (or the correct implementation of them) and OO's tendency of mystifying things.

When I first heard about design patterns I was already a PhD student at Cornell doing some PL research. I mostly used Standard ML and Haskell. After hearing my friends' high opinions of the 
[Design Patterns](http://en.wikipedia.org/wiki/Design_Patterns)
book (nicknamed the "GoF" book), I developed curiosity about its fame, so I borrowed one from the library. Within a few hours I found a mapping from all the weird names it introduced to the programming techniques I had been using all the time. Some of them are so fundamental and exist in every high-level language, so they don't really need names. Most of the advanced ones (such as visitor) are transcriptions of functional programming concepts into a convoluted form in order to get around OO language's limitations. Later on I found that Peter Norvig already gave a 
[talk](http://norvig.com/design-patterns)
on design patterns as early as 1998, pointing out that almost all of the design patterns will be "transparent" once you have first-class functions. This confirmed my observations — I don't need them.

I have to admit that some of the design patterns are cleverly designed and contain some ingenuity. You really need to get to the essence of the OO languages' internal designs and also understand lots of functional programming techniques in order to create them. But intelligence =/= wisdom. Even if they can achieve what functional languages can do, they are usually a lot more complicated. Choosing the hard ways can't really prove your genius. When you have first-class functions, things become so much easier and you won't even notice the design patterns' existence. Like Peter Norvig said, they will become transparent. So what a good language designer should do is to add first-class functions into the language instead of proposing design patterns as workarounds.

Every time I remove a design pattern (some other people wrote), the code becomes simpler and more manageable. I just removed the last visitor pattern from my Java code a few days ago and I felt so relieved. They gave me nothing but extra work when they existed. They hindered my progress. By deeply understanding how OO languages are implemented, you can write more advanced things than those provided by visitor patterns but without actually using them. I owe these insights into design patterns to some functional programming people. If you really want to understand the essence of OO design patterns and how NOT to use them, 
[this little book](http://www.amazon.com/Little-Java-Few-Patterns/dp/0262561158)
may be a good starting point.

Unfortunately design patterns somehow got really popular in companies, to the degree of unbearable. I saw the GoF book on almost every bookshelf when I interned at Google. Even if you don't write them yourself, there was almost no way you could avoid other people slipping design patterns into your code. Design patterns' marketing strategy as I perceived was much like weight loss products: "It can burn your fat without you doing any work!" They appeal to some new programmers' hope that they can write programs without understanding the fundamental concepts of computer science. Just by applying several patterns and patching things together, they hope to have a good program. This is too good to be true. You end up doing more work than you hoped to avoid. Design patterns eat programmers' brains. After using design patterns for some time, they no longer see things or write programs in clear and straightforward ways.



## What is an OO language any way?

To this point we haven't yet talked about what makes a language an "OO language" and what makes it not. Is it an OO language just because I can put both data fields and functions into a record? Or is it an OO language only if it also provides extremely late binding? How about inheritance, overloading, etc etc? Must I have all of them? Any of them?

It turns out that there is no good answer to this question. There really is no such thing as an "object-oriented language". Objects can be part of a language, but it is just a small part of it. You can't really say that a language is object-oriented just because it provides objects as a feature. The so-called OO languages are solidly rooted in traditional procedural programming (PP). OOP basically stole everything from PP, renamed the terminologies and acted as if the ideas were its own.

Historically the term OO was mainly used for marketing reasons. It could give a language some advantages of attracting people if you claim it to be an OO language, but now this advantage is diminishing because more and more people have realized the problems of OO's methodology.


## Harm in education and industry

Although OO has lots of problems, it is very successful in marketing and has risen to a dominant position over the years. Under social and market pressure, many colleges started using OO languages such as Java as their introductory language, replacing traditional procedural languages such as Pascal and functional languages such as Scheme. This in a large degree caused the students' failure to learn the most essential concepts of programming. The only thing that OO emphasizes is code reusing, but how can you teach it to the students who can't even write usable code, not to mention that code reusing is not really as important as some people believe.

At both Cornell and Indiana, I have been a TA for introductory programming courses in Java. I did it for multiple semesters. I still remember how confused the students were. Most of them had trouble understanding things such as the meaning of "this", why everything needs to be put inside classes, why make every field private and use getters, the difference between a method and a static method, etc etc.

There is a good reason that they don't understand — because OO is not how things work. Most of the time I feel that I was teaching design flaws and dogmas. Many of them learned very little in the end. Worse, some of those students really believed in OO. They ended up being proud of writing over-engineered and convoluted code. They no longer see things or write programs in straightforward ways. This is sad. I feel that we are no longer educating students as creative and critical thinkers, but mindless assembly line workers.


![yw_modern-times.jpg](http://zoomq.qiniudn.com/ZQCollection/img/yw_modern-times.jpg)

In industry, OO hasn't really proved its effectiveness with evidence. Good systems may be built in a "OO language", but the code is often written by people who understand the problems of OO and don't embrace "everything is an object" or "design patterns". Good programmers usually use workarounds in OO languages and are essentially writing in a traditional procedural style combined with bits from functional programming. So some OO languages and their tools may be pretty widely used, but the OO style doesn't really have much influence on the advancements of programming as a field.

## Final word

So what does this post has to say? A jihad against OO languages? Advocate functional programming? Neither. As I said, there is no such thing as an "OO language", so where is the war? Every so-called OO language also contains good elements that it borrowed (or stole) from procedural languages or sometimes functional languages, so they are not completely useless.

But honestly, it is the extra features added by OO (in addition to procedural programming, PP) that are causing most of the problems. There is no denial of PP's value. Those extra "true OO techniques" contain way more confusion than real value, to the point that their value is negligible. In my experience, accepting even one or two of those ideas may put you into a series of troubles and wrong ways of thinking which may take a long time to examine and recover.

Thus I suggest not to buy OO's way of thinking and don't try to exploit its "features". They are usually brain eaters that you want to stay away from. By eschewing those problematic features, you can still produce acceptable programs in an "OO language", because you are basically using it as an non-OO procedural language.



# 试理解 ;-) 快译畅读


![yw_dark_age_battle.jpg](http://zoomq.qiniudn.com/ZQCollection/img/yw_dark_age_battle.jpg)

[写在2013年尾,编程的黑暗时代.]

程序猿的世界充斥着各种时髦迷信.不时就有人跳出来吼:"俺能拯救世界!"诡异的是,无论多不靠谱的想法,总有追随者,并快速打造成全站的宗教,结成社区,尽量迫使其它所有人认同,以使这想法永存下去.

面向对象编程(OOP)就是宣称能将世界从所谓:"编程危机"中拯救出来的宗教.
然而,
即便在其引入这么多年以后,
OOP 不仅没有拯救世界,相比它宣称带来的好处, 带来了更多的混乱以及伤害,
不幸的是,其教条以及错误,
已经 根深蒂固的广泛植根于这世界.
本文,俺希望就此提出俺的观战,
并尝试指出值得学习的教训.


正如我的所有blog文章,
仅仅代表俺个人的意见,
并不代表我的教授以及雇主的态度.

## 一切皆对象 ? 
~ Is everything an object? 

`一切皆对象` 这是OOP 的核心教条,
并视为OO语言的最高设计准则.
现在,让俺,来谈谈这货是否真如其宣称的这么好.

很多人将
`一切皆对象`
视为理所当然的,
因为这话从字面儿上是吻合日常经验的.
因为,英语中 `对象` 的基本意思就是 `事物`,
那么 `一切皆事物` 当然正确了.
图样图森破,
在 OOP 中 `对象` 可是特殊定义的,和生活英语可是没一毛钱关系.

OOP中
通常接受的
[对象](http://en.wikipedia.org/wiki/Object-oriented_programming)
定义是: "
[数据字段](http://en.wikipedia.org/wiki/Field_(computer_science))
(描述对象的属性)以及关联方法 的结合体.
"
你真能在所有情景中适应这种模式嘛?

首先来设想一下OOP 模式是否能对真实世界加以解释. 汽车/树木/动物 视作对象的话, 那么它们的位置/速度/时间的 变化 乍说? 有什么对应的方法? 好吧, OOP 信徒可能叫你将类称为 速度 或是 时间 然后将方法增加进去. 可是速度/时间真的含有这种称为"方法"的东西 ? 当然没有, 这不过是想象罢了. 
你可以追加速度/时间,但是,怎么令其包含`加`处理? 
这就好比说:`子弹包含了枪`.

哪,信徒们最常说的:"一切皆对象"只是种好的思维方法,但事实并非如此. 一个对象的定义意味着一个方法只能属于一个对象,但大部分时间此思想并没有作用于任何对象. 当我们论及表达式: 1+2 , 是否得说 "+" 属于 1 ,或是算 2 的? 你必须作出属性方法归属的选择,而选择本身就已经意味着 "+" 操作其实并不真正属于任何一个对象,而是固有在对象之外的.

只能说 `有些` 事儿上对象是有帮助的,而 一切 皆对象这事儿即不真实也无用. 
悲摧的是, `一切皆对象` 已经成为面向对象语言设计的最高教条. 
一些面向对象语言声称在其内部真的一切都是对象. 
若你意识到什么不是对象时,就有人会跳出来将其折腾成对象. 
当然聪明人可以作到这点,只是事儿就变的复杂起来,
因为原本事物不是这么工作的.


`一切皆对象` 的理想完全类似 FP 世界里 `一切皆函式` . 
以前计算机科学称这种构想叫 lambda算子([lambda calculus](http://en.wikipedia.org/wiki/Lambda_calculus)). 

有人就在编码时,将所有数字/数据结构都给包含在 lambda 中了.
而这种包含了一切的东西叫
[Church numeral](http://en.wikipedia.org/wiki/Church_encoding)
. 但是,相比 `一切皆对象` , 
`一切皆函式` 好歹没有没有教条化过. 这只是在理论上是可行的,
但是,在实际工程中没有人这么折腾,因为这会令事儿变的复杂,而且效率低下.
因为,实际上并不是这么工作的,
它们只是近似描述(模式)计算机在我们视野外是如何计算的.
如果你真的将它们用在项目中,只能让事情变的复杂.

数学家们其实也有类似的宗教: 
[集(合)论](http://en.wikipedia.org/wiki/Set_theory).

有些天才试图编码掉一切:

- 数字
- 运算数字
- 数学结构
- ...

都能 `集合` 了.
一切都想是
集合包含集合包含集合等等....
这有什么问题嘛?
就是当他们真正尝试使用这些 集合 来进行证明时,
证明自身被掩盖了.
因为复杂性,
数学家无法用集合理论进行足够的表述.
很多人试图修复集合论,但都失败了.

因此`一切皆对象` 在某种意义上
和
`一切皆函式`
以及
`一切皆集合`
是相同的,
都是看起来是美的,却从未在实际工程中很好的工作过.

俺不认为存在: `唯一正当语言` (one true language),
何况 OOP 的模式和现实相差太远.
这有点儿象
[地球扁平论](http://en.wikipedia.org/wiki/Flat_Earth),
.时植今日,依然
[有人](http://theflatearthsociety.org/)
认为地球是平的,
而且用各种理论来证明.
他们一些论点看起来也很科学,
但是对比从国际空间站拍下来的照片,你愿意相信他们嘛?
而每当你发现有根本的东西错了,
又不想丢弃,
你就必须用更复杂的理论修补理论本身.

而这,正是 OOP 世界正在进行的事儿.


![yw_flat-earth.png](http://zoomq.qiniudn.com/ZQCollection/img/yw_flat-earth.png)



## 对象方法 ? 
~ Are functions objects?

据俺所知,将函式塞到对象中的原始动机是为了支持 GUI 开发.
点击一个按钮时,一些代码(回调)就应该被触发. 为了指明按了具体哪个按钮,回调的函式就需要触发的对象作为其一个参数.
因为回调就这么单纯,看起来将其存储在按钮中没有什么不好. 
于是我们有了个"对象", 包含了按钮的属性以及方法(回调). 的确挺方便. 
但 GUI 应用只是个非常有限的情景,并不能真正证明 "一切皆对象"的普世性. 
就象用两里路的平坦是不能证明地球是平的.

如果你真的理解什么是抽象,
可能已经注意到,上述故事包含一个微妙的错误:
    
    按钮的回调是不是一个真正的方法.

方法的本质目的是提供抽象的属性,但回调的目的不是为了提供抽象.
在这儿,只是刚好按钮包含了一个触发功能.

只有极少数功能应当视作对象的方法.
如果仔细观察,大部分情况中,对象只是作为一个命名空间(模块),
以便在其中存储相关属性和功能,
但是,这些功能在逻辑上并不属于对象.
他们只是将对象视为输入,并产生一些输出.
只有那些关系最密切,
并提供一个抽象层的功能,才应该考虑使用对象方法来封装.
其中大部分即所谓:
"getters"/"setters"/"iterators"


在一些语言,比如 Scala/Python, 函式也被视作对象.
而实际上,只是将一个函式包装成对象,
然后给予类似 `apply` 或是 `__call__` 的名称,
对象就酱紫能 `invoked` 了,而大家都知道函式只是调用了而已.

但是,将函式塞到对象中,并不等于函式也是对象,
好比,邀请朋友到家里来也不能令他们变成家人.

函式为程序的基本结构.
他们不属于对象.
他们描述变化,转变或是传送对象.
他们不是对象,也不能抽象为对象.
他们就像一种基本情况的归纳定义.
他们是`一切皆对象`的幻相的破灭.


## 过度抽象的代价
~ The cost of excessive abstraction 

OOP 的主要吸引力就是抽象(以便代码重用以及DRY),
然而,传统的程序语言以及函式语言提供的抽象设施足够了.
甚至于,他们中的一些比 OO语言抽象能力还要好.
OO信徒总是比其它语言更加强调抽象,好象这是OO 独创的.
结果是, OO程序猿总是作过头.
他们中有些人追求抽象以及代码复用的程度,就好象编程只是为了抽象.

![yw_screen-shot-2014-01-02-at-2-02-38-am.png](http://zoomq.qiniudn.com/ZQCollection/img/yw_screen-shot-2014-01-02-at-2-02-38-am.png)

出于代码重用的目标,鼓励以OOP的形式来抽象,其结果却是令程序难以理解/分析.
俺经常见到有 JAVA 程序动用多层继承/重载,但实际作的事儿不多.
更糟的是,正因堆砌了如此多的代码,却没有真正在作事儿,
以至于难以找到哪部分是你真正想作的东西.就象穿越一个迷宫.
而对这,有另外一个漂亮的形容词是 "[鲁棒性](http://zh.wikipedia.org/wiki/%E9%B2%81%E6%A3%92%E6%80%A7_(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6))" (健壮性,Robustness)

如果俺为了复用以及健壮,宁愿只用代码复制,再修订,
只要确保每个副本简单,容易理解.

每当你抱怨  JAVA/C++ 的冗长时, OO程序猿就会告诉你,那些不是真正的 OO 语言.
一准向你推荐 Smalltalk 的.
但是,如果 Smalltalk 是好的,为毛现在几乎没有人使用 Smalltalk 进行工程开发?
俺认为, Smalltalk 就是其它 OO 语言中
过度抽象以及过度复杂的发源.

在"正宗"OO 语言 Smalltalk 中,
提倡的风格是 "极迟绑定" (extremely late binding),
意味着,要尽可能晩的确定概念的意义再进行构建.

这样,你有机会换出(swap out)底层实现,
而不用强制变更上层.
但是,同时也意味着你也无法及时明确一段代码究竟会作什么!
比如,在 JAVA 或是 C++ 中看到诸如
`1+2` 或是 `if (t) then ...  else ... ` 的表达式时,
至少俺知道是作整数相加,以及往常一般的条件判别.
但是,若在"极迟绑定"语言中就完全一头雾水了!
因为 `+` 和 `if` 都是可以重新定义的.
类似问题也出现在 Lisp 家族语言的宏体系中.
事实证明,给予程序猿定义控制结构的能力,
这主意其实很囧,
因为立即就会发现,自作聪明的程序猿都在努力向语言里塞满各种特殊的控制结构.

这一特性,可以举个 Smalltalk 的著名条件结构为例:


    :::smalltalk
    result := a > b
        ifTrue:[ 'greater' ]
        ifFalse:[ 'less or equal' ]


你发送一消息 `ifTrue:` 给一个布尔对象,作为参数传递的代码,
当且仅当布尔接收器为真时,才执行.

首先,如果你真正拥有一个良好设计的语言,
但是,不想设计自个儿的条件控制结构.作为一名经验丰富的 Lisp/Scheme 程序员,
多年来俺见过各种定制的控制结构(如各种循环宏),
但是,没有一个证明是靠谱的.
俺宁愿在更好的语言中写稍稍长点的详细代码,也不愿没接没够的折腾无尽的奇葩控制结构.

其次,即使你天才到发明了另一种更好的控制结构,
Smalltalk 的延迟绑定功能,也难以提供足够的能力来定义它.
函式作为一个抽象工具的能力是有限的.
比Lisp/Scheme 的宏还要不如.

第三,Smalltalk 这一特性并不是新东西,而且包含了一个重大问题.
类似的但更加优美的控制结构,
在计算机科学诞生前就已经由 lambda演算科学定义出来了:


    :::lisp
    TRUE = λx.λy.x
    FALSE = λx.λy.y
    IF = λb.λt.λf.b t f


这是非常漂亮的,可以用任何语言实现的,
但是为毛没有任何一个函式语言以这种方式来实现条件语句?
因为当你看着表达式 `IF b t f` ,
是无法明确这是否为一个条件, 因为 `IF` 是能在程序中重定义的.
又,如果 `IF` 是个函式,
它也可以接受额外的值比如 `TRUE` 或是 `FALSE`.
这样的条件构造可以工作,但是最后总是造成麻烦.
这就是所谓 "无意语义"(unintentional semantics).
而且这种 bug 最难以追查.

这种实现,也令编译器或是静态分析器以及奏效.
设想当编译器遇到 `IF b t f` 时,它无法得知这是否条件判定,从而进行优化.
它只能将其视作普通的函式调用.
同样类型检查器遇到时,它也无从期待 `b` 应该是什么类型,
因为不应该是个条件.
lambda 演算以上参数形式却是可以对应到 Smalltalk 的.


因此,适度使用时,抽象是个好主意,
一但过了,就会事与愿违.

(`译注:`其实什么事儿不是酱紫的呢?)

过度抽象,不仅令代码难以为人理解,
更加令自动分析工具以及编译器难有作为.



## 食脑魔:设计模式
~ Design patterns, the brain eater


OO 语言自我吹嘘他们的抽象弄清,其实抽象以及表述能力都很一般.
很多事儿,使用传统程序语言或是函式语言中很容易作到,
但是在 OO 语言中就变得的很折腾.
这才是为毛出现了 `设计模式`.
其起源的主要原因,就是 `一切皆对象` 的教条以及缺乏高阶函式
(或正确的执行它们),
还有 OO 的神秘主义倾向.

头一次听说它们时,
俺已经在康奈尔大学作为博士生在进行一些 PL 研究了.
平时主要使用 ML 以及 Haskell 语言.
在听到朋友有关
[设计模式(Design Patterns)](http://en.wikipedia.org/wiki/Design_Patterns)
(这书绰号`GoF` ~Gang of Four, 即 `四人帮`)
的高见后,好奇这书的名气,
所以从图书馆借来的.
几个小时内,就发现书里那堆古怪的名称,
可以逐一对应到俺一直在使用的各种编程技术上.
有此是如此基础,其实是存在于每一个高级程序语言中的, 并不需要被命名.
很多高级模式(比如 访问者)只是将函式编程概念变成一个令人费解的形式,
以便避开OO 语言的固有局限性.
后来又发现,
[Peter Norvig](http://en.wikipedia.org/wiki/Peter_Norvig)
早在1998年就指出,
一但你完成了 `高阶函数`(first-class function) ,
大部分设计模式对你将是 "透明的".
这证实了俺的发现 - `我不需要它们`.

俺也得承认,有些设计模式的确精巧.
你真的必须理解 OO 语言的内部设计精髓,
同时也必须理解许多函式编程技术,才足以创建模式.
但是, 智力=/=智慧.
即便它们能作到函式语言作到的,也通常要复杂的多.
选择艰难模式并不能真正证明自个儿的天才.
当你完成了 `高阶函数`(first-class function) ,事儿就变得容易很多,
你甚至于不会注意到用了什么设计模式.
就象
[Peter Norvig](http://en.wikipedia.org/wiki/Peter_Norvig)
形容的,它们会变得的"透明".
那么,良好的语言设计者,应该作的是尽可能增加 `高阶函数`(first-class function) 到语言,
而不是提出设计模式作为解决方案.

(`译注:`无法同意更多!只有减少程序员心智负担的开发语言才是有良心的.)


每次俺从代码中中清除一个设计模式时(其它人写进去的),
代码就变得的更加简洁,易于管理.
前几天,俺终于很欣慰的将最后一个 访问者模式 从俺的 java 代码中给清除了.

(`译注:`指 [PySonar](https://github.com/yinwang0/pysonar2) 工程)

设计模式除了额外的工作,没有赋予俺任何好处.
俺可以作任何事儿,
包括所谓 访问者模式 提供的所有先进东西,
但是,不通过使用神马模式.
另外,俺欠函式编程者有关设计模式一个说法.
如果你真想了解设计模式的精髓,以及如何能不用它们,
[这本分书](http://www.amazon.com/Little-Java-Few-Patterns/dp/0262561158)
是个不错的开始.

(`译注:`指 Dan Friedman 的小字辈儿好书,
参考:[GTF - Great Teacher Friedman](http://www.yinwang.org/blog-cn/2012/07/04/dan-friedman/))


摧悲的是, 设计模式在企业里得到了某种程度上无法忍受的追捧.
当俺在 Google 实习时,在每一个书架上都见到了 `GoF`!
即使你自个儿不用它们,
但是几乎不可能避免其它人向你的代码中倾倒设计模式代码.
其营销战略非常象减肥产品:
"即使你不动,它一样燃烧你的脂肪!"
他们很是蛊惑了一大批新手,
以为无需理解计算机科学的基本概念,只要将几种模式折腾在一起,
就获得了一个漂亮的解决方案.
这看起来美好的象真的似的!
而最终,你将作比希望避免的更多的事儿.
设计模式食空了程序员的大脑!
一但使用设计模式一段时间,
他们就再也看不到其它东西,不会使用明确而直接的方式来写代码了.




## 乜系OO语言?
~ What is an OO language any way?


有关这方面,咱还没有论及什么使一门语言 "面向对象",
又或什么使之不是.
称其为OO语言,只是因为俺能将两个数据字段和一个方法塞到一个记录中?
又或是只有当其也提供 `极迟绑定` 时才算 OO?
那么 继承/重载/等等,等等呢?
是必须同时具有所有特性?还是有任何一个就算OO 了?


事实上,这一命题没有好答案.
本质上根本就不存在 "面向对象语言".
对象可以是语言的一部分,而且只是一小部分.
你真心不能说因为提供了对象的支持,语言就是面向对象的.
所谓的 OO语言是深深植根于传统的过程化编程(PP).
本质上 OOP 的一切都是从 PP 偷走的,
只是加以改名假装是自个儿创造的.


历史上鼓吹OO一直只是市场营销的需要.
一种语言想吸引人注目,就得宣称是 OO 的,
目测现在这点在慢慢改变,
因为越来越多的人意识到了 OO 的问题.


## OO对教育和产业的伤害
~ Harm in education and industry


虽然OO 有很多硬伤,但它在市场上非常成功,而且多年来都处于主导地位.
因为社会以及市场的压力,许多高校也开始使用 OO语言,
如JAVA 作为入门语言, 来取代传统的过程语言,比如 Pacsal,
又或是函式语言,比如 Scheme .
这在很大程度上造成了学生根本没有接触到编程最重要的概念.
OO 强调的唯一重要的事儿就是重用,
但是,怎么能教无法写出可用代码的学习重用?
更何况复审并不是如某些人物所言的那么重要.


在康奈尔和印第安纳大学,俺都作为 TA 使用JAVA 来进行编程入门课程.
用了好几个学期.
清楚的记得学生们是怎么被绕晕的.
他们多数无法理解什么是 `"this"`,
为毛一切都要塞进类里,
为毛每个字段都要私有并使用 `getters`,
方法和静态方法的差异,等等等等...


他们无法理解的一个正当理由是 - OO 并不是描述事情怎么运作的.
多数时候,俺感觉,俺在教授设计上的缺陷和教条.
最终他们只能学到些皮毛.
更杯具的是,那些真心相信OOP 的学生,
将以为能写出令人费解的代码而自豪.
他们再也无法用简洁直接的方式来编写程序了.
这是可悲的.
俺感觉,我们不再教导学生拥有创造性和批判性思维,
而只是批量制造流水线工人.


![yw_modern-times.jpg](http://zoomq.qiniudn.com/ZQCollection/img/yw_modern-times.jpg)


工程方面,OO 并没有证实它宣称的威力.
良好的系统,可能用 "OO 语言"来实现,
但是,往往代码出自真正理解 OOP 的问题,
不盲从 `一切皆对象`或是`设计模式` 的工程师.
优秀程序员,通常在 OO 语言中进行变通,基本上只写传统的过程式的代码,
并结合函数式编程风格.
因此,一些 OOP 语言及其工具可能有非常广泛的应用,
但是,OO风格其实并没有真正对编程领域施加什么大太的推动.


## 终言
~ Final word

那么终究这篇文章想说什么?
对OO语言的圣战?
提倡函数式编程?
都不是,如俺所言, 根本没有所谓 `"面向对象语言"`, 
所以,神马战争,是不存在的.
每一个 OO语言,都包含从过程式语言或是函数式语言借(或偷)来的好东西,
所以,它们也不算完全无用.


但是实话哪,大部分问题究其根源,就是追加的那些个 OO 特性
(死塞到过程编程, PP).
而这些额外的 "真OO技术" 带来的混乱比价值要多的多.
从这点看其价值是微不足道的.
根据俺的经验,
一但接受了哪怕只有一两个 OO 思想,
就将引发一系列麻烦和思维错误中,
且需要很长时间才能醒悟并摆脱.


因此,俺严正建议,表再接受任何 OO方面的想法,
也表试图使用它的 "特性".
OO 就是`食脑魔`,能躲多远躲多远.
但,你依然可以使用 "OO语言" 来生产可用程序,
因为你基本上是以非OO语言来使用它的.



# 是也乎

对于 `王珢` , 关注了太久了,久到成为习惯了... 
但是,认真翻译他翻越后的技术思考成果,还是第一次,可惜也只能用自个儿的语气来快译,真正涉及的所有技术细节,俺还没有能力逐一印证,俺也只是个期望简洁的结论,记忆下来,直接使用的那种知其然,不知所以然的家伙... 

但是,不得不说,对于 OOP 从第N次使用JAVA 败退后,
就一直对 OOP 的编程思想抱有深深的焦虑,
原先总是对自个儿为毛无法自然的对象化所有事物而自我嫌弃,
然后是奇怪为毛不用 OOP 编程反而更加自然,
到最后,沈游侠向俺演示,怎么通过清除 class 令Python代码更短,运行更快... 

这才,从俺的世界观里彻底放弃了 OOP ,但是,一直没有找到为毛这样的根因,现在 王珢完成了这一结论性描述,收藏之!严正推荐之!

PS:

- 有关 `first-class function` 的翻译
- 最初俺是图样图森破的译为 `一流功能`
- 王珢看了, 建议修订为 `高阶函数`
- 很多朋友指出,不对! 应该是 `第一类`/`头等`/`第一级`/`一等公民`...函数
- 我们大汉语的问题,就这样爆发了,多样可重载性...
- 参考:[First-class function - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/First-class_function)
    - 以及 [高阶函数与第一型_Higher-order function and First-class object | Web Development Machine](http://www.webdevelopmentmachine.com/blog/%E9%AB%98%E9%98%B6%E5%87%BD%E6%95%B0%E4%B8%8E%E7%AC%AC%E4%B8%80%E5%9E%8B_higher-order-function-and-first-class-object/) 等等吧
- 俺个人感觉, `高阶函数` 的意向在这儿没有问题,只是我们过往的翻译习惯感觉哪儿有不对了...


# Changlog ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 160322 发现 `王珢` 在原文中给出了俺的翻译链接!
    + [![131224_oop_linkback](http://zoomq.qiniudn.com/ZQCollection/snap/yw/131224_oop_linkback.png)](https://yinwang0.wordpress.com/2013/12/24/oop/)
    + 是也乎,(￣▽￣) 感动!
- 140109 获得`王珢`授权,得以进行传播.
- 140108 前后7.42小时完成快译.
- 131224 翻越抄录在 medium.com
 

## 增订:-o回收 

review 时发现 yw 增补了原blog ,有些段落已经发生了调整,只有回收了:


The programmers' world is full of fads and superstitions. Every now and then there will be somebody come up and announce: "I can save the world!" No matter how bad the ideas are, there will always be followers, and the ideas soon become their religion. They then develop their community or camp, try to make the rest of the world adopt those ideas, and try to make the ideas live forever.

程序猿的世界充斥着各种时髦迷信.不时就有人跳出来吼:"俺能拯救世界!"诡异的是,无论多不靠谱的想法,总有追随者,并快速打造成全站的宗教,结成社区,尽量迫使其它所有人认同,以史这想法永存下去.


Whenever you criticize a programming language or paradigm, people would think you are a proponent of some other language or paradigm. Since I wrote the article pointing out the drawbacks of purely functional programming and monads, some people have apparently taken me as a proponent of object-oriented programming. That's far from the case. I don't like OO at all. I use almost none of the OO techniques even when I write programs in Java.


当你开始批评某编程语言或是范式时,人们就认为你一定是另外某某党的拥趸. 自从俺写文章黒 纯函式 编程以及单子的问题后, 有的就以为俺已经投入到 OOP 的怀抱中了. 图样图森破,俺从来就没有尿过 OOP, 即便在使用JAVA 编程时.


I have a scientific mind. I do research on programming languages and I make some of my own. I have implemented almost every feature in every language. So programming languages have no power upon me. I play with them like toys. I never see a language or a paradigm as a whole. I can dissect them and take the good parts that I liked, and discard the parts that don't work well.

俺具备科学思想.进行过编程语言的研究,而且自行实现过一些. 在任何语言上俺都能实现几乎所有语言特性. 因此,编程语言已经蒙不住俺了.俺能象玩具一般把玩它们, 在俺眼中它们只是一堆零件,可以任意折腾,提取俺喜欢的,丢弃俺不屑的.


Actually in the first version of the previous article I also criticized OOP, but I soon realized that it may not be an interesting topic. I have known the shortcomings of OOP and associate design pattens etc for many years and I thought that most programmers know them, and there is no need to write about them. It turns out that I was wrong. I have lived in my nice little world for too long and forgot how confusing the world can be.

其实以往文章有部分已经对 OOP 吐糟过了,但是,很快反应过来这可能不是个有趣的话题. 俺以为大多数程序猿已经对 OOP 以及关联的设计模式的缺陷,没必要强调了. 然而,事实证明是俺图样图森破了,在自个儿可爱的小世界中呆久了,容易忘记外面的混沌.


I just saw this InfoQ talk by Gilad Bracha today. He dislikes the purely functional cult as much as I do, but unlike me, he has subscribed to another cult that is OOP. Although he made some good points, the general message I got from the talk was that OOP the "one true king" is going to rule the world, and FP will be deconstructed and serve as a subordinate of it. OOP will live forever. This is ridiculous.

刚看到今天 InfoQ 上 Gilad Bracha 的访谈 . 他象俺一样不是性能崇拜者, 但是,他已经是邪恶的OOP 教派成员了, 虽然传达了一些很好的意见,但是,整体上对于 OOP 是"真圣", FP 将解构为 OOP 的下属, 而 OOP 将永存. 这就过了吼!


FP has its problems, but it deserves a lot more respect than this. Although I dislike some purely functional language's cult-like culture, FP in general is highly valued. FP taught me a lot more and contains a lot more value than OOP. The education I received from some of the best FP people made me a better programmer. Even when I use a OO language, I avoid its shortcomings and write in a much cleaner way than the usual OO style. Some OO languages have been learning (or stealing) from FP languages for long and benefitted from it. To make a living, some highly educated FP people work on OO languages, make good compilers or tools for them. I feel terrible that somebody talks about FP that way.

FP 当然有自身的固有问题,但是它值得更多的尊重. 虽然俺不喜欢一些 纯函式 语言邪教般的文化, 但是 FP 具有很高的价值. FP 教了俺很多好东西,含有比 OOP 更多价值. 从那些 FP 程序员身上接受的教导令俺成为更好的程序员. 甚至当我使用一个 面向对象 的语言时, 俺也习惯性的在躲避其缺点, 使用更加简洁的方式来完成功能. 一些 面向对象的语言,其实一直在向 FP 窃取思想而从中受惠. 限于生计, 有些受过 FP 高级教育的程序员,却在为 面向对象的语言工作,为其编写更好的编译或其它工具. 这令俺细思恐极.


Gilad criticized some bad designs in FP, but highly promoted the bad designs from OOP, to the degree of calling them "the one true way". Many aspects of OOP have been bringing harm to the software industry and computer science education for long, but he didn't mentioned them. The more I forget about those ideas from OO, the simpler and better my code becomes. I thought many people have learned these lessons, but it looks that's not true.

Gilad 批评了一些FP 中不好的设计, 但鼓吹 OOP 的设计模式是 "唯一正当"的,这更加要命. 事实上 OOP 对计算机科学的教育以及软件产业已经造成了深远的伤害. 虽然俺自觉的忘记 OOP ,用更加简洁的方式改善代码. 原本以为大家都跟俺一样,但看来现实并非如此.


Thus I realized that my original criticism of OOP had some value, and I decided to write a dedicated article about it.

故此,俺意识到,俺对OOP 的批评具有一定的价值,决定写下来, 好好聊聊.

...


### 过度抽象的代价
~ The cost of excessive abstraction 

The major appeal of OOP is abstraction, but OO programmers usually overdo it. I know the value of abstraction. I build abstractions every day, in all kinds of languages. But OOP advocates a level of abstraction which makes programs hard to understand and hard to analyze. I often see Java programs with multiple levels of inheritance and overloading but doing very little. And worse, because there are so much code that doesn't do real things, it is very hard to find out which part of the code is doing the thing you want.

OOP 的主要吸引力就是抽象,
但是, OO程序猿总是作过头.
俺明白抽象的价值.
每天俺都在各种语言中实践着抽象.
但, OOP 主张构建抽象层,这通常使程序难以理解/分析.
俺经常见到有 JAVA 程序动用多层继承/重载,但实际作的事儿不多.
更糟的是,正因堆砌了如此多的代码,却没有真正在作事儿,
以至于难以找到哪部分是你真正想作的东西.

Whenever you complain about Java or C++, OO proponents will tell you that they are not authentic OO languages. They would ask you to take a look at Smalltalk. If Smalltalk's ways are that good, why almost nobody is using Smalltalk now? Because there are real problems in its approach. The "authentic" OO style of Smalltalk promotes the notion of "extremely late binding", which basically means that the meaning of the program constructs is determined as late as possible.

每当你抱怨 JAVA/C++ 时,OO程序猿就说,那些不是真正的 OO 语言.
一准向你推荐 Smalltalk 的.
但是,如果 Smalltalk 是好的,为毛现在几乎没有人使用 Smalltalk 进行工程开发?
在"正宗"OO 语言 Smalltalk 中,
提倡的风格是 "极迟绑定" (extremely late binding),
意味着,要尽可能晩的确定概念的意义再进行构建.

Late binding means that you have a chance to swap out the underlying implementation without forcing the upper levels to change, but it also means that you are no longer sure what a piece of code means! When I look at expressions such as '1+2′ and 'if (t) then ...  else ... ' in Java or C++, I at least know for sure that they mean an integer addition and an usual conditional. But I'm not sure about this in an "extremely late binding language", because even the meaning of '+' and 'if" can be redefined. A similar problem happens to Lisp family languages' macro systems. It is bad idea of giving the programmers the power of defining control structures, because soon your language will be abundant of quirky control structures designed by programmers who try to be clever.

这样,你有机会换出(swap out)底层实现,
而不用强制变更上层.
但是,同时也意味着你也无法及时明确一段代码究竟会作什么!
比如,在 JAVA 或是 C++ 中看到诸如
`1+2` 或是 `if (t) then ...  else ... ` 的表达式时,
至少俺知道是作整数相加,以及往常一般的条件判别.
但是,若在"极迟绑定"语言中就完全一头雾水了!
因为 `+` 和 `if` 都是可以重新定义的.
类似问题也出现在 Lisp 家族语言的宏体系中.
事实证明,给予程序猿定义控制结构的能力,
这主意很囧,因为立即就会发现,自作聪明的程序猿都在努力向语言里塞满各种特殊的控制结构.


Abstraction is a good idea when used moderately, but when you do it in excess, it backfires. Not only does it make it hard for humans to understand the code, it makes automated analysis tools and compiler optimizations difficult or impossible to make. I built an advanced static analysis tool for Python called PySonar. It works okay in general, but under the premise that the programs don't use the "deep magic" of Python (which are possibly learned from Smalltalk). If you do, there are all sorts of ways you can confuse the analysis, but for that I can do nothing to help. Nothing can analyze or optimize the code if you put expensive or undecidable computations into the abstraction layer.


适度使用时,抽象是个好主意,
一但过了,就会事与愿违.(其实什么事儿不是酱紫的呢?)
过度抽象,不仅令代码难以为人理解,
更加令自动分析工具以及编译器难有作为.
俺创建的先进静态分析工具,
对 Python 的叫 [PySonar](https://github.com/yinwang0/pysonar2).
其一般工作起来还成,
只要没用 Python 玩一些 `深度魔术`(deep magic)
(即前述Smalltalk 中能玩的).
如果你一定要玩,有太多方法可以弄晕分析器,
这时,俺也帮不了你什么了.
你一但将华丽的无法理解的东西塞到抽象层,
那就没有任何东西能帮你分析或是优化代码了!


So is there any value of making those deep abstractions an option but not encouraged to use by usual programmers? There might be, but probably too little to offset the lost safety guarantee and performance.

那么,不鼓励普通程序猿使用深层抽象,有什么价值会丧失?
可能有,但是,一定无法抵消代码失去安全以及性能保障!



...

### Are functions objects? 

The original motivation of putting functions inside objects was to support GUI applications. You click on a button and some code (a callback) will be invoked. For the convenience of referring to the button that gets clicked, the callback takes the triggered object as its first argument. Since the callback does nothing more than this, it seems to be convenient to just store it inside the button. And thus we had an "object" which combines the attributes of the button and its method (the callback). Indeed it is convenient and a good idea. But the limited usage case of GUI applications can't really justify a universal notion of "everything is an object". Computer science often suffers from such over-generalizations.


将函式塞到对象中的原始动机是在 GUI 开发中.点击一个按钮时,一些代码(回调)就应该被触发. 为了指明按了具体哪个按钮,回调的函式就想要一个指代的对象. 因为回调就这么单纯,看起来将其存储在按钮中没有什么不好. 于是我们有了个"对象". 的确挺方便. 但 GUI 应用只是个非常有限的情景,并不能真正证明 "一切皆对象"的普世性. 可惜计算机科学这种过度概括是常态.

But even the above contains a subtle mistake: the callback in the button is not really a method. It is just a usual function. Very few procedures should be considered methods of an object, and most others are just functions. If you look carefully, most of the time the objects just serve as a namespace (or module) in which you can put data fields and functions. But those functions can also live on their own (such as addition of velocities or time). They just take the objects as inputs and produce some output. Only the functions that are most intimately connected to the fields and provide an "abstraction layer" should be considered methods. Most of those are "getters", "setters" or "iterators". Functions don't necessarily belong to objects. They are not objects. They describe a change, transition or transformation of objects. They are external to the objects.


但是,即使上述包含一个微妙的错误:在按钮的回调是不是一个真正的方法. 这只是一个平常的功能. 很少有程序应被视为一个对象的方法,而大多数人都只是功能. 如果你仔细观察,大部分时间的对象只是作为一个命名空间(或模块)中,你可以把数据域和功能. 但是,这些功能也可以生活在他们自己的(如加速度或时间). 他们只是把对象作为输入,并产生一些输出. 只有那些最密切相关的领域,并提供了一个"抽象层"的功能,应考虑方法. 其中大部分是"干将","二传手"或"迭代器". 功能不一定属于对象. 他们不是对象. 他们描述的改变,转变或物体的转型. 它们是外部的对象. 


In some languages such as Scala or Python, functions are also treated as objects. But they actually just wrapped the functions into an object, give them some name such as "apply" or "__call__", so that when the objects are "invoked", you know which functions to call. But putting a function into an object doesn't really mean functions are also objects, just like inviting friends to your house doesn't make them your family.


在一些语言,比如 Scala/Python, 函式也被视作对象.
而实际上,只是将一个函式包装成对象,
然后给予类似 `apply` 或是 `__call__` 的名称,
对象就酱紫能 `invoked` 了,而大家都知道函式只是调用了而已.

但是,将函式塞到对象中,并不等于函式也是对象,
好比,邀请朋友到家里来也不能令他们变成家人.


...


### 一切皆角色(actor) ?

~ Everything is an actor? 

In his talk, Gilad Bracha disagrees with the FP hypes such as monads and pattern matching (with some good points), but he over-valued the ways of OOP and the actor model. From the blog posts he refers to, you can see that he thinks of the actor model as the "one true way".

在 Gilad Bracha 的有关言论中,
他不认同 FP 的炒作,
类似 monads 以及 模式匹配(这有点儿好处),
但他完全高估了 OOP 和角色模式了.
从他的blog 文章中可以看到,他宣称 角色模式是 "唯一正解".


I'm always wary of such notion as "one true way" or "everything is... " I actually read Carl Hewitt's actor model paper a long time ago and also some of his other concepts such as Direct LogicTM (Yes, there is a trademark sign on it). I didn't really appreciate the papers and his way of writing, with the "dedicated to some-big-names" headlines, trademark signs and grand claims.

俺对任何宣称 "唯一..." 或是 "一切..."
的概念有疑虑.
其实很久以前,俺就查阅过 Carl Hewitt 的角色模式论文,
他也描述了其它模式,比如 "Direct LogicTM"
(是的,有商标签注的呢).
这些论文都是标题 "高大上",签注商标以配套宏大的索赔可能性.
俺真心没体会到他论文这种撰写方法有什么意义.


The actor model suffers from the same drawbacks of OOP as I mentioned: over-abstraction and lacking of general expressiveness. There is no way a human being or an automated system can effectively reason about the programs if you build them at way. It hides bugs. Although the actor model may be useful in some cases, it is not really expressive and simple enough to nicely capture all computations. It has too much application-specific logic (which is essentially OOP) built in, thus it is not at the same universal level as lambda calculus or Turing machines.

角色模式有同OOP 一样的毛病,
正如俺所言:过度抽象,缺乏正常的表达能力.
用这种模式创建的程序,
没办法让一个人或是自动系统对其进行有效的推导.
当然,有时,角色模式很有用.
但是,它并不能真正很好的对所有计算进行简洁有效的表述.
它有太多内建的特殊应用逻辑
(这是OOP 的通病),
因此它和 lambda演算以及图灵机 不在一个能力水平上.

...

### 面向对象设计模式的傻缺
~ The stupidity of OO design patterns 

It may not be inherent in all OO languages, but OO design patterns (such names as Factory, Facade, Flyweight, Singleton, Visitor etc) have been the major source of over-complication and confusion. Their origin was mostly due to the dogma of "everything is an object" and the lack of high-order functions (or the correct implementation of them).

可能不是所有 OO 语言固有的,
但 面向对象设计模式 
(类似 Factory, Facade, Flyweight, Singleton, Visitor 等等)
就是代码过度复杂/混乱的根源.
主要原因就是 "一切皆对象" 的教条以及缺乏高阶函式
(或正确的执行它们).


The design patterns are completely nonsense to me and I never used them. When I first heard about them I was already a PhD student at Cornell doing some PL research. I was curious about the book's fame and borrowed one from the library. But I soon found a mapping from all those weird names to the programming techniques I have been using all the time. I don't understand how such a book as GoF can ever be published which contains nothing but just giving new and weird names to existing programming techniques that I use every day. If you say the purpose of writing this book is to "improve communication of programmers", then I would write a book and give new names to air, water and all kinds of food, in order to "improve the communication of all human beings".

这类设计模式完全是胡说八道,
俺从未使用过它们.
头一次听说它们时,
俺已经在康奈尔大学作为博士生在进行一些 PL 研究了.
(Programming Language research,参考:[什么是程序语言的研究](http://zoomq.qiniudn.com/ZQScrapBook/ZqSKM/data/20120910004839/index.html))
因为好奇这书的名气,
所以从图书馆借来的.
很快,俺发现书里那堆古怪的名称,可以逐一对应到俺一直在使用的各种编程技术上.
实在不明白,GoF
(`设计模式` 作者通常叫做 `GoF` ~Gang of Four, 即 `四人帮`)
这书是怎么出版的,
这书中没有任何新知识,
只是将大家每天都在使用的现有编程技术,赋予了新奇的名字.
如果你说这书的目的就是为了 
`改善程序员的沟通`.
那俺就应该写本书,来给空气/水/各种食物赋予全新名称,
以 `改善全人类的沟通`!


Peter Norvig gave a talk on design patterns in 1998 pointing out most of the design patterns will be "transparent" once you have first-class functions. He was too polite to call design patterns nonsense or stupid, but that's implied.

Peter Norvig 在98年就设计模式指出,
一但你完成了 `高阶函数`(first-class function) ,
大部分设计模式对你将是 "透明的".
他其实就是过于文雅的暗示: 设计模式就是废话或是愚蠢的.


Every time I remove a design pattern (some other people made) from PySonar, the code becomes simpler and more manageable. I just removed the last visitor pattern a few days ago, and I felt so relieved. They gave me nothing but extra work when they existed. I can do anything, including a lot more advanced things than those provided by visitor patterns, but without using them.

每次俺从 [PySonar](https://github.com/yinwang0/pysonar2)
中清除一个设计模式(由某些人物,生造出来的),
代码就变得的更加简洁,易于管理.
前几天,俺终于很欣慰的将最后一个 访问者模式 给清除了.
设计模式除了额外的工作,没有赋予俺任何好处.
俺可以作任何事儿,
包括所谓 访问者模式 提供的所有先进东西,
但是,不通用使用模式.

I owe my insights into design patterns to some functional programming people. If you really want to understand the essence of OO design patterns, and how NOT to use them, take a look at this little book other than the GoF one.

...

