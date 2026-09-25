<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Python - Core Data Structures

## Table of Contents :

  - [0. Print a list of integers](#subparagraph0)
  - [1. Safe access to a list element](#subparagraph1)
  - [2. Replace an element in a list](#subparagraph2)
  - [3. Print a matrix of integers](#subparagraph3)
  - [4. Tuple addition](#subparagraph4)
  - [5. Common elements in two sets](#subparagraph5)
  - [6. Update or add a key/value in a dictionary](#subparagraph6)
  - [7. Best score](#subparagraph7)
  - [8. Core data structures quiz](#subparagraph8)
## Introduction & Context

In Python, most real programs are built around collections of values rather than single variables. A program that can store, group, transform, and query data is far more expressive and reusable.

This project focuses on core built-in data structures and the reasoning skills needed to choose and use them correctly:

* **Lists** for ordered, mutable sequences
* **Tuples** for ordered, immutable groupings
* **Sets** for unique elements and set operations
* **Dictionaries** for key–value mappings

You will implement small, focused functions that manipulate these structures predictably and safely.

---

## Learning Objectives

By the end of this project, you should be able to:

* Iterate over lists and matrices and produce exact, formatted output.
* Access and modify list elements safely without raising unexpected errors.
* Create new collections without mutating the original input when required.
* Use tuples to return multiple values in a clear, consistent way.
* Use sets to compute intersections and symmetric differences.
* Use dictionaries to add, update, and query key–value data.
* Reason about edge cases such as empty inputs, missing keys, and repeated values.

---

## Resources

* [Python Tutorial — Data Structures](/rltoken/ghlloGWLhYUXZLDyIqdYig)
* [Python Tutorial — Sets](/rltoken/LWlI8eGdqdS4Fi-lP6dPgg)
* [Python Tutorial — Dictionaries](/rltoken/cH94IwF1nuauoLNlI1HJQA)
* [Built-in Types (reference)](/rltoken/HDR6vTM7bzbIwK1z4OLnPA)

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
* Unless explicitly stated otherwise, do not import modules.


## Task
### 0. Print a list of integers <a name='subparagraph0'></a>

### Updated Project Instruction

Write a function that prints all integers of a list.

* Prototype: `def print_list_integer(my_list=[])`
* Format: one integer per line
* You may assume every element of `my_list` is an integer.

⚠️ **Important note:** You are expected to explicitly format integers using `:d` in your `print` statement. Even if your function works correctly without it, most of the automated checks will fail if `:d` is not used.

#### Execution example:

```shell
$ cat main.py
#!/usr/bin/env python3
print_list_integer = __import__('print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

$ ./main.py
1
2
3
4
5
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/core_data_structures`
* File: `print_list_integer.py`

---

### 1. Safe access to a list element <a name='subparagraph1'></a>

Write a function that retrieves an element from a list like in C.

* Prototype: `def element_at(my_list, idx):`
* If `idx` is negative or out of range, return `None`.
* Otherwise, return the element at position `idx`.

Execution example:

```text
$ cat main.py
#!/usr/bin/env python3
element_at = __import__('element_at').element_at

my_list = ["a", "b", "c", "d", "e"]
print(element_at(my_list, 3))
print(element_at(my_list, -1))
print(element_at(my_list, 15))

$ ./main.py
d
None
None
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/core_data_structures`
* File: `element_at.py`

---

### 2. Replace an element in a list <a name='subparagraph2'></a>

Write a function that replaces an element of a list at a specific position.

* Prototype: `def replace_in_list(my_list, idx, element):`
* If `idx` is negative or out of range, return the original list unchanged.
* Otherwise, replace the element at position `idx` with `element` and return the list.

Execution example:

```text
$ cat main.py
#!/usr/bin/env python3
replace_in_list = __import__('replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
print(replace_in_list(my_list, 3, 99))
print(replace_in_list(my_list, 15, 99))

$ ./main.py
[1, 2, 3, 99, 5]
[1, 2, 3, 99, 5]
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/core_data_structures`
* File: `replace_in_list.py`

---

### 3. Print a matrix of integers <a name='subparagraph3'></a>

Write a function that prints a matrix of integers.

* Prototype: `def print_matrix_integer(matrix=[[]]):`
* `matrix` is a list of lists (2D list).
* Format each row on its own line.
* Values in a row must be separated by a single space.

Execution example:

```text
$ cat main.py
#!/usr/bin/env python3
print_matrix_integer = __import__('print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)

$ ./main.py
1 2 3
4 5 6
7 8 9
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/core_data_structures`
* File: `print_matrix_integer.py`

---

### 4. Tuple addition <a name='subparagraph4'></a>

Write a function that adds two tuples.

* Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
* Return a new tuple with exactly two integers.
* Treat missing values as `0`.
* Ignore values beyond the first two.

Execution example:

```text
$ cat main.py
#!/usr/bin/env python3
add_tuple = __import__('add_tuple').add_tuple

print(add_tuple((1, 89), (88, 11)))
print(add_tuple((1, 89), (1, )))
print(add_tuple((1, 89), ()))
print(add_tuple((), ()))

$ ./main.py
(89, 100)
(2, 89)
(1, 89)
(0, 0)
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/core_data_structures`
* File: `add_tuple.py`

---

### 5. Common elements in two sets <a name='subparagraph5'></a>

Write a function that returns a set of common elements in two sets.

* Prototype: `def common_elements(set_1, set_2):`
* Return a **new** set containing only elements present in both `set_1` and `set_2`.

Execution example:

```text
$ cat main.py
#!/usr/bin/env python3
common_elements = __import__('common_elements').common_elements

set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
print(sorted(list(common_elements(set_1, set_2))))

$ ./main.py
['C']
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/core_data_structures`
* File: `common_elements.py`

---

### 6. Update or add a key/value in a dictionary <a name='subparagraph6'></a>

Write a function that replaces or adds a key/value pair in a dictionary.

* Prototype: `def update_dictionary(a_dictionary, key, value):`
* If `key` already exists, replace its value.
* If `key` does not exist, create it.
* Return the (updated) dictionary.

Execution example:

```text
$ cat main.py
#!/usr/bin/env python3
update_dictionary = __import__('update_dictionary').update_dictionary

d = {'language': 'C', 'number': 89, 'track': 'Low level'}
print(update_dictionary(d, 'language', 'Python'))
print(update_dictionary(d, 'city', 'San Francisco'))

$ ./main.py
{'language': 'Python', 'number': 89, 'track': 'Low level'}
{'language': 'Python', 'number': 89, 'track': 'Low level', 'city': 'San Francisco'}
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/core_data_structures`
* File: `update_dictionary.py`

---

### 7. Best score <a name='subparagraph7'></a>

Write a function that returns the key with the biggest integer value.

* Prototype: `def best_score(a_dictionary):`
* You may assume that all values are integers.
* If `a_dictionary` is `None` or empty, return `None`.
* You may assume all values are different.

Execution example:

```text
$ cat main.py
#!/usr/bin/env python3
best_score = __import__('best_score').best_score

scores = {'John': 12, 'Bob': 14, 'Mike': 15, 'Molly': 16, 'Adam': 10}
print(best_score(scores))
print(best_score(None))

$ ./main.py
Molly
None
```

**Repo:**

* GitHub repository: `holbertonschool-core-engineering`
* Directory: `python_fundamentals/core_data_structures`
* File: `best_score.py`

---

### 8. Core data structures quiz <a name='subparagraph8'></a>

Before taking the quiz, take a short moment to reflect. Writing anything is optional.

Consider the following prompts:

* When do you prefer a list over a set, and why?
* What is one situation where a tuple makes your code clearer than a list?
* When updating a dictionary, what changes when the key already exists versus when it does not?
* What edge cases did you explicitly handle in the functions above?

The quiz is **timed** (each question has a limit between **45 and 60 seconds**) and is **one-shot**.

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
