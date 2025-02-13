# Lecture 06

## In-class Errata / Discussion

We started off with a discussion of the runtime error `EOFError: EOF when reading a line` that you might encounter in the zyBooks textbook editor in either **Submit mode**. 

If your code works in interactive mode (i.e., writing and testing it) but you're receiving this error in **Submit mode**, then you're providing the correct number of inputs in your program during interactive runs, but the actual program specifications are for fewer inputs.  For instance, your program might be set up for three `input()` statements, but the program is only expecting two, so when you submit your code via **Submit mode**, you'll receive the `EOFError` because zyBooks will only ever provide two pieces of input even though your program is expecting three.

If this is the case, go back to the code specifications and/or watch the associated video (if it's an MSP) and try to determine what the input should be for the program.

----

Some quick takeaways from the [highlights.py](highlights.py) file (not covered in class) are:

* You can use escape sequences like `\"` and `\'` to print double quotes inside double-quoted string literals and single quotes inside single-quoted string literals, respectively.
* The `len()` function will tell you how many characters are in a string.
* Strings can be accessed as a whole or each character individually by position. To access by position, use the name of the string, following by a set of square brackets and a position inside the brackets, like `phrase[7]`.
* Strings start numbering their characters at position `0`, as many "collections" of data do in Python.  So the first character of variable `phrase` would be `phrase[0]`.
* Strings are immutable, which means you can't change a piece of a string, like `phrase[3] = 'x'`.  You'll receive a runtime error if you attempt this. You can only change the contents of a string as a whole, such as `phrase = "new value"`. 

	This is the first time we've seen code that prevents us from changing an immutable object. Strings, integers, and floats are all immutable, but when we've changed values up to this point we don't see the destruction of the current variable and creation of a new variable because we're just using the variable by name, which is the intent.  The immutability of those types of data is supposed to be transparent to us for the most part but is brought to our attention if we try to change a part of a string.
	
* f-strings can specify the type of data that we put into a placeholder, such as `f'{a:d}'`, which means that we're holding a space for variable `a` and it *must* be an integer.  If variable a is a floating point value, we'll encounter a runtime error: `ValueError: Unknown format code 'd' for object of type 'float'` Again, you'll receive a line number that the error occurs on and will then need to work backward to figure out which variable is trying to be used incorrectly.

	```python
	thing = 21.12
	print(f'Attempting to print float as an integer: {thing:d}') # this results in ValueError
	```
	
* f-strings will do implicit conversion of integer values to floats, though, such as:


	```python
	value = 6
	print(f'My value as a float: {value:f}') # will print 6.000000
	```

----

For the most part, the question discussions went as expected.

[Q6.py](Q6.py) brought to our attention the fact that using an f-string specifier like `f'{value:f}'` will output 6 digits after the decimal, as well as the way that the expression `11 // 2 *  5.6 // 5` is evaluated from left-to-right.  This is a great expression to put into a small program in Thonny and step through the debugger. Notice the way that the integer floored division of `11 // 2` produces an integer result, but when you get to `28.0 // 5` after the implicit promotion of `5 * 5.6` that *that* floored division generates a floating point result. We've talked about this before, but it's interesting to notice it when it happens.

[Q7.py](Q7.py) introduced us to the fact that you can do calculations or call functions in your f-strings, though it's not advisable to do so because it makes your code harder to read, debug, and maintain.  The code in Q7.py has a better suggestion for how to handle that.

Lastly, [Q8.py](Q8.py) showed us an example of the `ValueError` mentioned above, where a floating point result is attempted to be forced into a `{x*y:d}` placeholder in an f-string.  


## The topics for this lecture were:

* Representing Text
 - Escape Sequences
 - Converting between encodings and text
* String Basics
 - Strings as Sequences
 - String Manipulations
* String Formatting
 - Using format()
* Type Conversions

## The highlighted topics for this lecture were

* Representing Text
 	- Unicode
 	- Newline \n
 	- Escape sequences such as `\\` `\'`

* String basics
	- String literals
	- `len()`
	- Brackets to access position
	- Strings are immutable
	- Concatenation

* String formatting
 	- `format()`
 	- Replacement field using `{}`
 	- Keyword argument using `{}`
 	- Format specifiers for replacement fields
  		- `{:s}`
 		- `{:d}`
  		- `{:f}`
  		-  `{:.3f}`
  		- Using `f''`

* Type conversions
 	- Implicit conversion
 	- Explicit conversion
  		+ `int()`
  		+ `float()`
  		+ `str()`

