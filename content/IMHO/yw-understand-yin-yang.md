Title: Understanding the yin-yang puzzle
Date: 2012-07-27
Tags: Think,yinwang,Chinese
Slug: yw-yang-puzzle


via: http://yinwang0.wordpress.com/2012/07/27/yin-yang-puzzle/

![yinyang.gif](http://yinwang0.files.wordpress.com/2012/07/yinyang.gif?w=300)

I have a friend who is a very fast learner. I introduced him to the Scheme programming language a few days ago and he soon digged into this [yin-yang puzzle](http://stackoverflow.com/questions/2694679/how-does-the-yin-yang-puzzle-work):


    :::lisp
    (let* ((yin
            ((lambda (cc) (display #\@) cc) (call/cc (lambda (c) c))))
           (yang
            ((lambda (cc) (display #\*) cc) (call/cc (lambda (c) c)))))
      (yin yang))


This program prints out the infinite string @*@**@***@****@*****@****** …

Why does this happen? This took me almost a full afternoon to figure out. It is always good to have friends who feed you with questions and challenges. I’m going to document my finding here. I may want to make some animated slides (as is always a good idea) later, but for now a short note may suffice.

## The Plan

You will probably never understand the program if you examine the contents of the stack. You need their high level semantic meaning to think clearly. The higher level meaning of the stack is the continuation. So instead of frightening you with the details of the stack, I’m going to use functions to show the continuations explicitly.

Also I will use a little bit of compiler optimizations along the way. The optimizations will simplify the program and show its deeper meanings.

Here is an overall plan of this article:

1. Find the functional representations of the two continuations. Name them c1 and c1.
1. Plug in c1 and c2 into the places of the two call/cc’s.
1. Simplify the program using compiler optimizations.
1. Perform behavioral analysis on the simplified program.

## Transform and Remove Call/cc

So here we go. Let’s repeat the original program here:

:::lisp
(let* ((yin
        ((lambda (cc) (display #\@) cc) (call/cc (lambda (c) c))))   ; B1
       (yang
        ((lambda (cc) (display #\*) cc) (call/cc (lambda (c) c)))))  ; B2
  (yin yang))


Note that there are two binding clauses, B1 and B2, each prints a char and binds a continuation to a variable.

B1 binds yin to the “current continuation” of the first call/cc. Let’s call this continuation c1. Its function representation is:

:::lisp
(lambda (k)
  (let* ((yin
          ((lambda (cc) (display #\@) cc) k))           
         (yang
          ((lambda (cc) (display #\*) cc) (call/cc (lambda (c) c)))))          
    (yin yang)))

We can simplify it using some compiler optimization tricks. I will go very slowly here just in case you are not familiar with compiler optimizations.

First, since Scheme is a strict language, k will be a pure value (with no side-effects), so we can lift the side-effect (display #\@) out:

(lambda (k)
  (display #\@)
  (let* ((yin
          ((lambda (cc) cc) k))           
         (yang
          ((lambda (cc) (display #\*) cc) (call/cc (lambda (c) c)))))          
    (yin yang)))

Now we can “partial evaluate” ((lambda (cc) cc) k) to k:


:::lisp
(lambda (k)
  (display #\@)
  (let* ((yin k)           
         (yang
          ((lambda (cc) (display #\*) cc) (call/cc (lambda (c) c)))))          
    (yin yang)))

Then we can copy propagate the value of yin, k, to the body of let*, (yin yang). And now we have only one binding left:

:::lisp
(lambda (k)
  (display #\@)
  (let ((yang
         ((lambda (cc) (display #\*) cc) (call/cc (lambda (c) c)))))
                                         ^^^^^^^^^^^^^^^^^^^^^^^^
    (k yang)))

Now we try to figure out the underlined continuation. It should be:

:::lisp
(lambda (j)
  (let ((yang
         ((lambda (cc) (display #\*) cc) j)))
    (k yang)))

You see why? Since the “current continuation” means “what is going to happen with this value”, it doesn’t include the computation before it, namely (display #\@). Now we do a similar optimization on this continuation: lifting out the side-effect (display #\*), do some partial evaluation and copy propagation:

The result of this inner continuation is:

:::lisp
(lambda (j)
  (display #\*)
  (k j))

Now we can plug it back:

:::lisp
(lambda (k)
  (display #\@)
  (let ((yang
         ((lambda (cc) (display #\*) cc) 
          (lambda (j)
            (display #\*)
            (k j)))))
    (k yang)))

Do a similar sequence of optimizations: lifting out the first (display #\*), partial evaluation, copy propagation. And we have the final result for the value of yin. Let’s name it c1 with a definition:

:::lisp
(define c1
 (lambda (k)
   (display #\@)
   (display #\*)
   (k (lambda (j)
        (display #\*)
        (k j)))))

Now, the original program would look like the following. The program would have by now printed a @ before binding yin to c1, so we make a sequence and include the display term in the front of it.

:::lisp
(begin
  (display #\@)
  (let* ((yin c1)
         (yang
          ((lambda (cc) (display #\*) cc) (call/cc (lambda (c) c)))))
    (yin yang)))

Try it. It will behave the same as the original program. Now we do another copy propagation to get rid of the first binding:

:::lisp
(begin
  (display #\@)
  (let ((yang
         ((lambda (cc) (display #\*) cc) (call/cc (lambda (c) c)))))
    (c1 yang)))

Since the call/cc here will not cause any side-effects (why?), we can lift (display #\*) out:

:::lisp
(begin
  (display #\@)
  (display #\*)
  (let ((yang
         ((lambda (cc) cc) (call/cc (lambda (c) c)))))
                           ^^^^^^^^^^^^^^^^^^^^^^^^
    (c1 yang)))

Now we just have to find what this underlined continuation is, and it will become the value of yang. It is:

:::lisp
(lambda (k)
  (let ((yang
         ((lambda (cc) cc) k)))
    (c1 yang)))

After our routine sequence of optimizations we have the value of yang. Let’s define it as c2:

:::lisp
(define c2
  (lambda (k)
    (display #\*)
    (c1 k)))

Plug c1 and c2 back into the original program:

:::lisp
(begin
  (display #\@)
  (display #\*)
  (let* ((yin c1)
         (yang c2))
    (yin yang)))

And do a copy propagation:

:::lisp
(begin
  (display #\@)
  (display #\*)
  (c1 c2))

## Transformed Program

Now we have our final transformed and optimized program. Let’s put the definitions of c1 and c2 here for an overview:

:::lisp
(define c1
 (lambda (k)
   (display #\@)
   (display #\*)
   (k (lambda (j)
        (display #\*)
        (k j)))))

(define c2
  (lambda (k)
    (display #\*)
    (c1 k)))

(begin
  (display #\@)
  (display #\*)
  (c1 c2))


For simplicity, let’s inline c2 into the main program. Now c2 disappears.

:::lisp
(define c1
 (lambda (k)
   (display #\@)
   (display #\*)
   (k (lambda (j)
        (display #\*)
        (k j)))))

(begin
  (display #\@)
  (display #\*)
  (c1 (lambda (k)
        (display #\*)
        (c1 k))))

Try it. It will still work the same as the original program.

## Behavioral Analysis

Now the program doesn’t contain any call/cc’s and is much easier to understand. Let’s try to figure out how it executes:

1. First, @* will be printed, and we will invoke:

:::lisp
(c1 (lambda (k)
      (display #\*)
      (c1 k)))

2. Inside the invocation, @* will be printed by the body of c1, and k is now bound to (lambda (k) (display #\*) (c1 k)). So the program proceed to:

:::lisp
((lambda (k)
   (display #\*)
   (c1 k))
 (lambda (j)
   (display #\*)
   ((lambda (k)
      (display #\*)
      (c1 k)) 
    j)))

It will print a *, and becomes:

:::lisp
(c1
 (lambda (j)
   (display #\*)
   ((lambda (k)
      (display #\*)
      (c1 k)) 
    j)))

Now we have seen @*@**

3. Notice that we are back to a call to c1! This is a good sign of recursion. But this time the argument is different. If we simplify it a little, we get:

:::lisp
(c1
 (lambda (j)
   (display #\*)
   (display #\*)
   (c1 j)))


4. I think you see what’s going on here. This time, c1 is called with

:::lisp
(lambda (j)
   (display #\*)
   (display #\*)
   (c1 j))

which means “When called, display TWO *’s, and then behave like c1 on the argument”. If we go on, the argument to c1 will be longer and longer, and each time with an additional (display #\*). It will print @***, and then @****, and then @*****, and so on.

5. Let’s introspect a bit. Which part of the program is responsible for creating the ever-longer displays, and why? It is this piece from the definition of c1:

:::lisp
(k (lambda (j)
     (display #\*)
     (k j)))


Here k is c1′s argument. Notice that k is always of the form:

:::lisp
(lambda (j)
   (display #\*)
   (display #\*)
   ...
   (c1 j))

When k is applied, it will print the corresonding number of *’s inside it, and then behave like c1. The argument to k is:

:::lisp
(lambda (j)
  (display #\*)
  (k j))

What does this mean? It says: “When called, print a * and then behave like k on the argument.” This is how you get a “new k”, with one more display of *.

This will go on indifinitely. This is why you see the infinite string: @*@**@***@****@*****@****** …

## Changelog

- 140109 pub. as zoomquiet.io's blog
