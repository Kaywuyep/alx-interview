## 0x03-log_parsing

0. Log parsing
mandatory
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

#### Concepts Needed:
- File I/O in Python:

1. Understand how to read from sys.stdin line by line.
Python Input and Output
Signal Handling in Python:

2. Handling keyboard interruption (CTRL + C) using signal handling in Python.
Python Signal Handling
Data Processing:

3. Parsing strings to extract specific data points.
Aggregating data to compute summaries.
Regular Expressions:

4. Using regular expressions to validate the format of each line.
Python Regular Expressions
Dictionaries in Python:

5. Using dictionaries to count occurrences of status codes and accumulate file sizes.
Python Dictionaries
Exception Handling:

6. Handling possible exceptions that may arise during file reading and data processing.
Python Exceptions 
