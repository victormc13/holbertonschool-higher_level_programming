# Python - if/else, loops, functions

## Resources
**Read or watch:**
- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (Read until "4.6. Defining Functions" included)
- [IndentationError](https://docs.python.org/3/tutorial/errors.html)
- [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
- [Learn to Program 2 : Looping](https://docs.python.org/3/tutorial/introduction.html#first-steps)
- [Pycodestyle – Style Guide for Python Code](https://pep8.org/)

**Man or help:**
- `python3`

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
- Why indentation is so important in Python
- How to use the `if`, `if ... else` statements
- How to use comments
- How to assign values to variables
- How to use the `while` and `for` loops
- How to use the `break` and `continue` statements
- How to use `else` clauses on loops
- What the `pass` statement does, and when to use it
- How to use `range`
- What is a function and how to use functions
- What a function that does not use any `return` statement returns
- Scope of variables
- What's a traceback
- What are the arithmetic operators and how to use them

## Requirements
**Python Scripts**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.*)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use `pycodestyle` (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## More Info
Note: you do not need to understand lists yet.

### 0-positive_or_negative.py
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

You can find the source code here
The variable number will store a different value every time you will run this program
You don’t have to understand what import, random. randint do. Please do not touch this code
The output of the program should be:
The number, followed by
if the number is greater than 0: is positive
if the number is 0: is zero
if the number is less than 0: is negative
followed by a new line

### 1-last_digit.py
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

You can find the source code here
The variable number will store a different value every time you will run this program
You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)
The output of the program should be:
The string Last digit of, followed by
the number, followed by
the string is, followed by the last digit of number, followed by
if the last digit is greater than 5: the string and is greater than 5
if the last digit is 0: the string and is 0
if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
followed by a new line
