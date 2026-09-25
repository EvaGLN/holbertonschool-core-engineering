<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Python - Functions & Modularity

## Table of Contents :

  - [0. islower](#subparagraph0)
  - [1. To Uppercase](#subparagraph1)
  - [2. Print Last Digit](#subparagraph2)
  - [3. a ^ b](#subparagraph3)
  - [4. Script Execution and Import Behavior](#subparagraph4)
  - [5. Import a Simple Function from a Simple File](#subparagraph5)
  - [6. My First Toolbox](#subparagraph6)
  - [7. Everything Can Be Imported](#subparagraph7)
## Introduction & Context

As programs grow, repeating logic becomes inefficient and error-prone.
Functions allow you to encapsulate behavior into reusable blocks.
Modules allow you to organize those functions into separate files and reuse them safely.

This project introduces:

* Function definition and return values
* Execution flow inside and outside functions
* Separation between printing and returning
* How Python executes a file
* How importing a file affects execution
* How to reuse functions and variables across files

The order of the exercises is intentional. The project progresses from defining functions to safely organizing code across multiple files.

---

## Learning Objectives

By the end of this project, you should be able to:

* Define functions with parameters and return values.
* Distinguish clearly between `print` and `return`.
* Implement logic inside functions using conditionals and loops.
* Understand how Python executes top-level code in a file.
* Explain what `if __name__ == "__main__"` does and why it is necessary.
* Import functions from other files.
* Import variables from other files.
* Write scripts that behave correctly when executed and when imported.

---

## Resources

* Python Tutorial — Defining Functions
  [https://docs.python.org/3/tutorial/controlflow.html#defining-functions](/rltoken/W0Rdp1xi3LDSsOFUw8JRGg)

* Python Tutorial — Modules
  [https://docs.python.org/3/tutorial/modules.html](/rltoken/E4k-zIOr64_PaCn4uXNA0A)

* Python Reference — `__name__`
  [https://docs.python.org/3/library/__main__.html](/rltoken/41qOjxYsKQFCyLNubVATUw)

* PEP8 Style Guide
  [https://peps.python.org/pep-0008/](/rltoken/51HrWLChrAi_OeUQytszYw)

---

## General Requirements

* Corrections will run on **Ubuntu 20.04 LTS**.
* Python version used for correction: **Python 3.8.x**.
* The first line of every Python file must be exactly:

```
#!/usr/bin/env python3
```

* All files must:

    * Be executable.
    * End with a newline.
    * Be PEP8 compliant (pycodestyle 2.7.x).
* No external libraries are allowed.
* No use of `sys.argv` in this project.
* Each task must follow its own constraints precisely.


## Task
### 0. islower <a name='subparagraph0'></a>

Write a function:

```python
def islower(c):
```

The function must return `True` if `c` is a lowercase letter and `False` otherwise.

Constraints:

* You are not allowed to use built-in string methods such as `.islower()`.
* You must use ASCII logic (`ord()`).
* The function must return a boolean value.

Example:

```python
>>> islower('a')
True
>>> islower('A')
False
>>> islower('3')
False
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/functions_modules`
* File: `islower.py`

---

### 1. To Uppercase <a name='subparagraph1'></a>

Write a function:

```python
def uppercase(str):
```

The function must print the string in uppercase followed by a new line.

Constraints:

* You are not allowed to use `.upper()`.
* You must use ASCII conversion (`ord()` and `chr()`).
* The function must print the `result` directly.
* The function does not return a value.

Example

```python-repl
>>> uppercase("Holberton")
HOLBERTON
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/functions_modules`
* File: `uppercase.py`

---

### 2. Print Last Digit <a name='subparagraph2'></a>

Write a function:

```python
def print_last_digit(number):
```

The function must:

* Print the last digit of `number`.
* Return the value of the last digit.

The last digit must always be positive.

Example:

```python-repl
>>> print_last_digit(98)
8
>>> print_last_digit(-1024)
4
```

The printed digit must appear without extra text.

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/functions_modules`
* File: `print_last_digit.py`

---

### 3. a ^ b <a name='subparagraph3'></a>

Write a function:

```css
def pow(a, b):
```

The function must return the value of `a` raised to the power of `b`.

Constraints:

* You are not allowed to use the built-in exponent operator `**`.
* You are not allowed to import modules.
* You must implement the logic manually using a loop.

Example:

```python-repl
>>> pow(2, 4)
16
>>> pow(5, 0)
1
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/functions_modules`
* File: `pow.py`

---

### 4. Script Execution and Import Behavior <a name='subparagraph4'></a>

### Introduction

Until now, you have defined functions and executed them within the same file. In this task, you will analyze what changes when functions are placed in one file and that file is reused from another.

When Python imports a file, it executes the file from top to bottom in order to create its namespace. This means that:

* Function definitions are executed.
* Variable assignments are executed.
* Any top-level statements (including `print`) are also executed.

If execution is not controlled, importing a file can trigger unintended behavior.

The objective of this task is to:

* Observe the difference between executing a file directly and importing it.
* Understand why top-level code runs during import.
* Learn the role of `if __name__ == "__main__"`.
* Distinguish clearly between defining behavior and executing behavior.

You must carefully observe the behavior before and after introducing the execution guard. The quiz following this task will evaluate your understanding of these concepts.

### Instructions:

Create two files:

File: `simple_add.py`

* Define a function `add(a, b)` that returns the sum of two numbers.
* At the **top level of the file** (outside any function, but after the definition), call the function and print the result of:

```scss
add(3, 5)
```

File: `test_import.py`

* Import `simple_add`.
* Run `python3 test_import.py`

Observe what happens.

Then modify `simple_add.py`:

* Move the print call inside:

```markdown
if __name__ == "__main__":
```

Run again.

You must ensure:

* When running `python3 simple_add.py`, the result is printed.
* When running `python3 test_import.py`, nothing is printed.

### Reflection (Before Quiz)

Before attempting the quiz, take a few minutes to reflect on the following points:

* Why does the print statement execute during import before adding the execution guard?
* What is the value of `__name__` when a file is executed directly?
* What is the value of `__name__` when a file is imported?
* Why does moving the print statement inside `if __name__ == "__main__":` change the behavior?

You are not required to submit written answers. However, you are strongly encouraged to reason through these questions carefully before continuing.

The quiz that follows:

* Has a strict time limit per question (between 45 and 60 seconds).
* Can only be attempted once (one-shot attempt).

Make sure you fully understand the execution model before starting the quiz.

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/functions_modules`

---

### 5. Import a Simple Function from a Simple File <a name='subparagraph5'></a>

Write a program that imports the function `add()` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`

```css
def add(a, b):
```

The program must:

* Assign `1` to a variable `a`.
* Assign `2` to a variable `b`.
* Print:

```undefined
1 + 2 = 3
```

Constraints:

* You are not allowed to use `*` for importing.
* You are not allowed to use `__import__`.
* The program must not execute when imported.

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/functions_modules`
* File: `add.py`

---

### 6. My First Toolbox <a name='subparagraph6'></a>

Write a program that imports functions from calculator_1.py and prints the result of:

* addition
* subtraction
* multiplication
* division

Using:

```ini
a = 10
b = 5
```

Each operation must be printed on its own line.

Constraints:

* You are not allowed to use `*` for importing.
* The program must not execute when imported.

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/functions_modules`
* File: `calculation.py`

---

### 7. Everything Can Be Imported <a name='subparagraph7'></a>

Write a program that imports the variable `a` from `variable_load_5.py` and prints its value.

Constraints:

* You are not allowed to use `*` for importing.
* The program must not execute when imported.

Example:

```undefined
98
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/functions_modules`
* File: `variable_load.py`

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
