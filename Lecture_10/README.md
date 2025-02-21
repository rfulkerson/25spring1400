# Lecture 10

## In-class Errata / Additional Discussion

One thing I often get asked is, "How can I learn Python better and more deeply?" The answer I always give is to find something that you're passionate about and dive deep. 

* Do you like robotics? Get a Raspberry Pi and some servos and write some code to build an insect walker. 
* Do you like collecting data? Get a Raspberry Pi and a camera module and/or temperature sensor and collect images or temperature data.  
* Do you like art? Look into graphics libraries and see if you can write programs that make or modify art (think: writing filters). 
* Make a basic video game. 
* Process DNA sequences. 
* Send emails to your friends ... but from inside a program! 
* Process stock market data!
* Predict fantasy sports leagues!
* Make music!
* Get some low-cost boards and create interactive wearables for cosplay.

Essentially, if you have a passion, you can probably apply Python to it in some way. The possibilities are, truly, limited only by what you can think up.

----

We had a lot of good discussions today.  Here are some highlights ...

We started off talking about order of precedence and how things such as exponentiation (`**`) needs to be done before you can evaluate additive or multiplicative operations (`+`, `-`, `*`, `/`, `//`, `%`). We looked at some examples of how those arithmetic operations need to be completed before relational and equality tests (`<`, `>`, `<=`, `>=`, `==`, `!=`) can be evaluated. And those expressions need to be evaluated before logical `and`, `or`, and `not` can be applied.

[Here's an article](https://www.programiz.com/python-programming/precedence-associativity) that discusses precedence. There are some extra operators we haven't discussed yet (and some we won't discuss this semester), but the ones we have so far are there.

In [Q1.py](Q1.py), we looked at code that had two errors, but the syntax error of assignment would be encountered first and then, when that was fixed, the indentation error would be identified.

---

[Q2.py](Q2.py) provided an opportunity to investigate the precedence of `and` over `or` in an expression that contained both. There were good discussions had in the groups I talked to about how the larger expression is evaluated. The key that I want you to take away from our whole class discussion is that all relational and equality operations will be evaluated and *then* logical `and` and logical `or` will be applied to those results. This isn't entirely the way Thonny showed us that it will happen because we saw that, depending on how an expression is put together, [short-circuit boolean evaluation](https://www.youtube.com/watch?v=oV1JOkjCw5E) might occur. 

Understanding how Python would evaluate the entire expression is fundamental to understanding how it can perform short-circuit evaluation.

----

[Q3.py](Q3.py) addresses the concept that you shouldn't use equality `==` to try and test floating point values.

The code is:

```python
x = float(input("Enter pi: "))
if x == 3.14:
    print("We've got pi!")
```

Entering `3.14` for `x` will result in the test successfully completing. So it's tough to demonstrate that there are times when it won't work. Here's an example value that would cause the test to succeed even though the values are not the same:

```python
3.1400000000000001
```

If that was the input, the result would come back with a True execution of the conditional test and it would output `We've got pi!`.

[Here's a more detailed explanation](https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch07s02.html) of floating point equality testing if you're interested. Where we're headed is testing the absolute value of the differences of two numbers being less than an acceptable threshold. This is usually done when there have been calculations that generate floating point values.

----

[Q4.py](Q4.py) showcased the runtime error in the code, comparing `x >= '1' and x <= 10` when `x` had been input as an `int()` prior to this.  Syntactically, the code is correct but when Python attempts to compare an integer to a string (`x <= '1'`), a runtime `TypeError` occurs.

----

[Q5.py](Q5.py) had us explicitly parenthesizing the expression `one < 0 or two < 0 and three > 10 or four > 10` without changing the meaning of the test, and that requires the knowledge of how precedence works so we know what to parenthesize.

----

Finally, [Q8.py](Q8.py) used the conditional expression `y = x if x < 10 else x * 10` to assign either `x` or `x * 10` to variable `y` based on the condition `x < 10`.  It's a shorthand version of writing this:

```python
if x < 10:
    y = x
else:
    y = x * 10
```

Both statements accomplish the same task, but using the conditional expression allows us to write a shorter version of the code.

-----

[highlights.py](highlights.py) contains some work from previous semesters that look at lots of different ways to accomplish the task of inputting four quiz grades and identifying the lowest quiz score to drop. We first looked at using logical operator `and` to create a cascading `if` structure to find the lowest value.

We can refactor that into a sequence of a few `if` statements based on the assumption that if we have four variables and our task is just to find the smallest value, we can manipulate and process that data in whatever way makes sense.

Lastly, we can see that we could just use the `min()` function in Python to accomplish the task. While it's great to have this function availale, built in to Python for us, it's also incredibly useful and desirable to understand the underlying logic as to how `min()` could be accomplishing it's job. Our first two attempts give us some hints about that.


## The topics for this lecture were:

* Comparing Data Types
* Common Errors
* Expanded Order of Evaluation
* Conditional Expressions


## The highlighted topics for this lecture were

* Comparing data and common errors
	- Comparing integers
	- Comparing Strings
	- Comparing floating-point types
	- Comparing disparate data
	- Common syntax errors (=, =>, etc)

* Conditional expressions
	- true_value `if` condition `else` false_value

* Order of evaluation
	- Precedence rules
	- `()`
	- `*` `/` `%` 
	- `+` `-`
	- `<` `<=` `>=` `==` `!=`
	- `not`
	- `and`
	- `or`
