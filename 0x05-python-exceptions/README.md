## 0x05-python-exceptions
### Description:
This project is treats errors and exceptions in Python
### FILES:
> [0-safe_print_list.py](0-safe_print_list.py)
- "Prints x elements of a list"
- Prototype: `def safe_print_list(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line
- `x` represents the number of elements to print
- `x` can be bigger than the length of `my_list`
- You have to use try: / except:
- You have to use "{:d}".format() to print as integer
- You are not allowed to import any module
- You are not allowed to use type()

> [1-safe_print_integer.py](1-safe_print_integer.py)
- "Prints an integer with "{:d}".format()"
- Prototype: `def safe_print_integer(value):`
- `value` can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns `True` if `value` has been correctly printed (it means the value is an integer)
- Otherwise, returns `False`
- You have to use try: / except:
- You have to use "{:d}".format() to print as integer
- You are not allowed to import any module
- You are not allowed to use type()

> [2-safe_print_list_integers.py](2-safe_print_list_integers.py)
- "Prints the first x elements of a list and only integers"
- Prototype: `def safe_print_list_integers(my_list=[], x=0):`
- my_list can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
- x represents the number of elements to access in my_list
- x can be bigger than the length of my_list
  - if it’s the case, an exception is expected to occur
- Returns the real number of integers printed
- You have to use `try: / except:`
- You have to use `"{:d}".format()` to print an integer
- You are not allowed to import any module
- You are not allowed to use `len()`

