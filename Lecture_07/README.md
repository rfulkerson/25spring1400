# Lecture 07

(from a previous semester's writeup since we didn't meet for class)

## In-class Errata / Discussion

Today we shifted gears from the foundational material of input, output, arithmetic, strings, and formatting output and started talking about how do we make decisions using conditions and selection. To that end, we introduced the `if`, `if`/`else`, and `if`/`elif`/`else` structures.

----

At the end of class, we started writing some basic conditions that we could test. We wrote code to test if `a` was an odd number and if one of two variables was even while the other was odd.

That code can be seen in [conditions.py](conditions.py).

Toward the end, I suggested some final thoughts thoughts about determining if one variable was even and the other was odd. Those thoughts were that you need to have a good understanding of the data and what it means if, for instance, one of the conditions in an `if`/`elif`/`else` fails. What does that mean for future tests you can make?

```python
# if e or f is even and the other is odd

e = 41
f = 67

if e % 2 !=  f % 2:
    print("one is even, one is odd!")
elif e % 2 == 0:
    print("They're both even!")
elif e % 2 != 0:
    print("They're both odd!")
```

So, in this example, if our first test fails (i.e., `e` and `f` are not even/odd), we know that the two variables are either both even or both odd. So, I asked the question in class, "how can we simply test if they're both even?" The suggestion was as you see it above, which is to test `e % 2 == 0`. How do we know that this will work to test if both `e` and `f` are positive?  We know because if the first test fails, then we know with 100% certainty (as long as our first condition is written correctly &#128512;), that both are either even or odd and thus if we test if one of the variables is even, it would mean that both were even. We can then test with our second `elif` if the numbers are odd in a similar fashion.

We didn't get this far in the discussion, but technically we could rewrite the code to just have an `else` as the last part because if the first *two* conditions fail, we know that it's not an even/odd situation (first condition failure) nor is it an even/even situation (second condition failure), leaving the only other option which is that they're both odd numbers:


```python
# if e or f is even and the other is odd

e = 41
f = 67

if e % 2 !=  f % 2:
    print("one is even, one is odd!")
elif e % 2 == 0:
    print("They're both even!")
else:
    print("They're both odd!")
```

----

From previous semesters, we wrote the code in the [highlights.py](highlights.py) file. I've included that discussion because it's a pretty good discussion about developing code.

The file [highlights.py](highlights.py) contains code for a basic calculator that you can look at and play with. It doesn't do any error checking and only handles single digit arithmetic and single-character operators.  That's what we can do right now. We'll be able to do more advanced stuff with string input soon that would allow any values and other operators to be used.

In addition to demonstrating writing the calculator itself, I wanted to focus on the write-and-test, write-and-test methodology of writing code.  Don't be a hero and try to write it all at once.  Write a little, test a little. It makes it easier to debug.  

Doing this, we were able to identify that our `left` and `right` operands weren't converted to numeric data when we were trying to do math with them.  

We were also able to write one solution that had a series of stacked `if` statements that we were then able to convert into a singular cascading `if`/`elif`/`elif` ... structure.

Lastly, we were able to take our initial solution where there were six separate `if` conditions to test with six separate yet similar `print` statements. We simplified the code to calculate a value for variable `result` in the cascading `if` structure and then have a singular `print` statement at the end of the code.

We saw that writing a little and testing a little helped us handle any issues immediately and more conveniently than if we waited and had written 30 or 40 lines of code and then had to make massive changes to existing code along the way.  Small, incremental changes when we encounter the need to make them makes it easier to write correct code.

----

The basic format for an `if` selection structure is:

```python
if condition:
   action
```

The condition, for now, will be either an equality `==` or inequality `!=` test, and is an assertion at that point in the code. You're essentially saying, "At this point in the code, I think that `condition` will be `True` or `False`.  If the condition is `True`, my code will execute the `action`.  If the condition is `False`, my code will skip the action."

At least, that's what I hope you're saying as you read code.  :)

For example:

```python
my_value = int(input("Enter 10: "))

if my_value == 10:
   print("You entered the number I asked you to enter!")
```

For an `if`/`else`, your code makes an assertion but then offers a mandatory alternative action to be performed if the condition fails:

```python
if condition:
   action1
else:
   action2
```

Here, you're essentially saying, "At this point in the code, I think that `condition` will be `True` or `False`.  If the condition is `True`, my code will execute `action1`.  If the condition is `False`, my code will execute `action2`."

For example:

```python
my_value = int(input("Enter 10: "))

if my_value == 10:
   print("You entered the number I asked you to enter!")
else:
   print("You didn't enter the desired number!") 
```

For an `if`/`elif`/`else`, your code offers multiple assertions to be tested and can possibly (and usually does) offer a mandatory alternative action to be performed if the conditions fail:

```python
if condition1:
   action1
elif condition2:
   action2
else:
   action3
```

Here, you're essentially saying, "At this point in the code, I think that `condition1` will be `True` or `False`.  If the condition is `True`, my code will execute `action1`.  If `condition1` is `False`, my code will then go on to test `condition2`, and if that's `True`, it will execute `action2`. If `condition2` fails, my code is forced to execute `action3`."

For example:

```python
my_value = int(input("Enter 10: "))

if my_value == 10:
   print("You entered the number I asked you to enter!")
elif my_value == 11:
   print("That's also a pretty good number.")
else:
   print("You didn't enter the desired number!") 
```

A student came up after class and asked me to explain the `if`/`elif`/`else` again and what happens if you don't use an `elif`.  This is the analogy I came up with:

Say you're going to drive to either Denver, Kansas City, or Des Moines.  The following code would work perfectly giving you rough directions, assuming you were only ever headed to one of those three destinations:

```python
where = input("Where you headed? ")

if where == "Denver":
   print("Head to Denver on I-80 west until you hit I-76 west")
elif where == "Kansas City":
   print("You're going to want to take I-29 south.")
else:
   print("You're headed to lovely Des Moines on I-80 East!")
```

If you replace the `elif` with just an `if` statement, similar to what we had in [Q6.py](Q6.py) vs. [Q7.py](Q7.py), you end up with this:

```python
where = input("Where you headed? ")

if where == "Denver":
   print("Head to Denver on I-80 west until you hight I-76 west")
if where == "Kansas City":
   print("You're going to want to take I-29 south.")
else:
   print("You're headed to lovely Des Moines on I-80 East!")
```

Now the code works fine for Kansas City and Des Moines, but if you say you're going to Denver, your directions will tell you that you're going to Denver on I-80W and then turn around and tell you that you need to take I-80E and head to Des Moines.  This is because you have two separate tests to make. So, now you're being instructed to do two separate things all because you didn't use an `elif` for the second test for `Kansas City`.

Of course, there are ways to fix this, such as turning the final `else` into an `elif` with a conditional test.  While the code below will work and is more explicit and complete, it still has to make at least two tests regardless of the input.  If that's not clear, copy the code into Thonny and step through it to watch how there will always be at least two tests performed even if you enter `Denver` as your destination.


```python
where = input("Where you headed? ")

if where == "Denver":
   print("Head to Denver on I-80 west until you hight I-76 west")
if where == "Kansas City":
   print("You're going to want to take I-29 south.")
elif where == "Des Moines":
   print("You're headed to lovely Des Moines on I-80 East!")
```

**With so many different approaches to coding and so many tools in our programming toolboxes, it's tough to cover all possible options, but hopefully these examples provide you with some things to think about.**

Our goal, ultimately, is to write the most accurate code with zero errors and hopefully a modest amount of efficiency and flexibilty so that the code runs quickly and can be updated easily to, for example, add more options (such as going to Fargo) with consistent code.

## The topics for this lecture were:

* If-else branches (general)
	- if branches
	- if-else branches
	- if-elseif-else branches
* Detecting Equal Values with Branches
	- Equality and inequality operators
	- Detecting equality with an if statement
	- Detecting equality with an if-else statement
	- Detecting equality with an if-elif-else statement

## The highlighted topics for this lecture were

* If-else branches (general)
	- branch
	- if
	- if-else

* Detecting equal values with branches
	- Equality operator (`==`)
	- Inequality operator (`!=`)
	- Boolean
	- `if`
	- `if`-`else`
	- `if`-`elif`-`else`


