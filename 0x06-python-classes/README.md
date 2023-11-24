## 0x06-python-classes
### General Overview:
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
* What are the special `__str__` and `__repr__` methods and how to use them
* What is the difference between `__str__` and `__repr__`
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain `__dict__` of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the `getattr` function

## Files
### [0-square.py](0-square.py)
* Write an empty class Square that defines a square:
* You are not allowed to import any module

### [1-square.py](1-square.py)
* Write a class Square that defines a square by: (based on 0-square.py)
* Private instance attribute: size
* Instantiation with size (no type/value verification)
* You are not allowed to import any module

Why?
Why `size` is private attribute?
* The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

### [2-square.py](2-square.py)
* Write a class Square that defines a square by: (based on 1-square.py)
* Private instance attribute: size
* Instantiation with optional size: `def __init__(self, size=0):`
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* You are not allowed to import any module

### [3-square.py](3-square.py)
* Write a class Square that defines a square by: (based on 2-square.py)
* Private instance attribute: size
* Instantiation with optional size: `def __init__(self, size=0):`
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Public instance method: `def area(self):` that returns the current square area
* You are not allowed to import any module

### [4-square.py](4-square.py)
* Write a class Square that defines a square by: (based on 3-square.py)
* Private instance attribute: size:
* property def size(self): to retrieve it
* property setter def size(self, value): to set it:
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Instantiation with optional size: `def __init__(self, size=0):`
* Public instance method: `def area(self):` that returns the current square area
* You are not allowed to import any module
Why?

Why a getter and setter?
* Reminder: `size` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.
Reminder: `size` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

### [5-square.py](5-square.py)
* Write a class Square that defines a square by: (based on 4-square.py)
* Private instance attribute: size:
  * property def size(self): to retrieve it
  * property setter def size(self, value): to set it:
    * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    * if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Instantiation with optional `size`: `def __init__(self, size=0):`
* Public instance method: `def area(self):` that returns the current square area
* Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
  * if size is equal to 0, print an empty line
* You are not allowed to import any module

### [6-square.py](6-square.py)
* Write a class `Square` that defines a square by: (based on `5-square.py`)
* Private instance attribute: `size`:
* property `def size(self):` to retrieve it
* property setter `def size(self, value):` to set it:
  * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
  * if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Private instance attribute: `position`:
  * property `def position(self):` to retrieve it
  * property setter `def position(self, value):` to set it:
    * `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integer`
* Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
* Public instance method: `def area(self):` that returns the current square area
* Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
  * if `size` is equal to 0, print an empty line
  * `position` should be use by using space - Don’t fill lines by spaces when `position[1] > 0`
* You are not allowed to import any module

### [101-square.py](101-square.py)
* Write a class Square that defines a square by: (based on 6-square.py)
* Private instance attribute: size:
* property def size(self): to retrieve it
* property setter def size(self, value): to set it:
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Private instance attribute: position:
* property def position(self): to retrieve it
* property setter def position(self, value): to set it:
* position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integer
* Instantiation with optional size and optional position: `def __init__(self, size=0, position=(0, 0)):`
* Public instance method: `def area(self):` that returns the current square area
* Public instance method: `def my_print(self):` that prints in stdout the square with the character #:
* if size is equal to 0, print an empty line
* position should be use by using space
* print position should be use by using space - Don’t fill lines by spaces when position[1] > 0
* You are not allowed to import any module

### [102-square.py](102-square.py)
* Write a class Square that defines a square by: (based on 4-square.py)
* Private instance attribute: size:
* property def size(self): to retrieve it
* property setter def size(self, value): to set it:
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Private instance attribute: position:
* property def position(self): to retrieve it
* property setter def position(self, value): to set it:
* position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
* Instantiation with optional size and optional position: `def __init__(self, size=0, position=(0, 0)):`
* Public instance method: `def area(self):` that returns the current square area
* Public instance method: `def my_print(self):` that prints in stdout the square with the character #:
* if size is equal to 0, print an empty line
* position should be use by using space
* print position should be use by using space - Don’t fill lines by spaces when position[1] > 0
* You are not allowed to import any module

### [103-magic_class.py](103-magic_class.py)
* Write the Python class MagicClass that does exactly the same as the following Python bytecode:
```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60

 12          27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 13          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 14     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE