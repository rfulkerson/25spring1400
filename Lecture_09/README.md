# Lecture 09

## In-class Errata / Additional Discussion

We talked about [De Morgan's Law](https://en.wikipedia.org/wiki/De_Morgan%27s_laws) when using the `not` operator.  

* Here is [an explanation using a Penguin](https://blog.penjee.com/what-is-demorgans-law-in-programming-answered-with-pics/) to discuss De Morgan's Law; the examples use a `Penguin` and some code that's a little past where we are right now, but it's not so overwhelming that it won't make sense, I don't think.  
* Here is a [visual discussion of union (or) and intersection (and)](https://www.youtube.com/watch?v=LBGbwQDhceg) that may help the negation of logical operators `and` and `or` make sense.  
* Here is a [lengthier, more in-depth](https://www.i-programmer.info/programming/theory/4977-dangerous-logic-de-morgan-a-programming.html) discussion about De Morgan's Law in case you want to go down that rabbit hole.

----

The only question we didn't get to was [Q8.py](Q8.py).

----

People wonder when a good time to use `not` would be since I talked about how people shouldn't write code like `if not(y < 5)` and instead write `if y >= 5`. This is a valid concern: if the distribution of `not` across an expression/condition basically just results in using DeMorgan's Law for making code easier to read/debug/maintain, when would you ever use `not`?

The answer is that there are good times to use `not` and that we'll see those times coming up with data validation loops in the coming few lectures.  A rough example might look like this (with more explanation coming soon):

```python
done = False

while not done:
    x = input("Enter 'stop' to quit: ")
    if x == "stop":
        done = True
    else:
        print(f"You entered {x} and I would do something useful with it here.")
```

Basically, using `not` to simply negate the value of a Boolean variable's value is a good use case for `not`.  It's not the *only* good use case, but it's the most prevalent that we might see this semester.

----

There are some examples in [highlights.py](highlights.py) that might be interesting to look through:

* There is code to test a year whether it was a leap year or not, which requires the use of logical operators to handle the two separate cases:
	* Leap years are divisible by 4 but not divisible by 100 (i.e., 2024 is leap year, 1900 is not a leap year)
	* Leap years are divisible by 400 (i.e., 2000 is a leap year, 1900 is not)
* There is also code to determine if a squirrel party is successful based on two potential scenarios:
	* If between 40 and 60 (inclusive) cupcakes are consumed, the party is a success.
	* Unless it's a weekend, when there is no upper bound on cupcake consumption.

In the squirrel party example, there are three different example ways to write cascading `if`/`else` structures to handle it, one using chained operators as well a logical operators and the other two using just logical operators but different ways to do that.


## The topics for this lecture:

* Logical Operators
	- and
	- or
	- not
* Ranges with Gaps
* Multiple Branches
	- Nested branches

## The highlighted topics for this lecture:

* Detecting ranges using logical operators
	- Logical `and`
	- Logical `or`
	- Logical `not`

* Detecting ranges with gaps

* Detecting multiple features with branches
	- Nested `if`-`else`
	- Cascading `if`-`else`


