## 0X12-JAVASCRIPT_WARM_UP
### Learning Objectives
  - Why JavaScript programming is amazing
  - How to run a JavaScript script
  - How to create variables and constants
  - What are differences between var, const and let
  - What are all the data types available in JavaScript
  - How to use the if, if ... else statements
  - How to use comments
  - How to affect values to variables
  - How to use while and for loops
  - How to use break and continue statements
  - What is a function and how do you use functions
  - What does a function that does not use any return statement return
  - Scope of variables
  - What are the arithmetic operators and how to use them
  - How to manipulate dictionary
  - How to import a file

### Requirements
    - All your files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
    - The first line of all your files should be exactly #!/usr/bin/node
    - A README.md file, at the root of the folder of the project, is mandatory
    - Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
    - All your files must be executable
    - The length of your files will be tested using wc
    - You are not allowed to use var

### More Info
Install Node 10
```sh
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
Install semi-standard
```sh
$ sudo npm install semistandard --global
```
Install `request` module and use it
```sh
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
### Tasks
files | description
----- | -----------
[0-javascript_is_amazing](./0-javascript_is_amazing.js) | Write a script that prints “Javascript is amazing”
[1-multi_languages](./1-multi_languages.js) | Write a script that prints 3 lines
[2-arguments](./2-arguments.js) | Write a script that prints a message depending of the number of arguments passed
[3-value_argument](./3-value_argument.js) | Write a script that prints the first argument passed to it
[4-concat](./4-concat.js) | Write a script that prints two arguments passed to it, in the following format: “ is ”
[5-to_integer](./5-to_integer.js) | Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
[6-multi_languages_loop](./6-multi_languages_loop.js) | Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
[7-multi_c](./7-multi_c.js) | Write a script that prints x times “C is fun”
[8-square](./8-square.js) | Write a script that prints a square
[9-add](./9-add.js) | Write a script that prints the addition of 2 integers
[10-factorial](./10-factorial.js) | Write a script that computes and prints a factorial
[11-second_biggest](./11-second_biggest.js) | Write a script that searches the second biggest integer in the list of arguments
[12-object](./12-object.js) | Update this script to replace the value 12 with 89
[13-add](./13-add.js) | Write a function that returns the addition of 2 integers
[100-let_me_const](./100-let_me_const.js) | Write a file that modifies the value of myVar to 333
[101-call_me_moby](./101-call_me_moby.js) | Write a function that executes x times a function
[102-add_me_maybe](./102-add_me_maybe.js) | Write a function that increments and calls a function
[103-object_fct](./103-object_fct.js) | Update this script by adding a new function incr that increments the integer value
[104-search_comfortable](./104-search_comfortable.js) | Write a script that imports an array and computes a new array
[105-task_search](./105-task_search.js) | Write a script