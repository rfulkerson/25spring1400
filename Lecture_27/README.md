# Lecture 27

## In-class Errata / Additional Discussion

Today's discussions focused primarily on reading and writing to files.  The big differences that were noted were:

* `readlines()` gives us all of the lines from the open textfile as a list with each element still retaining the newline `\n` character at the end.  So ```lines = f.readlines()``` as seen in [Q1.py](Q1.py) would store all of the lines from the text file associated with `f` into the list `lines`.
* `read()` reads the entire text file as one large string, including embedded newline characters.  So the `lines = f.read().split()` as seen in [Q2.py](Q2.py) would store the individual words into a list of "lines" because the `f.read()` reads the entire file into a single string and then the `.split()` will split it on whitespace. In the example in Q2, since there is only one word per line, it appears to break it into "lines" when in fact it is breaking it apart into word tokens instead.
* `readline()` reads a single line from the file, including any newline `\n` at the end of the line. This allows for more controlled processing of the file, line-by-line.

## The topics for this lecture were:

* Reading files
* Writing files

## The highlighted topics for this lecture were

* Reading from a file
	* `open()`
	* File modes used with `open()`:
		* `r` and `r+`
		* `w` and `w+`
		* `a` and `a+`
	* `f.readlines()`
	* `f.read()`
	* `f.readline()`
	* `f.close()`
	* Using `for` loops to read

* Writing to a file
	* `f.write()`
	* The use of the `with` statement

