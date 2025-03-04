# Lecture 12

**NOTE: This writeup is from a previous semester as I was absent from class and you had a sub for the day. All of the relevant information is present.**

## In-class Errata / Additional Discussion

We spent the first 30 minutes of class writing a password generator in [highlights.py](highlights.py). We used the `random` module and the `random.randint(x,y)` function to help pick random characters out of a source string and then apply it to building a password of a specific length.  This allowed us to explore the following concepts:

1. Random number generation with `random`.
2. String processing by position (similar to the way you access list elements by position).
3. Counter-controlled repetition to create passwords of a specific length.

We did some code refinement as we developed the solution, such as creating the `howmany` variable that is the length of the `source` string so that we can add and subtract potential password characters without worrying about modifying our actual password generation loop. All told, we wrote 9 lines of code that will generate strong passwords.

Another worked example we didn't get a chance to work can be found in [highlights2.py](highlights2.py), which should create a list of high temperatures (Sunday through Saturday). Using lists, we can find the highest and lowest high temps, the average high temperature for the week, and print Sunday's and Friday's high temperatures. Using sequence functions like `len()`, `sum()`, `min()`, and `max()`, we can process a list of values in a pretty straightforward manner to accomplish the requested tasks. The code is not completed but is available for you to implement as a practice exercise.

----

We then started working on our Peer Instruction questions, and [Q1.py](Q1.py) and [Q2.py](Q2.py) explored counter-controlled loops to see if we could determine the number of executions of the various loops.

Of the five remaining questions, we spent the most time on [Q7.py](Q7.py) which utilzed the `remove()`, `pop()`, and `append()` functions for a list. What most folks wrestled with was whether or not `remove()` deletes only the first instance of the value or all instances of the value in the list. As we found out, [it removes only the first instance](https://www.programiz.com/python-programming/methods/list/remove).


## The topics for this lecture were:

* Counter-controlled loops
	- Counting by 1
 	- Counting in reverse
	- Skip-counting

* Lists
	- Data container in Python
	- `[]` notation to create
	- Element
	- Position/index
	- Mutable collection

* Sequence-type functions
	- Allow us to perform common tasks for a collection.



## The highlighted topics for this lecture were

Sequence-type functions

* `len(sequence)`
* `sequence1 + sequence2`
* `min(sequence) and max(sequence)`
* `sum(sequence)`
* `sequence.index(value)`
* `sequence.count(value)`

