# Lecture 28

## In-class Errata / Additional Discussion

Today, we looked at reading from a CSV file. You can do this manually by reading each line of the file and then splitting on commas, but the `csv.reader()` functionality of the `csv` library takes that step out and allows you to focus on using the code as seen in [Q4.py](Q4.py), which uses a `for` loop to simply process each line and have immediate access to the elements on each line by position in a list.

## The topics for this lecture were:

* The `with` statement
* CSV files

## The highlighted topics for this lecture were

* Reading CSV files
	* `import csv`
	* `csv.reader(f, delimiter='\t')`
	* Using `for` loops with `csv.reader()`

* Writing CSV files
	* `import csv`
	* `csv.writer(f)`
	* `file.writerow(data)`
	* `file.writerows(data)`
