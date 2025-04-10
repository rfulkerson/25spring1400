# Lecture 22

## In-class Errata / Additional Discussion

Today, we discussed that `split()` on a string breaks strings apart based on whitespace characters by default, so it essentially just tokenizes a string into "words" (whatever non-whitespace looks like in a particular string).

When provided with an argument, such as `split('?')` in [Q2.py](Q2.py), Python will return results for something on both sides of the delimiter, since a delimiter separates tokens.  So if the delimeter is at the beginning or end of a string, there will be an empty string that is generated in the list at the front or the back of the list.

We worked through a couple of questions from [Lecture 21](../Lecture_21) and then worked through the first seven questions of this lecture. These quesions covered topics from the correct use of `split()` and `join()` to working through some basic list-related questions.

## The topics for this lecture were:

* String split and join
	* `split()` and `join()`
* Lists review

* Lists
	* Data container in Python
	* `[]` notation to create
	* Element
	* Position/index
	* Mutable collection
* Sequence-type functions
	* Allow us to perform common tasks for a collection.

## The highlighted topics for this lecture were

* `split()`
* Token
* Separator and default separator
* `join()`

* List
* Container
* Index
* Mutable
* In-place modification
* `list()`
* `del` 
* `my_list[x:y]`

* Lists
	* Position/index always starts at `0`
	* Mutable (can change)
	* `list.append(value)`
	* `list.extend([x])`
	* `list.insert(i, x)`
	* `list.pop()`
	* `list.pop(position)`
	* `list.remove(value)`
	* `list.sort()`
	* `list.reverse()`
 
* Sequence-type functions
	* `len(list)`
	* `list1 + list2`
	* `min(list) and max(list)`
	* `sum(list)`
	* `list.index(value)`
	* `list.count(value)`
