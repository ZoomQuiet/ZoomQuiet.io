Title: Tests and static analysis
Date: 2013-11-27 
Tags: YinWang,Pythonner,Zh 
Slug: 131127-yw-on-test-static-analysis 


via: http://yinwang0.wordpress.com/2013/12/27/tests-and-static-anaysis/

Ever since I made a static analysis tool for Python called PySonar, I have been asked about the question: "What is the difference between testing and static analysis?" I just replied to a comment asking a similar question, so I think it's a good time to write down some systematic answer for this question.

## Static analysis is static, tests are dynamic 

Static analysis and tests are similar in their purposes. They are both tools for improving code quality. But they are very different in nature: static analysis is static, but tests are dynamic. "Static" basically means "without running the program".

Static analysis is similar to the compiler's type checker but usually a lot more powerful. It can find bugs that type checkers cannot find, such as resource leaks, array index out of bounds, security risks etc. Static analysis has the "reasoning power" that tests hasn't, so static analysis can find problems that testing may never detect. For example, a security static analysis may show you how your website can be hacked after a series of events.

Tests just run the programs with certain inputs. They are fully dynamic, so you can't test all cases but just some of them. But because tests run dynamically, they may detect bugs that static analysis can't find. For example, tests may find that your algorithm produces wrong results. Static analysis tools are not (yet) intelligent enough for checking this kind of high-level properties.

But notice that although tests can tell you that your algorithm is wrong, they can't tell you that it is correct. To guarantee the correctness of programs is terribly harder than tests or static analysis. You need a mechanical proof of the program's correctness, which means at the moment that you need a theorem prover such as Coq, Isabelle or ACL2, lots of math/logics knowledge, lots of time, and even with all those you may not be able to prove it, because your program may have encoded the Goldbach conjecture in it. So the program's passing the tests doesn't mean it is correct. It only means that you haven't done terribly stupid things.

##  Huge difference in manual labor 

Testing requires lots of manual work. Tests for "silly bugs" (such as null pointer dereference) are very boring and tedious to make. Because of thedesign flaws of lots of programming languages, those things can happen anywhere in the code, so you need a good coverage in order to prevent them.

You can't just make sure that every line of the code is covered by the tests, you need good path coverage. But in the worst case, the number of execution paths of the program is exponential to its size, so it is almost impossible to get good path coverage however careful you are.

On the other hand, static analysis is fully automatic. It explores all paths in the program systematically, so you get very high path coverage for free. Because of the exponential algorithm complexity exploring the paths, static analysis tools may use some heuristics to cut down running time, so the coverage may not be 100%, but it's still enormously higher than any human test writer can get.

## Static analysis is symbolic 

Even when you get good path coverage in tests, you may still miss lots of bugs. Because you can only pass specific values into the tests, the code can still crash at the values that you haven't tested. In comparison, static analysis processes the code symbolically. It doesn't assume specific values for variables. It reasons about all possible values for every variable.

The most powerful static analysis tools can keep track of specific ranges of the numbers that the variables represent, so they may statically detect bugs such as "array index out of bound" etc. (PySonar hasn't that kind of power yet and I'm working towards that.) Tests may detect those bugs too, but only if you pass them specific values that hits the boundary conditions. Those tests are painful to make, because the indexes may come after a series of arithmetic operations. You will have a hard time finding the cases where the final result can hit the boundary.

## Static analysis has false positives 

Some static analysis tools may be designed to be conservative. That is, whenever it is unsure, it can assume that the worst things can happen and issue a warning: "You may have a problem here." Thus in principle it can tell you whenever some code may cause trouble. But a lot of times the bugs may never happen, this is called a false positive. This is like your doctor misdiagnosed you to have some disease which you don't have. Lots of the work in building static analysis tools is about how to reduce the false positive rate, so that the users don't lose faith in the diagnosis reports.

Tests don't have false positives, because when they fail your program will surely fail under those conditions.

## The value of static analysis 

Although static analysis tools don't have the power to guarantee the correctness of programs, they are the most powerful bug-finding tools that don't need lots of manual labor. They can prevent lots of the silly bugs that we spend a lot of time and energy writing tests for. Some of those bugs are so stupid but so easy to make. Once they happen they may crash an airplane or launch a missile. So static analysis is a very useful and valuable tool. It takes over the mindless and tedious jobs from human testers so that they can focus on more intellectual and interesting tests.


>>> 试理解::

# 测试与静态分析 
自从俺折腾了Python静态代码分析工具 PySonar, 俺就问过自个儿这个问题:"究竟测试和静态分析的差异在哪儿?" 这不是一个简单的评注就能回答的了的,现在俺想可以好好解释一下了.

## 静态分析是静态的,测试是动态的 

Static analysis is static, tests are dynamic Static analysis and tests are similar in their purposes. They are both tools for improving code quality. But they are very different in nature: static analysis is static, but tests are dynamic. "Static" basically means "without running the program".

Static analysis is similar to the compiler's type checker but usually a lot more powerful. It can find bugs that type checkers cannot find, such as resource leaks, array index out of bounds, security risks etc. Static analysis has the "reasoning power" that tests hasn't, so static analysis can find problems that testing may never detect. For example, a security static analysis may show you how your website can be hacked after a series of events.

Tests just run the programs with certain inputs. They are fully dynamic, so you can't test all cases but just some of them. But because tests run dynamically, they may detect bugs that static analysis can't find. For example, tests may find that your algorithm produces wrong results. Static analysis tools are not (yet) intelligent enough for checking this kind of high-level properties.

But notice that although tests can tell you that your algorithm is wrong, they can't tell you that it is correct. To guarantee the correctness of programs is terribly harder than tests or static analysis. You need a mechanical proof of the program's correctness, which means at the moment that you need a theorem prover such as Coq, Isabelle or ACL2, lots of math/logics knowledge, lots of time, and even with all those you may not be able to prove it, because your program may have encoded the Goldbach conjecture in it. So the program's passing the tests doesn't mean it is correct. It only means that you haven't done terribly stupid things.

## 存在巨大的人肉工作量差异 
~ Huge difference in manual labor 

Testing requires lots of manual work. Tests for "silly bugs" (such as null pointer dereference) are very boring and tedious to make. Because of thedesign flaws of lots of programming languages, those things can happen anywhere in the code, so you need a good coverage in order to prevent them.

You can't just make sure that every line of the code is covered by the tests, you need good path coverage. But in the worst case, the number of execution paths of the program is exponential to its size, so it is almost impossible to get good path coverage however careful you are.

On the other hand, static analysis is fully automatic. It explores all paths in the program systematically, so you get very high path coverage for free. Because of the exponential algorithm complexity exploring the paths, static analysis tools may use some heuristics to cut down running time, so the coverage may not be 100%, but it's still enormously higher than any human test writer can get.

## 静态分析是符号化的 
~ Static analysis is symbolic 

Even when you get good path coverage in tests, you may still miss lots of bugs. Because you can only pass specific values into the tests, the code can still crash at the values that you haven't tested. In comparison, static analysis processes the code symbolically. It doesn't assume specific values for variables. It reasons about all possible values for every variable.

The most powerful static analysis tools can keep track of specific ranges of the numbers that the variables represent, so they may statically detect bugs such as "array index out of bound" etc. (PySonar hasn't that kind of power yet and I'm working towards that.) Tests may detect those bugs too, but only if you pass them specific values that hits the boundary conditions. Those tests are painful to make, because the indexes may come after a series of arithmetic operations. You will have a hard time finding the cases where the final result can hit the boundary.

## 静态分析会误报 
~ Static analysis has false positives 

Some static analysis tools may be designed to be conservative. That is, whenever it is unsure, it can assume that the worst things can happen and issue a warning: "You may have a problem here." Thus in principle it can tell you whenever some code may cause trouble. But a lot of times the bugs may never happen, this is called a false positive. This is like your doctor misdiagnosed you to have some disease which you don't have. Lots of the work in building static analysis tools is about how to reduce the false positive rate, so that the users don't lose faith in the diagnosis reports.

Tests don't have false positives, because when they fail your program will surely fail under those conditions.

## 静态分析的价值 
~The value of static analysis 

虽然静态分析工具并不能确保程序的正确性,但却是最强力的bug调查工具,而且不需要大量的手工劳动. 以往我们花费了巨大工作量编写的测试依然包含极其愚蠢的错误.有的蠢到你无法相信是自个儿写出来的.而这种低级问题一但出现,就可能令飞机坠毁导弹发射! 因此,静态分析是种非常有用以及有价值的工具.能接管测试人员盲目而乏味的工作,使人类测试工程师能专注更加智能/有趣的测试.

## Changlog

- 14010? 
- 131212 翻越抄录在 medium.com 开始翻译
 
