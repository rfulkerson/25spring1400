# Lecture 24

## In-class Errata / Additional Discussion

This lecture was all about list comprehensions.  Essentially, list comprehensions are just shorthanded, elegant ways to compress looping over a list. We looked at a number of different ways to process lists of data using list comprehensions, including conditional comprehensions. Those conditional comprehensions can use regular relational operators such as `results = [p for p in prices if p <= val]` such as in [Q5.py](Q5.py) or even call functions that return values of `True` or `False`, such as `leap = [x for x in years if isLeapYear(x)]` in [Q6.py](Q6.py).


## The topics for this lecture were:

* List Comprehensions
* Lists in comprehensions are not mutable
* Conditional list comprehensions


## The highlighted topics for this lecture were

* Lists in comprehensions are not mutable
* Conditional list comprehensions
* `foo = [expr for loop_var in iterable]`
* `foo = [expr for loop_var in iterable if condition]`
