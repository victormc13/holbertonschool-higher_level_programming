# Python - Classes and Objects 
## Background Context
It’s VERY important that you read at least all the material that is listed below (and skip what we recommend you to skip, you will see them later in the curriculum).

As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

Read or watch the below resources in the order presented.

## Resources
**Read or watch**:

* [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, `classmethod` and `staticmethod` yet)

* [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The `__init__` Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)

* [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
* [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
* [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

### General
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is `self`
* What is a method
* What is the special `__init__` method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is the `__dict__` of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use the `getattr` function

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## More Info
**Documentation is now mandatory!** Each module, class, and method must contain docstring as comments. [Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) [Google Style Docstrings for classes](https://google.github.io/styleguide/pyguide.html#384-classes)

## Tasks

### 0-square.py
Write an empty class Square that defines a square:

* You are not allowed to import any module

### 1-square.py
Write a class `Square` that defines a square by: (based on `0-square.py`)

* Private instance attribute: `size`
* Instantiation with `size` (no type/value verification)
* You are not allowed to import any module

**Why?**
Why `size` is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

### 2-square.py
Write a class `Square` that defines a square by: (based on `1-square.py`)

* Private instance attribute: `size`
* Instantiation with optional `size`: `def __init__(self, size=0):`
  * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
  * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* You are not allowed to import any module

### 3-square.py
Write a class `Square` that defines a square by: (based on `2-square.py)

* Private instance attribute: `size`
* Instantiation with optional `size`: `def __init__(self, size=0):`
  *`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
  * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* Public instance method: `def area(self):` that returns the current square area
* You are not allowed to import any module

### 4-square.py
Write a class `Square` that defines a square by: (based on `3-square.py`)

* Private instance attribute: `size`:
  * property `def size(self):` to retrieve it
  * property setter `def size(self, value):` to set it:
    * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* Instantiation with optional `size`: `def __init__(self, size=0):`
* Public instance method: `def area(self):` that returns the current square area
* You are not allowed to import any module

**Why?**

Why a getter and setter?

Reminder: `size` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

