# Lecture 11

**NOTE: This writeup is from a previous semester, but all of the relevant slides are discussed.**

## In-class Errata / Additional Discussion



We had some good discussions about our Poll Everywhere questions.  [Q1.py](Q1.py) asked about how many times a loop would execute. Everyone answered either 11 or 12 based on the code, which was expected. When trying to determine how many times a counter-controlled loop will execute, just make sure to look at the initial value, the final value for testing, and the operator being used to test fo the final value.  In the Q1 example, the initial value was 0, the test was `x <= 11` and the modifcation was `x += 1`.  So it runs from 0 through 11, inclusive, which is 12 times.

----

Regarding [Q2.py](Q2.py), we talked about how this loop would be an infinite loop.  Theoretically, this is true, as integers don't really have an upper or lower limit.  ChatGPT provides this response about integer values:

> In Python, integer values do not overflow or underflow because they are implemented as "unlimited precision" integers, which means they can represent integers of arbitrary size. This is in contrast to many other programming languages, where integers have a fixed size and can overflow or underflow if the result of an arithmetic operation exceeds the maximum or minimum representable value.

> Python's implementation of integers is achieved using a technique called "bignum arithmetic," which allows the program to dynamically allocate memory as needed to represent integers of arbitrary size. This means that you can perform arithmetic operations on very large integers without worrying about overflow or underflow errors.

That's great, but there *is* a practical limit to how big an integer can be, however, and that is limited by the amount of memory the system has. So eventually, our code in [Q2.py](Q2.py) would encounter what is known as "underflow", which means that it would reach the smallest number it could possibly store on the system it's running on and then the  number would either roll around mathematically to the largest number the system could store (thus making the loop fail) or it would become a NaN (Not a Number) value, which would likely also cause the loop to exit.

Underflow/overflow _does_ occur with floating point numbers in Python.  Run this code in Thonny to test it that I culled from [https://stackoverflow.com/questions/52151647/integer-overflow-in-python3](https://stackoverflow.com/questions/52151647/integer-overflow-in-python3) and [this brief explanation at python.org](https://docs.python.org/3/library/exceptions.html#OverflowError):

```python
import sys

i = sys.maxsize
print(i)
# 9223372036854775807
print(i == i + 1)
# False
i += 1
print(i)
# 9223372036854775808

f = sys.float_info.max
print(f)
# 1.7976931348623157e+308
print(f == f + 1)
# True
f += 1
print(f)
# 1.7976931348623157e+308
```

----

We discussed what good sentinel values are for [Q3.py](Q3.py). Because the question asked about numeric input for quilt squares, the best option is an impossible integer value size for quilt squares:

```python
size = int(input("enter quilt square size: "))

while size >= 0:
    total += size
    size = int(input("enter quilt square size: "))
```

But arguments _could_ be made for the word `done` or `q` if you did the numeric casting inside the loop:

```python
size = input("enter quilt square size: ")

while size != "done":
    total += int(size)
    size = int(input("enter quilt square size: "))
```

The only problem with this is if you allow textual input and you try to cast it as an integer inside the loop, without proper precautions (which we don't have yet) the code will crash.  So if someone entered `seventeen`, the code would crash trying to cast it with `int()`.

-----

Then in [Q4.py](Q4.py) and [Q5.py](Q5.py) we looked at sentinel-controlled loops that had the same input but produced different results. Q4.py had the correct code, which has the structure of:

* prime the loop with initial value for loop control variable
* while the loop control value hasn't been entered:
	* process the value in whatever fashion makes sense
	* read another value for the loop control variable and then end the loop, to go back to test again.

In Q5, the order of statements inside the loop were reversed, which means that if you enter the loop with a valid value, you immediately throw it away because you read a new value. Then you process that value without testing it for validity and _then_ end the loop and test again.

Sentinel-controlled loops, in general, operate on the principle of entering good data and then processing it and continuing to enter data until a bad value is entered:

```python
total = 0
grade = int(input("Enter a grade to process: "))

while grade >= 0:
    total += grade
    grade = int(input("Enter a grade to process: "))

print("The total of all grades is:", total)
```

Data validation loops, a subset of sentinel-controlled loops, work on the opposite premise: the loop continues while you keep entering bad values. The value that allows you to exit the data validation loop will be a _good_ value.

```python
weight = float(input("Enter a weight greater than 0: "))

while weight <= 0:
    weight = float(input("Enter a weight greater than 0: "))

print("The weight you entered, which is definitely bigger than 0, is:", weight) 
```

----

We struggled a bit with [Q7.py](Q7.py), which asked us to find code that would check that a valid age was entered. This is known as a sentinel-controlled, data validation loop. The correct answer set up the following code:

```python
age = int(input("Enter age: "))
while age < 0:
    age = int(input("Enter age: "))
print(f"You entered {age} as the age.")
```

This is a data validation loop, which means that we're actually looking for a *good* value to end the loop. This loop's condition is `True` while bad values are entered and becomes `False` (and thus exits the loop) when a good value is entered so that when we print the age, we're actually printing a valid age.

This means that there are two different ways to think about sentinel-controlled `while` loops:

* We keep looping while valid data is entered, and while valid data is entered we process it and ask for more data to process. Only bad data or a sentinel value (a specific value identified that is out of range for valid values but indicates that we're done) will end the loop.
* We keep looping while *invalid* data is entered, and while invalid data is entered we keep reprompting the user to enter data again. Only *valid* or *good* data will end the loop, and we are guaranteed on the other side of the loop to have a valid value for whatever variable we're obtaining input for.

----


## The topics for this lecture were:

* Loop body
* Iteration
* while condition: 
	- statement1
	- statement2

## The highlighted topics for this lecture were

* while loop
* Loop body
* Iteration

* Counter-controlled loop
* Sentinel-controlled loop
* Sentinel value

* Infinite loop
* Pre-test loop

* Requirements for looping:

	1. Loop Control Variable (LCV)
	2. Initial value for the LCV
	3. Modification of the LCV
	4. Test for the final value of the LCV
