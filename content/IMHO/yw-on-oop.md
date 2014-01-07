Title: On object-oriented programming 
Date: 2013-12-24 
Tags: YinWang,Pythonner,Zh 
Slug: 131224-yw-on-oop 

via: http://yinwang0.wordpress.com/2013/12/24/on-object-oriented-programming/

The programmers’ world is full of fads and superstitions. Every now and then there will be somebody come up and announce: “I can save the world!” No matter how bad the ideas are, there will always be followers, and the ideas soon become their religion. They then develop their community or camp, try to make the rest of the world adopt those ideas, and try to make the ideas live forever.

Whenever you criticize a programming language or paradigm, people would think you are a proponent of some other language or paradigm. Since I wrote the article pointing out the drawbacks of purely functional programming and monads, some people have apparently taken me as a proponent of object-oriented programming. That’s far from the case. I don’t like OO at all. I use almost none of the OO techniques even when I write programs in Java.

I have a scientific mind. I do research on programming languages and I make some of my own. I have implemented almost every feature in every language. So programming languages have no power upon me. I play with them like toys. I never see a language or a paradigm as a whole. I can dissect them and take the good parts that I liked, and discard the parts that don’t work well.

Actually in the first version of the previous article I also criticized OOP, but I soon realized that it may not be an interesting topic. I have known the shortcomings of OOP and associate design pattens etc for many years and I thought that most programmers know them, and there is no need to write about them. It turns out that I was wrong. I have lived in my nice little world for too long and forgot how confusing the world can be.

I just saw this InfoQ talk by Gilad Bracha today. He dislikes the purely functional cult as much as I do, but unlike me, he has subscribed to another cult that is OOP. Although he made some good points, the general message I got from the talk was that OOP the “one true king” is going to rule the world, and FP will be deconstructed and serve as a subordinate of it. OOP will live forever. This is ridiculous.

FP has its problems, but it deserves a lot more respect than this. Although I dislike some purely functional language’s cult-like culture, FP in general is highly valued. FP taught me a lot more and contains a lot more value than OOP. The education I received from some of the best FP people made me a better programmer. Even when I use a OO language, I avoid its shortcomings and write in a much cleaner way than the usual OO style. Some OO languages have been learning (or stealing) from FP languages for long and benefitted from it. To make a living, some highly educated FP people work on OO languages, make good compilers or tools for them. I feel terrible that somebody talks about FP that way.

Gilad criticized some bad designs in FP, but highly promoted the bad designs from OOP, to the degree of calling them “the one true way”. Many aspects of OOP have been bringing harm to the software industry and computer science education for long, but he didn’t mentioned them. The more I forget about those ideas from OO, the simpler and better my code becomes. I thought many people have learned these lessons, but it looks that’s not true.

Thus I realized that my original criticism of OOP had some value, and I decided to write a dedicated article about it.

# Is everything an object? 

“Everything is an object” is the favorite dogma of OOP. Now let’s take a look to see if it is true, or if it is a good idea to make it that way.

The generally accepted definition of an object is a combination of “data fields (attributes that describe the object) and associated procedures known as methods.” Can you really fit everything into this model?

First let’s look at the real world and see if this definition can capture everything. Cars, trees, animals may sometimes be thought of as objects, but what about a change of the objects’ position, their velocity and time? What methods do they have? Well, true believers of OOP may give you classes called Velocity or Time, with methods such as addition in them. But do velocity and time really contain these things you call “methods”? They don’t. Those are just your imagination. You can add the velocities or time, but how can velocities or time contain the addition procedure? This is like saying that the integers contain the CPU’s adders.

So the most you can say is that “everything is an object” is a good way of thinking, but that is not true either. The definition of an object implies that a method can only belong to one object, but most of the time it doesn’t make sense thinking of functions as belonging to any object. Say we have the expression 1+2, does the operator ‘+’ belong to 1, or does it belong to 2? You have to make some arbitrary choice. Since you can make a choice, this means the ‘+’ operator doesn’t really belong to either of them. It is inherently outside of the objects.

So thinking of some things as objects may be helpful, but thinking ofeverything as an object is neither true nor useful. Unfortunately, “everything is an object” has been taken as a dogma and the highest standard of OO language design. Some OO languages claim that everything is an object in them. Whenever you notice that something is not an object, somebody will try to make it one. You may succeed in that, but things get very complicated.

The idealism of “everything is an object” is similar to the FP world’s “everything is a function”. Before computer science was conceived there was this thing called lambda calculus. Some people encoded everything including all numbers and all data structures — all in lambdas. One of the encodings of numbers is called the Church numeral. But unlike “everything is an object”, “everything is a function” has never become a dogma. It works in principle but nobody really use them for actual computation, because they are inefficient and they make things complicated.

So “everything is an object” is in some sense on the same track of “everything is a function”, although to a lesser extent and uglier. Good thought exercise, but doesn’t really work well in practice.

# Are functions objects? 

The original motivation of putting functions inside objects was to support GUI applications. You click on a button and some code (a callback) will be invoked. For the convenience of referring to the button that gets clicked, the callback takes the triggered object as its first argument. Since the callback does nothing more than this, it seems to be convenient to just store it inside the button. And thus we had an “object” which combines the attributes of the button and its method (the callback). Indeed it is convenient and a good idea. But the limited usage case of GUI applications can’t really justify a universal notion of “everything is an object”. Computer science often suffers from such over-generalizations.

But even the above contains a subtle mistake: the callback in the button is not really a method. It is just a usual function. Very few procedures should be considered methods of an object, and most others are just functions. If you look carefully, most of the time the objects just serve as a namespace (or module) in which you can put data fields and functions. But those functions can also live on their own (such as addition of velocities or time). They just take the objects as inputs and produce some output. Only the functions that are most intimately connected to the fields and provide an “abstraction layer” should be considered methods. Most of those are “getters”, “setters” or “iterators”. Functions don’t necessarily belong to objects. They are not objects. They describe a change, transition or transformation of objects. They are external to the objects.

In some languages such as Scala or Python, functions are also treated as objects. But they actually just wrapped the functions into an object, give them some name such as “apply” or “__call__”, so that when the objects are “invoked”, you know which functions to call. But putting a function into an object doesn’t really mean functions are also objects, just like inviting friends to your house doesn’t make them your family.


# The cost of excessive abstraction 

The major appeal of OOP is abstraction, but OO programmers usually overdo it. I know the value of abstraction. I build abstractions every day, in all kinds of languages. But OOP advocates a level of abstraction which makes programs hard to understand and hard to analyze. I often see Java programs with multiple levels of inheritance and overloading but doing very little. And worse, because there are so much code that doesn’t do real things, it is very hard to find out which part of the code is doing the thing you want.

Whenever you complain about Java or C++, OO proponents will tell you that they are not authentic OO languages. They would ask you to take a look at Smalltalk. If Smalltalk’s ways are that good, why almost nobody is using Smalltalk now? Because there are real problems in its approach. The “authentic” OO style of Smalltalk promotes the notion of “extremely late binding”, which basically means that the meaning of the program constructs is determined as late as possible.

Late binding means that you have a chance to swap out the underlying implementation without forcing the upper levels to change, but it also means that you are no longer sure what a piece of code means! When I look at expressions such as ’1+2′ and ‘if (t) then … else …’ in Java or C++, I at least know for sure that they mean an integer addition and an usual conditional. But I’m not sure about this in an “extremely late binding language”, because even the meaning of ‘+’ and ‘if” can be redefined. A similar problem happens to Lisp family languages’ macro systems. It is bad idea of giving the programmers the power of defining control structures, because soon your language will be abundant of quirky control structures designed by programmers who try to be clever.

Abstraction is a good idea when used moderately, but when you do it in excess, it backfires. Not only does it make it hard for humans to understand the code, it makes automated analysis tools and compiler optimizations difficult or impossible to make. I built an advanced static analysis tool for Python called PySonar. It works okay in general, but under the premise that the programs don’t use the “deep magic” of Python (which are possibly learned from Smalltalk). If you do, there are all sorts of ways you can confuse the analysis, but for that I can do nothing to help. Nothing can analyze or optimize the code if you put expensive or undecidable computations into the abstraction layer.

So is there any value of making those deep abstractions an option but not encouraged to use by usual programmers? There might be, but probably too little to offset the lost safety guarantee and performance.

# Everything is an actor? 

In his talk, Gilad Bracha disagrees with the FP hypes such as monads and pattern matching (with some good points), but he over-valued the ways of OOP and the actor model. From the blog posts he refers to, you can see that he thinks of the actor model as the “one true way”.

I’m always wary of such notion as “one true way” or “everything is…” I actually read Carl Hewitt’s actor model paper a long time ago and also some of his other concepts such as Direct LogicTM (Yes, there is a trademark sign on it). I didn’t really appreciate the papers and his way of writing, with the “dedicated to some-big-names” headlines, trademark signs and grand claims.

The actor model suffers from the same drawbacks of OOP as I mentioned: over-abstraction and lacking of general expressiveness. There is no way a human being or an automated system can effectively reason about the programs if you build them at way. It hides bugs. Although the actor model may be useful in some cases, it is not really expressive and simple enough to nicely capture all computations. It has too much application-specific logic (which is essentially OOP) built in, thus it is not at the same universal level as lambda calculus or Turing machines.

# The stupidity of OO design patterns 

It may not be inherent in all OO languages, but OO design patterns (such names as Factory, Facade, Flyweight, Singleton, Visitor etc) have been the major source of over-complication and confusion. Their origin was mostly due to the dogma of “everything is an object” and the lack of high-order functions (or the correct implementation of them).

The design patterns are completely nonsense to me and I never used them. When I first heard about them I was already a PhD student at Cornell doing some PL research. I was curious about the book’s fame and borrowed one from the library. But I soon found a mapping from all those weird names to the programming techniques I have been using all the time. I don’t understand how such a book as GoF can ever be published which contains nothing but just giving new and weird names to existing programming techniques that I use every day. If you say the purpose of writing this book is to “improve communication of programmers”, then I would write a book and give new names to air, water and all kinds of food, in order to “improve the communication of all human beings”.

Peter Norvig gave a talk on design patterns in 1998 pointing out most of the design patterns will be “transparent” once you have first-class functions. He was too polite to call design patterns nonsense or stupid, but that’s implied.

Every time I remove a design pattern (some other people made) from PySonar, the code becomes simpler and more manageable. I just removed the last visitor pattern a few days ago, and I felt so relieved. They gave me nothing but extra work when they existed. I can do anything, including a lot more advanced things than those provided by visitor patterns, but without using them.

I owe my insights into design patterns to some functional programming people. If you really want to understand the essence of OO design patterns, and how NOT to use them, take a look at this little book other than the GoF one.

# What the heck is OO? 
If some concepts of FP are white elephants, then most of the OO concepts are emperor’s new clothes.

“OO” has never been a coherent concept. In the beginning it claims to be able to save the world by having all those nice things such as abstract data types, inheritance, overloading, encapsulation etc etc. As those marketing hypes fail one after another, OO supporters make excuses. They started to claim that some elements, such as inheritance, are not the true element of OO.

The meaning of “object-oriented” is always vague and shifting. OO supporters can change the term’s meaning at any time to their advantages. You can be called an OO language at one moment, and then be called a non-OO language just a few minutes later, depending on what they need. When they need to claim that “OOP rules the world”, they would say that you are an OO language because you have something which contains both data fields and procedures, thus satisfying the definition of an “object”. When you are criticized by users for your shortcomings, they would say that you are not an OO language because you don’t have “extremely late binding” etc etc, …

# The harm of OOP

Although purely functional programming has a cult-like culture, it at least contains something we can learn. On the contrary, OOP is almost pure stupidity and cult. In comparison to the recent popularity of FP, OOP has been there longer, so the harm is much deeper. Some years ago, almost every language tried to be OO just because of it is a good marketing word that the companies were looking for. Later on, many companies bought the concept of so-called “OO design patterns” and write convoluted code, and only by now some of them realized that they were wrong.

The harm of OO is deep into education. It is destroying computer science departments. Many colleges use OO languages such as Java as their introductory language, which cause the students’ failure to learn the most essential concepts of programming.

In industry, OO hasn’t really proved its effectiveness with evidence. Good systems may be built in a “OO language”, but the code is often written by people who understand the problems of OO and don’t embrace “everything is an object” or “design patterns”. All the good programmers use workarounds in OO languages and are essentially writing in a style that’s not really OO. So some OO language and its tools may be pretty successful, but the OO style has largely failed.

OO encourages code reusing, but we want something expressive, bug-free and fast. The OO style and OO design patterns produce convoluted code which confuses even its own author. Lots of times people can’t bear with the bugs but can’t understand the code, thus they end up rewriting the code on their own.

The programming languages world has cared too much about styles, paradigms and code reusing, this is why such things as OO and design patterns can have a chance to fool lots of people. Styles and paradigms may help, but they don’t solve actual problems. There really is no such “one true way” to follow as some people believe. Not only that OOP will not rule the world, it will leave very little impact on the future of programming.


====================================================================

>>> 试理解

程序猿的世界充斥着各种时髦迷信.不时就有人跳出来吼:”俺能拯救世界!”诡异的是,无论多不靠谱的想法,总有追随者,并快速打造成全站的宗教,结成社区,尽量迫使其它所有人认同,以史这想法永存下去.


当你开始批评某编程语言或是范式时,人们就认为你一定是另外某某党的拥趸. 自从俺写文章黒 纯函式 编程以及单子的问题后, 有的就以为俺已经投入到 OOP 的怀抱中了. 图样图森破,俺从来就没有尿过 OOP, 即便在使用JAVA 编程时.

俺具备科学思想.进行过编程语言的研究,而且自行实现过一些. 在任何语言上俺都能实现几乎所有语言特性. 因此,编程语言已经蒙不住俺了.俺能象玩具一般把玩它们, 在俺眼中它们只是一堆零件,可以任意折腾,提取俺喜欢的,丢弃俺不屑的.

其实以往文章有部分已经对 OOP 吐糟过了,但是,很快反应过来这可能不是个有趣的话题. 俺以为大多数程序猿已经对 OOP 以及关联的设计模式的缺陷,没必要强调了. 然而,事实证明是俺图样图森破了,在自个儿可爱的小世界中呆久了,容易忘记外面的混沌.

刚看到今天 InfoQ 上 Gilad Bracha 的访谈 . 他象俺一样不是性能崇拜者, 但是,他已经是邪恶的OOP 教派成员了, 虽然传达了一些很好的意见,但是,整体上对于 OOP 是”真圣”, FP 将解构为 OOP 的下属, 而 OOP 将永存. 这就过了吼!

FP 当然有自身的固有问题,但是它值得更多的尊重. 虽然俺不喜欢一些 纯函式 语言邪教般的文化, 但是 FP 具有很高的价值. FP 教了俺很多好东西,含有比 OOP 更多价值. 从那些 FP 程序员身上接受的教导令俺成为更好的程序员. 甚至当我使用一个 面向对象 的语言时, 俺也习惯性的在躲避其缺点, 使用更加简洁的方式来完成功能. 一些 面向对象的语言,其实一直在向 FP 窃取思想而从中受惠. 限于生计, 有些受过 FP 高级教育的程序员,却在为 面向对象的语言工作,为其编写更好的编译或其它工具. 这令俺细思恐极.

Gilad 批评了一些FP 中不好的设计, 但鼓吹 OOP 的设计模式是 “唯一正当”的,这更加要命. 事实上 OOP 对计算机科学的教育以及软件产业已经造成了深远的伤害. 虽然俺自觉的忘记 OOP ,用更加简洁的方式改善代码. 原本以为大家都跟俺一样,但看来现实并非如此.

故此,俺意识到,俺对OOP 的批评具有一定的价值,决定写下来, 好好聊聊.

## 一切都是对象 ? Is everything an object? 

“一切皆对象” 这是OOP 们最喜欢的教条. 现在来谈谈这货是否真如其宣称的这么好.

通常被接受的对象定义是: “数据字段”(描述对象的属性)以及关联方法 的结合体.
你真能在所有情景中适应这种模式嘛?

首先来设想一下OOP 模式是否能对真实世界加以解释. 汽车/树木/动物 视作对象的话, 那么它们的位置/速度/时间的 变化 乍说? 有什么对应的方法? 好吧, OOP 信徒可能叫你将类称为 速度 或是 时间 然后将方法增加进去. 可是速度/时间真的含有这种称为”方法”的东西 ? 当然没有, 这不过是想象罢了. 你可以追加速度/时间,但是,怎么令其包含 加处理? 这简直就象说该整数包含 CPU 的加法器.

哪,信徒们最常说的:”一切皆对象”只是种好的思维方法,但事实并非如此. 一个对象的定义意味着一个方法只能属于一个对象,但大部分时间此思想并没有作用于任何对象. 当我们论及表达式: 1+2 , 是否得说 “+” 属于 1 ,或是算 2 的? 你必须作出属性方法归属的选择,而选择本身就已经意味着 “+” 操作其实并不真正属于任何一个对象,而是固有在对象之外的.

只能说 有些 事儿上对象是有帮助的,而 一切 皆对象这事儿即不真实也无用. 悲摧的是, “一切皆对象” 已经成为面向对象语言设计的最高教条. 一些面向对象语言声称在其内部真的一切都是对象. 若你意识到什么不是对象时,就有人会跳出来整成对象. 当然聪明人可以作到这点,只是事儿就变的复杂起来.

“一切皆对象” 的理想完全类似 FP 世界里 “一切皆函式” . 以前计算机科学称这种构想叫 lambda算子(lambda calculus). 有人就在编码时,将所有数字/数据结构都给包含在 lambda 中了.而这种包含了一切的东西叫Church numeral. 但是,相比 “一切皆对象”, “一切皆无函式” 复合材料没有教条化过. 这只是在理论上是可行的,但是,在实际工程中没有人这么折腾,因为这会令事儿变的复杂,而且效率低下.

因此”一切皆对象” 在某种意义上是 “一切皆函式” 的同位素, 理论上是美好的,但是从未在实际工程中很好的工作过.

## 方法对象 ? Are functions objects?

将函式塞到对象中的原始动机是在 GUI 开发中.点击一个按钮时,一些代码(回调)就应该被触发. 为了指明按了具体哪个按钮,回调的函式就想要一个指代的对象. 因为回调就这么单纯,看起来将其存储在按钮中没有什么不好. 于是我们有了个”对象”. 的确挺方便. 但 GUI 应用只是个非常有限的情景,并不能真正证明 “一切皆对象”的普世性. 可惜计算机科学这种过度概括是常态.

But even the above contains a subtle mistake: the callback in the button is not really a method. It is just a usual function. Very few procedures should be considered methods of an object, and most others are just functions. If you look carefully, most of the time the objects just serve as a namespace (or module) in which you can put data fields and functions. But those functions can also live on their own (such as addition of velocities or time). They just take the objects as inputs and produce some output. Only the functions that are most intimately connected to the fields and provide an “abstraction layer” should be considered methods. Most of those are “getters”, “setters” or “iterators”. Functions don’t necessarily belong to objects. They are not objects. They describe a change, transition or transformation of objects. They are external to the objects.

但是，即使上述包含一个微妙的错误：在按钮的回调是不是一个真正的方法。这只是一个平常的功能。很少有程序应被视为一个对象的方法，而大多数人都只是功能。如果你仔细观察，大部分时间的对象只是作为一个命名空间（或模块）中，你可以把数据域和功能。但是，这些功能也可以生活在他们自己的（如加速度或时间）。他们只是把对象作为输入，并产生一些输出。只有那些最密切相关的领域，并提供了一个“抽象层”的功能，应考虑方法。其中大部分是“干将”，“二传手”或“迭代器”。功能不一定属于对象。他们不是对象。他们描述的改变，转变或物体的转型。它们是外部的对象。

In some languages such as Scala or Python, functions are also treated as objects. But they actually just wrapped the functions into an object, give them some name such as “apply” or “__call__”, so that when the objects are “invoked”, you know which functions to call. But putting a function into an object doesn’t really mean functions are also objects, just like inviting friends to your house doesn’t make them your family.

## The cost of excessive abstraction 

The major appeal of OOP is abstraction, but OO programmers usually overdo it. I know the value of abstraction. I build abstractions every day, in all kinds of languages. But OOP advocates a level of abstraction which makes programs hard to understand and hard to analyze. I often see Java programs with multiple levels of inheritance and overloading but doing very little. And worse, because there are so much code that doesn’t do real things, it is very hard to find out which part of the code is doing the thing you want.

Whenever you complain about Java or C++, OO proponents will tell you that they are not authentic OO languages. They would ask you to take a look at Smalltalk. If Smalltalk’s ways are that good, why almost nobody is using Smalltalk now? Because there are real problems in its approach. The “authentic” OO style of Smalltalk promotes the notion of “extremely late binding”, which basically means that the meaning of the program constructs is determined as late as possible.

Late binding means that you have a chance to swap out the underlying implementation without forcing the upper levels to change, but it also means that you are no longer sure what a piece of code means! When I look at expressions such as ’1+2′ and ‘if (t) then … else …’ in Java or C++, I at least know for sure that they mean an integer addition and an usual conditional. But I’m not sure about this in an “extremely late binding language”, because even the meaning of ‘+’ and ‘if” can be redefined. A similar problem happens to Lisp family languages’ macro systems. It is bad idea of giving the programmers the power of defining control structures, because soon your language will be abundant of quirky control structures designed by programmers who try to be clever.

Abstraction is a good idea when used moderately, but when you do it in excess, it backfires. Not only does it make it hard for humans to understand the code, it makes automated analysis tools and compiler optimizations difficult or impossible to make. I built an advanced static analysis tool for Python called PySonar. It works okay in general, but under the premise that the programs don’t use the “deep magic” of Python (which are possibly learned from Smalltalk). If you do, there are all sorts of ways you can confuse the analysis, but for that I can do nothing to help. Nothing can analyze or optimize the code if you put expensive or undecidable computations into the abstraction layer.

So is there any value of making those deep abstractions an option but not encouraged to use by usual programmers? There might be, but probably too little to offset the lost safety guarantee and performance.

## Everything is an actor? 

In his talk, Gilad Bracha disagrees with the FP hypes such as monads and pattern matching (with some good points), but he over-valued the ways of OOP and the actor model. From the blog posts he refers to, you can see that he thinks of the actor model as the “one true way”.

I’m always wary of such notion as “one true way” or “everything is…” I actually read Carl Hewitt’s actor model paper a long time ago and also some of his other concepts such as Direct LogicTM (Yes, there is a trademark sign on it). I didn’t really appreciate the papers and his way of writing, with the “dedicated to some-big-names” headlines, trademark signs and grand claims.

The actor model suffers from the same drawbacks of OOP as I mentioned: over-abstraction and lacking of general expressiveness. There is no way a human being or an automated system can effectively reason about the programs if you build them at way. It hides bugs. Although the actor model may be useful in some cases, it is not really expressive and simple enough to nicely capture all computations. It has too much application-specific logic (which is essentially OOP) built in, thus it is not at the same universal level as lambda calculus or Turing machines.

# The stupidity of OO design patterns 

It may not be inherent in all OO languages, but OO design patterns (such names as Factory, Facade, Flyweight, Singleton, Visitor etc) have been the major source of over-complication and confusion. Their origin was mostly due to the dogma of “everything is an object” and the lack of high-order functions (or the correct implementation of them).

The design patterns are completely nonsense to me and I never used them. When I first heard about them I was already a PhD student at Cornell doing some PL research. I was curious about the book’s fame and borrowed one from the library. But I soon found a mapping from all those weird names to the programming techniques I have been using all the time. I don’t understand how such a book as GoF can ever be published which contains nothing but just giving new and weird names to existing programming techniques that I use every day. If you say the purpose of writing this book is to “improve communication of programmers”, then I would write a book and give new names to air, water and all kinds of food, in order to “improve the communication of all human beings”.

Peter Norvig gave a talk on design patterns in 1998 pointing out most of the design patterns will be “transparent” once you have first-class functions. He was too polite to call design patterns nonsense or stupid, but that’s implied.

Every time I remove a design pattern (some other people made) from PySonar, the code becomes simpler and more manageable. I just removed the last visitor pattern a few days ago, and I felt so relieved. They gave me nothing but extra work when they existed. I can do anything, including a lot more advanced things than those provided by visitor patterns, but without using them.

I owe my insights into design patterns to some functional programming people. If you really want to understand the essence of OO design patterns, and how NOT to use them, take a look at this little book other than the GoF one.

# What the heck is OO? 
If some concepts of FP are white elephants, then most of the OO concepts are emperor’s new clothes.

“OO” has never been a coherent concept. In the beginning it claims to be able to save the world by having all those nice things such as abstract data types, inheritance, overloading, encapsulation etc etc. As those marketing hypes fail one after another, OO supporters make excuses. They started to claim that some elements, such as inheritance, are not the true element of OO.

The meaning of “object-oriented” is always vague and shifting. OO supporters can change the term’s meaning at any time to their advantages. You can be called an OO language at one moment, and then be called a non-OO language just a few minutes later, depending on what they need. When they need to claim that “OOP rules the world”, they would say that you are an OO language because you have something which contains both data fields and procedures, thus satisfying the definition of an “object”. When you are criticized by users for your shortcomings, they would say that you are not an OO language because you don’t have “extremely late binding” etc etc, …

# The harm of OOP
Although purely functional programming has a cult-like culture, it at least contains something we can learn. On the contrary, OOP is almost pure stupidity and cult. In comparison to the recent popularity of FP, OOP has been there longer, so the harm is much deeper. Some years ago, almost every language tried to be OO just because of it is a good marketing word that the companies were looking for. Later on, many companies bought the concept of so-called “OO design patterns” and write convoluted code, and only by now some of them realized that they were wrong.

The harm of OO is deep into education. It is destroying computer science departments. Many colleges use OO languages such as Java as their introductory language, which cause the students’ failure to learn the most essential concepts of programming.

In industry, OO hasn’t really proved its effectiveness with evidence. Good systems may be built in a “OO language”, but the code is often written by people who understand the problems of OO and don’t embrace “everything is an object” or “design patterns”. All the good programmers use workarounds in OO languages and are essentially writing in a style that’s not really OO. So some OO language and its tools may be pretty successful, but the OO style has largely failed.

OO encourages code reusing, but we want something expressive, bug-free and fast. The OO style and OO design patterns produce convoluted code which confuses even its own author. Lots of times people can’t bear with the bugs but can’t understand the code, thus they end up rewriting the code on their own.

The programming languages world has cared too much about styles, paradigms and code reusing, this is why such things as OO and design patterns can have a chance to fool lots of people. Styles and paradigms may help, but they don’t solve actual problems. There really is no such “one true way” to follow as some people believe. Not only that OOP will not rule the world, it will leave very little impact on the future of programming.

## 是也乎

 对于 王珢, 关注了很久了,久到成为习惯了…
但是,认真翻译他翻越后的技术思考成果,还是第一次,可惜也只能用自个儿的语气来快译,真正涉及的所有技术细节,俺还没有能力逐一印证,俺也只是个期望知道个认同的结论,记忆下来,直接使用的那种知其然,不知所以然的家伙…

但是,不得不说,对于 OOP 从第N次使用JAVA 败退后,就一直对 OOP 的编程思想抱有深深的焦虑,原先是对自个儿为毛无法自然的对象化所有事物而自我嫌弃,然后是奇怪为毛不用 OOP 编程反而更加自然,到最后,沈游侠向俺演示,怎么通过清除 class 关键词令脚本的代码更短,运行更快…彻底放弃了 OOP 俺的世界观,但是,一直没有找到为毛这样的根因,现在 王珢完成了这一结论性描述,收藏之!

## Changlog

- 140105 前后2小时翻译42%
- 131224 翻越抄录在 medium.com
 