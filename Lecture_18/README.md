# Lecture 18

## In-class Errata / Additional Discussion

Today's discussion focused more on the how's and why's of writing functions.

We discussed print functions, typically also referred to as void functions because they don't return any values.  They generate output, yes, but there is not an explicit `return` statement to sends a value back to the function call. void functions _do_ return somethingn implicitly, however, which is `None`.  You can see this if you run even a simple program like this in Thonny and step through it with the debugger:

```python
print("Hello")
```

If you step through that program, you'll see `None` displayed after the `print()` statement has executed because the built-in `print()` function doesn't have a `return` statement.

We also spent some time writing the [highlights.py](highlights.py) code, which introduced the concept of `if __name__ == '__main__'`, which is a requirement moving forward in the textbook so that methods can be tested correctly.

The only other major thing we talked about in addition to working through a number of questions was in relation this concept of using `if __name__ == '__main__'`.  From now moving forward, the programs will expect you to write code that includes a test for the `__main__`, as seen in [Q1.py](Q1.py):

```python
def print_price(item, cost):
    print('{:>12} : ${:.2f}'.format(item, cost))

if __name__ == '__main__':
    print_price("Beans", 1.23)
    print_price("Corn", 0.59)
    print_price("chips", 3.59)
    print_price("Steak", 9.59)
    print_price("Detergent", 7.59)
```

When you start introducing your own functions into programs, typically you move toward using this format for your code, with the `if __name__ == '__main__':` conditional statement.  This is discussed in lecture 18, section 1 of the textbook.

The zyBooks platform requires that format of the code for it to be able to properly test your functions. Some of the tests test to just make sure your output is correct, but some of the tests isolate the function you have written and test _just_ the function to make sure it is taking correct inputs and generating correct outputs or return values. In order to do this, zyBooks requires your programs to follow this new format. Many of the function templates indicate this, so make sure to follow those rules.

Oftentimes, you'll see the code written like this, with a `main` function called from that `if` statement.  Copy and paste the code below into Thonny and use a step-into debugging session to watch how the code is called and managed.

```python
def print_price(item, cost):
    print('{:>12} : ${:.2f}'.format(item, cost))

def main():
    print_price("Beans", 1.23)
    print_price("Corn", 0.59)
    print_price("chips", 3.59)
    print_price("Steak", 9.59)
    print_price("Detergent", 7.59)
    
if __name__ == '__main__':
    main()
```

In this instance (and the example prior to this), anything that you've typically been writing for your programs ends up being dumped into the `main()` function and then you have the supporting functions elsewhere, such as `print_price(item, cost)`.

----

We also spent time revisiting the pythagorean triples program, demonstrating timing for using `a**2 + b**2 == c**2` vs. putting that into a function like the following.

Original:

```python
import time
start = time.perf_counter()

for a in range(1,max_value):
    for b in range(1,max_value):
        for c in range(1,max_value):
            if a**2 + b**2 == c**2:
                print(a,b,c)

end = time.perf_counter()

print(f"I just tested {max_value**3} possibilities.")
print(f"It took me {end-start:.2f} seconds to do that!")
```

With a function:

```python
import time
def is_triple(a,b,c):
   return a**2 + b**2 == c**2

start = time.perf_counter()
howmany = 200
for a in range(0,howmany):
    for b in range(0,howmany):
        for c in range(0,howmany):
            if is_triple(a,b,c):
                print(f"{a},{b},{c} is a pythag triple!")
end = time.perf_counter()

print(f"I just tested {max_value**3} possibilities.")
print(f"It took me {end-start:.2f} seconds to do that!")
```

The version with the `is_triple()` function took about a half second longer because of the overhead of calling the function.

We were able to trim the amount of time to accomplish the task by importing the `math` module and replacing the test with calls to `math.pow()`:

```python
import math
import time
howmany = 200
start = time.perf_counter()
for a in range(0,howmany):
    for b in range(0,howmany):
        for c in range(0,howmany):
            if math.pow(a,2) + math.pow(b,2) == math.pow(c,2):
                print(f"{a},{b},{c} is a pythag triple!")
end = time.perf_counter()

print(f"I just tested {max_value**3} possibilities.")
print(f"It took me {end-start:.2f} seconds to do that!")
```

Even though there are three function calls there instead of just using `**` (no function calls) or a single function call to `is_triple()`, the time was cut in about half because the functions in the `math` module are highly optimized.

Even wrapping the calls to `math.pow()` in another function results in a reduction in execution time as measured with the `time` module over using straigh `**`:


With a function:

```python
import math
import time
def is_triple_math(a,b,c):
   return math.pow(a,2) + math.pow(b,2) == math.pow(c,2)

howmany = 200
start = time.perf_counter()
for a in range(0,howmany):
    for b in range(0,howmany):
        for c in range(0,howmany):
            if is_triple_math(a,b,c):
                print(f"{a},{b},{c} is a pythag triple!")
end = time.perf_counter()

print(f"I just tested {max_value**3} possibilities.")
print(f"It took me {end-start:.2f} seconds to do that!")
```



## The topics for this lecture were:

* Print functions
* Dynamic typing
* Reasons for defining functions
* Mathematical functions
	- Calling functions in expressions


## The highlighted topics for this lecture were

* void function
* Polymorphism
* Dynamic typing vs. static typing
* Modular development
