<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Python - Flujo de control

## Table of Contents :

  - [0. Positive anything is better than negative nothing](#subparagraph0)
  - [1. The last digit](#subparagraph1)
  - [2. Alphabet Game (Lowercase)](#subparagraph2)
  - [3. Hexadecimal Printing](#subparagraph3)
  - [4. 00...99](#subparagraph4)
  - [5. Combinations of Two Digits](#subparagraph5)
  - [6. Control Flow Concepts Quiz](#subparagraph6)
## Introduction & Context

Programs become meaningful when they can make decisions and repeat actions. Control flow allows a program to:

* Execute different code depending on conditions.
* Repeat instructions using loops.
* Combine logical conditions to model real scenarios.

This project focuses exclusively on control flow using:

* `if`, `elif`, `else`
* Comparison operators
* Boolean logic
* `while` loops
* `for` loops with `range()`

The activities are adapted from the existing "Python - if/else, loops, functions" project, keeping only those aligned with control flow.

---

## Learning Objectives

By the end of this project, you should be able to:

* Write conditional statements using `if`, `elif`, and `else`.
* Use comparison and logical operators correctly.
* Control repetition using `while` and `for` loops.
* Reason about loop boundaries and iteration ranges.
* Generate formatted output using numeric iteration.
* Combine conditions and loops to produce deterministic output.

---

## Resources

* Python Tutorial — Control Flow Tools
  [https://docs.python.org/3/tutorial/controlflow.html](/rltoken/h5wcjRShf3KJAzr29WnAcg)

* Python Tutorial — More on Conditions
  [https://docs.python.org/3/reference/expressions.html#comparisons](/rltoken/Ijkz_u6qSXvDRSUE2RIZuQ)

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
* No functions are allowed in this project.
* No imports are allowed.
* Output must match expected formatting exactly.


## Task
### 0. Positive anything is better than negative nothing <a name='subparagraph0'></a>

Create a script that assigns a random integer to a variable named `number`. Copy the following line **exactly** as it is, after the shebang line.

```python
number = __import__('random').randint(-10, 10)
```

> The previous line will assign a random integer between -10 and 10 to the `number` variable. You don't need to focus on this yet.

Using conditional statements, print:

* `<number> is positive` if the number is greater than 0
* `<number> is zero` if the number equals 0
* `<number> is negative` if the number is less than 0

Example:

```ruby
spam@camelot:~/$ ./positive_or_negative.py 
-4 is negative
spam@camelot:~/$ ./positive_or_negative.py 
0 is zero
spam@camelot:~/$ ./positive_or_negative.py 
-3 is negative
spam@camelot:~/$ ./positive_or_negative.py 
-10 is negative
spam@camelot:~/$ ./positive_or_negative.py 
10 is positive
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/control_flow`
* File: `positive_or_negative.py`

---

### 1. The last digit <a name='subparagraph1'></a>

Assign a random integer to `number`. Copy the following line **exactly** as it is, after the shebang line.

```python
number = __import__('random').randint(-10000, 10000)
```

Compute the last digit and print:

* `Last digit of <number> is <digit> and is greater than 5`
* `Last digit of <number> is <digit> and is 0`
* `Last digit of <number> is <digit> and is less than 6 and not 0`

Output must match exactly the expected structure.

```ruby
spam@camelot:~/$ ./last_digit.py
Last digit of -9200 is 0 and is 0
spam@camelot:~/$ ./last_digit.py
Last digit of 5247 is 7 and is greater than 5
spam@camelot:~/$ ./last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/control_flow`
* File: `last_digit.py`

---

### 2. Alphabet Game (Lowercase) <a name='subparagraph2'></a>

Print the lowercase alphabet except for `q` and `e`.

Output must be continuous (no spaces, no new lines except at end).

You can only use print once in your code

Expected pattern:

```text
abcdfghijklmnoprstuvwxyz
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/control_flow`
* File: `print_alphabt.py`

---

### 3. Hexadecimal Printing <a name='subparagraph3'></a>

Print numbers from 0 to 98 in decimal and hexadecimal.

Format:

```text
0 = 0x0
1 = 0x1
...
98 = 0x62
```

* You can only use **one** `print` function **with string format**
* You can only use **one loop** in your code
* You are **not** allowed to store numbers or strings in a variable

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/control_flow`
* File: `print_hexa.py`

---

### 4. 00...99 <a name='subparagraph4'></a>

Print numbers from 0 to 99 formatted as two-digit numbers separated by comma and space.

Last number must not be followed by comma.

Example beginning:

```text
00, 01, 02, 03, ...
```

* Correct formatting with **leading zeros**.
* No trailing comma.
* Exact spacing.
* The last number should be followed by a **new line**
* You can only use **no more** than 2 `print` functions with string format
* You can only use **one loop** in your code
* You are not allowed to store numbers or strings in a variable

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/control_flow`
* File: `print_comb2.py`

---

### 5. Combinations of Two Digits <a name='subparagraph5'></a>

Print all unique combinations of two different digits from 0 to 9.

Rules:

* Digits must be different.
* Combinations must be printed in ascending order. (Print only the smallest combination of two digits)
* Format: `01, 02, 03, ..., 89` (Numbers must be separated by `,` followed by a space)
* No repetition ("01" and "10" are the same combination of digits).
* You can only use no more than 3 `print` functions with string format
* You can only use no more than 2 loops in your code

```ruby
spam@camelot:~/$ ./print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/control_flow`
* File: `print_comb3.py`

---

### 6. Control Flow Concepts Quiz <a name='subparagraph6'></a>

This task validates conceptual understanding of:

* Condition evaluation
* Boolean logic
* Loop boundaries
* Range behavior
* Off-by-one reasoning

You have 45 seconds to answer each question.

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
