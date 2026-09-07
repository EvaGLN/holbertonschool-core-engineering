# Python - Exception Handling

* Novice
* By: Javier Valenzani
* Weight: 1
* Your score will be updated as you progress.

## Introduction & Context

Real-world programs must be resilient. Inputs may be invalid, data may be missing, and operations may fail unexpectedly. Exception handling allows a program to detect errors, respond appropriately, and continue execution safely when possible.

In this project, you will learn how Python handles runtime errors and how to manage them using:

* `try` / `except`
* Specific exception types
* `else` and `finally` blocks
* Raising exceptions explicitly

The exercises focus on writing defensive, predictable code.

## Learning Objectives

By the end of this project, you should be able to:

* Identify common runtime exceptions (`TypeError`, `IndexError`, `ZeroDivisionError`, `KeyError`).
* Use `try` and `except` blocks correctly.
* Catch specific exception types rather than broad exceptions.
* Use `else` and `finally` appropriately.
* Raise exceptions explicitly when required.
* Write functions that fail safely and predictably.

## Resources

* [Python Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

## General Requirements

* Corrections will run on Ubuntu 20.04 LTS.
* Python version used for correction: Python 3.8.x.
* Every Python file must start exactly with:

```shell
#!/usr/bin/env python3
```

* Every Python file must:
  * Be executable.
  * End with a newline.
  * Be PEP8 compliant (pycodestyle 2.7.x).
* No external libraries are allowed.
* Unless explicitly stated, do not use broad `except:` blocks.