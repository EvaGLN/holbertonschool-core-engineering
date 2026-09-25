<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Python - Exception Handling

## Table of Contents :

  - [0. Safe list printing](#subparagraph0)
  - [1. Safe integer printing](#subparagraph1)
  - [2. Safe list printing with type handling](#subparagraph2)
  - [3. Divide two integers safely](#subparagraph3)
  - [4. Raise exception](#subparagraph4)
  - [5. Raise a message](#subparagraph5)
  - [6. Exception Handling Quiz](#subparagraph6)
## Introduction & Context

Real-world programs must be resilient. Inputs may be invalid, data may be missing, and operations may fail unexpectedly. Exception handling allows a program to detect errors, respond appropriately, and continue execution safely when possible.

In this project, you will learn how Python handles runtime errors and how to manage them using:

* `try` / `except`
* Specific exception types
* `else` and `finally` blocks
* Raising exceptions explicitly

The exercises are focus on writing defensive, predictable code.

---

## Learning Objectives

By the end of this project, you should be able to:

* Identify common runtime exceptions (TypeError, IndexError, ZeroDivisionError, KeyError).
* Use `try` and `except` blocks correctly.
* Catch specific exception types rather than broad exceptions.
* Use `else` and `finally` appropriately.
* Raise exceptions explicitly when required.
* Write functions that fail safely and predictably.

---

## Resources

* Python Tutorial — Errors and Exceptions
  [https://docs.python.org/3/tutorial/errors.html](/rltoken/Xsee8rcBA4p-DJWwg1OKFg)

* Built-in Exceptions
  [https://docs.python.org/3/library/exceptions.html](/rltoken/7s-IUYNaffm_mmK-TtYEYw)

---

## General Requirements

* Corrections will run on **Ubuntu 20.04 LTS**.
* Python version used for correction: **Python 3.8.x**.
* Every Python file must start exactly with:

  ```
  #!/usr/bin/env python3
  ```
* Every Python file must:

    * Be executable.
    * End with a newline.
    * Be PEP8 compliant (pycodestyle 2.7.x).
* No external libraries are allowed.
* Unless explicitly stated, do not use broad `except:` blocks.


## Task
### 0. Safe list printing <a name='subparagraph0'></a>

Write a function that prints `x` elements of a list.

* Prototype: `def safe_print_list(my_list=[], x=0):`
* `my_list` can contain any type (integer, string, etc.)
* All elements must be printed on the same line followed by a new line.
* `x` represents the number of elements to print
* `x` can be bigger than the length of `my_list`
* Returns the real number of elements printed
* You have to use `try: / except:`
* You are not allowed to import any module
* You are not allowed to use `len()`

```ruby
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
safe_print_list = __import__('safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print(f"elements: {nb_print}")

spam@camelot:~/$ ./main.py
12
nb_print: 2
spam@camelot:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/exception_handling`
* File: `safe_print_list.py`

---

### 1. Safe integer printing <a name='subparagraph1'></a>

Write a function that prints an integer with `"{:d}".format()` followed by a new line.

* Prototype: `def safe_print_integer(value):`
* If `value` is an integer, print it and return `True`.
* Otherwise, return `False`.
* You have to use `try: / except:`
* You are not allowed to import any module
* You are not allowed to use `type()

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/exception_handling`
* File: `safe_print_integer.py`

---

### 2. Safe list printing with type handling <a name='subparagraph2'></a>

Write a function that prints the first `x` elements of a list.

* Prototype: `def safe_print_list_integers(my_list=[], x=0):`
* Print only integers.
* Skip elements that are not integers.
* Return the number of integers printed.
* All integers have to be printed on the same line followed by a new line.
* `my_list` can contain any type (integer, string, etc.)
* You have to use `try: / except:`

```ruby
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
safe_print_list_integers = __import__('safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

spam@camelot:~/$ ./main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "//safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
spam@camelot:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/exception_handling`
* File: `safe_print_list_integers.py`

---

### 3. Divide two integers safely <a name='subparagraph3'></a>

Write a function that divides two integers.

* Prototype: `def safe_print_division(a, b):`
* Perform the division inside a `try` block.
* If any other exception occurs, print `"Inside result: None"`.
* Always print `"Inside result: <result>"` using `finally`.
* Return the result (or `None`).

```ruby
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
safe_print_division = __import__('safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

spam@camelot:~/$ ./main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
spam@camelot:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/exception_handling`
* File: `safe_print_division.py`

---

### 4. Raise exception <a name='subparagraph4'></a>

Write a function that raises a `TypeError`.

* Prototype: `def raise_exception():`
* The function must raise a `TypeError`.

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/exception_handling`
* File: `raise_exception.py`

---

### 5. Raise a message <a name='subparagraph5'></a>

Write a function that raises a `NameError` with a custom message.

* Prototype: `def raise_exception_msg(message=""):`
* The function must raise a `NameError` with `message`.

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/exception_handling`
* File: `raise_exception_msg.py`

---

### 6. Exception Handling Quiz <a name='subparagraph6'></a>

Before taking the quiz, reflect briefly on the following:

* What is the difference between catching a specific exception and using a broad `except`?
* When should you allow an exception to propagate instead of catching it?
* What guarantees does the `finally` block provide?

The quiz is timed (45–60 seconds per question) and is one-shot.

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
