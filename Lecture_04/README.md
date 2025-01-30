# Lecture 04

## Summary

We started the class with a brief discussion of the [UNO Counseling and Psychological Services](http://bit.ly/unocapsinfo) resource on campus.

----

Today we talked about variables, assignment statements, objects, mutability, immutability, and different numeric data types.

When naming variables, Python best practices indicate that you should start your variables with a letter, followed by meaningful letters, digits and underscores. Underscores should be used for spaces for readability and all letters should be lowercase. Naming conventions are discussed in [PEP8](https://peps.python.org/pep-0008/#naming-conventions), the Python Enhancement Proposal.  PEP8 also discusses coding styles, etc. Here are some examples of valid identifiers used as variable names:

```python
the_first_number = 1
yellow = 2112.0
first_name = "Jessica"
last_name = "Smith"
```

Assignment statements use the assignment operator `=` and, at least for right now, have a single variable on the lefthand side and an expression on the righthand side. The expression on the right is evaluated to a single value (for now) and is stored/assigned to the variable on the lefthand side. We briefly touched on this in [Lecture 03](../Lecture_03/) in class.  Here are some examples:

```python
the_first_number = 1
yellow = 2112.0
first_name = "Jessica"
last_name = "Smith"
```

Yup, those same statements from the variable examples are all valid assignment statements. We're assigning the values on the righthand side to the variables on the lefthand side. Assignment statements can be more complex, however, like this (which isn't too complex for now):

```python
my_value = int(input("Enter a value: "))
final_value = my_value * 10
```

Two assignment statements, one which takes user input and converts it to an integer value, and another that multiplies that input value (stored in `my_value`) by 10 to store it into `final_value`.

We also briefly talked about every variable being an object and each object in Python having a value (what's stored in the variable) and the `type()` (such as integer, float, or string), and the `id()`, which is where the variable is stored in memory.

The id of a variable helps to demonstrate the last concept we talked about, which is mutability. Variables that are integers, floats, or strings are *immutable*, which means that when you store a value into a variable and then change that value, the variable name stays the same but Python allocates an entirely different location in memory for the new value to be stored in. It's kind of like having a sticky note with a title of "Important Phone Number" having a value of 1-800-555-1111 and then, if you change the important phone number on the sticky note to 1-800-555-1112 the location of the sticky note needs to move from its original position. This is a rough analogy -- you don't *have* to move the sticky note -- but assuming that you would have to take the sticky note off the wall to change the number, you probaby wouldn't get it back in *exactly* the same place it was before.  This is immutability.  You can change the value of a variable, but it will keep moving around in memory as you do that.

```python
my_x = 2112
print(x,id(x))     # this will print the value of x and it's memory location
my_x = my_x + 1
print(x,id(x))     # this will print the new value and the new memory location
```

We'll see mutable variables later in the semester and be able to better compare and contrast why there are mutable and immutable objects in Python.

Lastly, we talked about `float()` and floating point values, as well as a basic overview of f-strings (formatted strings):

```python
# regardless of what's entered (3 or 3.12), it will be converted to a floating point value
my_neat_value = float(input("Enter a number: "))

value_of_pi = 3.14159

# print values with different levels of digits after decimal
print(f"{value_of_pi}")
print(f"{value_of_pi:.4f}")
print(f"{value_of_pi:.3f}")
print(f"{value_of_pi:.2f}")
print(f"{value_of_pi:.1f}")
```

## The topics for this lecture

* Variables and Assignments
* Identifiers
  - Naming rules and style guidelines
* Objects
  - Name binding / Memory
  - Object properties
* Numeric Types
  - Integers and Floats
  - Formatting output


## The highlighted topics for this lecture

* Variables
* Valid identifiers
  - Letters
  - Digits
  - Underscores
  - Case-sensitive
  - PEP 8
* Reserved Keywords

* Assignment statements
* Incrementing a variable's value

* Object
  - Value
  - Type … `type()`
  - Identity … `id()`

* Mutability
* Immutable

* Scientific notation

* Floating point values
* Floating point literals
* `float()`
* Formatting floating point output

