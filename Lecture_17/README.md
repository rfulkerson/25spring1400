# Lecture 17

## In-class Errata / Additional Discussion

From SPRING 2024 discussion:

We started off talking about developing a function to determine if a number was even or not in [highlights.py](highlights.py). There are three versions of the function in the code, developed incrementally to show different ways to approach the solution. Here are three variations on the same theme:

```python
def isEven(x):  # call whatever is sent to me "x"
    if x % 2 == 0:
        return True
    else:
        return False

def isEven_two(x):
    result = False
    if x % 2 == 0:
        result = True
    return result
    
def isEven_three(x):
    return x % 2 == 0
```

They all do the same thing, just in different ways. We had a brief discussion of why we would implement a function for the simple task of determining if a number was even, since the test is just `x % 2 == 0`. By isolating that repetitive task, we're able to minimize places that the code could be implemented incorrectly, as in the code below:

```python
number = int(input())
if number % 2 == 0:
    print("It's even!")
    
value = int(input())
# below is wrong; could be managed by calling function    
if value % 3 == 0:
    print("It's also even!")
```

By using the function `isEven()`, for instance, this becomes less of an issue:

```python
number = int(input())
if isEven(number):
    print("It's even!")
    
value = int(input())
if isEven(value):
    print("It's also even!")
```

We had one carryover question from [Lecture 16](../Lecture_16/) that discussed `enumerate()`, [Q7](../Lecture_16/Q7.py).

We then focused on introducing that ideas of functions and some basic syntax. There were some good discussions about the questions and then we were able to discuss a little bit about `turtle` with functions and we introduced and started talking about scope.

The [first 13 minutes of this video](https://www.youtube.com/watch?v=QVdf0LgmICw) cover some of the concepts that we talked about briefly today regarding scope.


## The topics for this lecture were:

* Function definition
* Function call
* Return statement
* Parameter
* Argument
* Nested function calls


## The highlighted topics for this lecture were

* A function is a small, self-contained block of code that accomplishes a singular, well-defined task.
* Function definition
* `def`
* `return` statements
* Function call
* Parameter
* Argument
