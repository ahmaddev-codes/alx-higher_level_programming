## 0X0A - Python inheritance
### Learning Objectives:
* Why Python programming is awesome
* What is a superclass, baseclass or parentclass
* What is a subclass

## Tasks:
### [0. Lookup](./0-lookup.py)
Write a function that returns the list of available attributes and methods of an object:
* Prototype: def lookup(obj):
* Returns a list object
* You are not allowed to import any module

### [1. My list](./1-my_list.py)
Write a class MyList that inherits from list:
* Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
* You can assume that all the elements of the list will be of type int
* You are not allowed to import any module

### [2. Exact same object](./2-is_same_class.py)
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
* Prototype: def is_same_class(obj, a_class):
* You are not allowed to import any module

### [3. Same class or inherit from](./3-is_kind_of_class.py)
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
* Prototype: def is_kind_of_class(obj, a_class):
* You are not allowed to import any module

### [4. Only sub class of](./4-inherits_from.py)
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
* Prototype: def inherits_from(obj, a_class):
* You are not allowed to import any module

### [5. Geometry module](./5-base_geometry.py)
Write an empty class BaseGeometry.
* You are not allowed to import any module

### [6. Improve Geometry](./6-base_geometry.py)
Write a class BaseGeometry (based on 5-base_geometry.py).
* Public instance method: def area(self): that raises an Exception with the message area() is not implemented
* You are not allowed to import any module
