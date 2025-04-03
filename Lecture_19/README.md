# Lecture 19

## In-class Errata / Additional Discussion

This lecture and the [previous lecture](../Lecture_18) are both kind of summary/bridge lectures for function material.  We've been talking about a lot of these concepts so far and now we're just formalizing what we've been experiencing in our in-class discussions as well as in your labs, etc.

Today we started talking about [highlights.py](highlights.py) and wrote three separate functions, `demo_one()`, `demo_two()`, and `demo_three()` which all demonstrate various concepts about local and global scope. Variables that aren't declared inside any functions are considered to have global scope.  Variables declared explicitly within functions have local scope; that includes parameter lists.

**Question from class:** How can you access both a local and a global variable's value if they have the same name?  This came about when discussing the `demo_four()` function in [highlights.py](highlights.py). I begged off answering because, as I mentioned in class, I sometimes get all of my languages jumbled in my head and this was one of those topics that I wanted to be explicitly clear on.

Here's the code for `demo_four()` that accesses the local variable but can't access the global variable:

```python
def demo_four(): # demo_four has global scope
    a = 156      # a has local scope
    print(a)     # accessing local a, not affecting global a

print()
print("Calling demo_four()")
a = 134          # global scope
demo_four()
print(a)
```

If you want to be able to access both the local `a` and the global `a`, you need to use the `globals()` function which, when used, provides a list of all items in the global scope of your program.  The code could be rewritten like this:

```python
def demo_four(): # demo_four has global scope
    a = 156      # a has local scope
    print(a)     # accessing local a, not affecting global a
    # this allows me to get to the `a` variable in the global scope:
    print(globals()['a'])   
    # replace `a` with the name of the variable you're trying to access

print()
print("Calling demo_four()")
a = 134          # global scope
demo_four()
print(a)
```

A best practice, however, is to try and *not* name variable the same thing locally and globally. This doesn't mean you can't have an `a` locally and an `a` globally that aren't related, but you typically shouldn't try to access global variables inside your functions.

Here's an interesting thought experiment.  What would the output of the following code be?

```python
for a in range(5):
    d = 6
    print("Do a thing")
print(a)
print(d)
```

Variable `a`, which you might *think* would be locally scoped to that `for` loop is in fact not locally scoped. In the above example, `a` has local scope, but it _does_ "leak" out of the `for` loop with the last value it had and you _can_ print it outside the loop. The same goes for variable `d` created inside the loop; it also "leaks" out of the loop and you have access to it after the loop.

This is different than our `demo_one()` function that looks like this:

```python
def demo_one():  # demo_one has global scope
    x = 12  # local scope
    print(x)
    
demo_one()
print(x)
```

In this example, `x` has local scope, but it belongs solely to the function and does not escape out for us to have access outside the function.

This is where programming starts to get very tricky because there are some consistent behaviors and some seemingly inconsistent behaviors. This is where incremental devleopment can come in handy; test as you develop to make sure that the code is behaving the way you think it should and it's easier to catch issues like `a` or `d` leaking out of the loops. I'm using the term "leak" to give it a sense of "you should be aware of this because maybe the use of `a` or `d` later on is unintended".

----

We also had some good discussions about [Q1.py](Q1.py) being a void function and returning something (the value `None`), which would be printed because Python is calling function `generate()` in a `print()` statement.

----

[Q3.py](Q3.py) let us investigate how we need to be careful with `return` values not being created/initialized. Function `determine(inc)` would sometimes work (if the value of `inc` is in one of the tested ranges) and sometimes not work (if it's outside the tested ranges).  Full testing of your functions should be a priority to make sure that all situations are handled correctly.

**Student question during class:** Is the `UnboundLocalError` a syntax error or a runtime error?  As I discussed in class, I maintain that it's a runtime error because a syntax error is caught before the program is allowed to execute at all and is a violation of the structure of the language itself. A runtime error is encountered and dispatched when the Python interpreter runs a line of code and it does something unexpected like dividing by zero or, in our instance, attempting to return the value of a variable that hasn't been declared yet.

Here's a [nice description](https://cscircles.cemc.uwaterloo.ca/1e-errors/) of syntax vs. runtime errors.

----

Question [Q4.py](Q4.py) counts lowercase vowels in function `mystery(w)`. It's a good example of working code that could be made more literate or legible if variables like `word` were used instead of `w` and `vowels` instead of `v` or `count` instead of `a`.  Legibility really helps in situations like this.  

We could also modify the `if` statement to look like `if w[z].lower() in v:` to test lower- or upper-case letters without having to modify the list of vowels. I mentioned that "less is more", so the less you do with the list of vowels, the better. Meaning that you could expand the list of vowels to look like this:

```python
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
```

There's nothing wrong with that, but it's easier to forget a vowel, possibly, like this:

```python
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'U']
```

Debugging this isn't necessarily difficult, but it's easy to do a quick scan of that line of code and think that all of the vowels are there.

Instead, if you keep the list to just the 5 vowels in all lowercase, then adding the `w[z].lower()` does the "heavy-lifting" of converting any capital letters to lowercase and testing against a smaller known good set of data.

We wrapped up talking about namespaces, namely local, global, and built-in, with [Q5.py](Q5.py).

Overall, great discussions in class today!


## The topics for this lecture were:

* Functions with branches
* Functions with loops
* Copy-paste errors
* Return errors
* Variable scope
* Function scope
* Namespaces
* Scope resolution

## The highlighted topics for this lecture were

* Scope
* Local variables
* Global variables
* global
* Namespace
* Scope resolution
