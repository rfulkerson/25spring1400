# Lecture 14

## In-class Errata / Additional Discussion

Today, we looked at the membership and identity operators as well as the `for` loop in Python.

During our Peer Instruction questions [Q1.py](Q1.py), [Q2.py](Q2.py), and [Q3.py](Q3.py), we looked at the identity (`is`) and membership (`in`) operators and discussed how the identity operator only evaluates to true if the lefthand and righthand operators are the same object in memory.  This is usually reserved for small numeric values and short strings. Usually, for beginning programming students, what is usually intended is an equality test when `is` is used instead. Here's a really nice explanation of `is` vs `==`: [https://www.youtube.com/watch?v=CZ8bZPqtwU0](https://www.youtube.com/watch?v=CZ8bZPqtwU0)

----

We also looked at using the membership operator with dictionaries in [Q4.py](Q4.py). What we discovered is that the `in` operator when used with a dictionary only looks at the keys of a dictionary. Later this semester, we'll look at the `.values()` function we can call on a dictionary to find the values and use that instead if we want to look at using `in` with the values of a dictionary.

----

[Q8.py](Q8.py) demonstrated how to use a `for` loop to work through a collection. In this instance, it was a list, and we were able to see that in the most basic form, a `for` loop will visit every element from front to back and give you access to process those elements.
----

[Q5.py](Q5.py) had us work through using the `in` operator with a `for` loop and a list to iterate through. We did really well with this question, understanding that the `for x in [10, 20, 30, 40, 50]` allows us to just move through all values in a list of values.

As an extension of this, think about the following situation:

```python
y = [10, 20, 30, 40, 50]
for x in y:
    x *= 2
print(y)
```

What would happen to list `y` and what would print. Some possibilities are printing `[10, 20, 30, 40, 50]` or `[20, 40, 60, 80, 100]`. The answer is the former, because `for` loops like this don't affect the original list at all.  Variable `x` takes on copies of values in the list, so any modifications to `x` don't change the original list.

----

[Q6.py](Q6.py) asked about using a `while` loop to move through a string, but we discussed that the way the loop is written, it's missing a loop control variable modification so it's an infinite loop stuck printing nothing but the first letter of the string you entered.

[Q7.py](Q7.py) remedied this by implementing a `for` loop like the one we implemented in [highlights2.py](highlights2.py). Using a `for` loop like this, you don't have to keep track of your position in a string (or list, tuple, set, or keys of a dictionary) because the `for` loop will just work from beginning to end, first element to last element.

----

We didn't get a chance to work through [Q9.py](Q9.py) or [Q10.py](Q10.py).

## The topics for this lecture were:

* Membership Operators
	* in / is
* Summary of Types so far
* For loops
	* Structure
	* Use of in
	* Processing lists, tuples, sets, dictionaries, and strings

* Membership and Identity
	* `in`
	* `not in`
	* Can be used on containers or strings
	* Used quite a bit!

	* `is`
	* `is not`
	* These don’t check values, but rather if two variables are the same object (reference the same item in memory)
	* Not used that much, but good to know


## The highlighted topics for this lecture were

```python
for var in container:
    # loop body
```

* The container can be a string, list, tuple, set, or dictionary.
* Variable `var` takes on the values of the container in a read-only manner.
* Must work through the entire container front to back, and there's no easy way to "skip-count" through elements.

* Strings: each character
* Lists, tuples, sets: each value
* Dictionaries: keys

