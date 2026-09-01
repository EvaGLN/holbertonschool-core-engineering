# Python - Functions & Modularity

* Novice
* By: Javier Valenzani
* Weight: 1
* Your score will be updated as you progress.

## Introduction & Context

As programs grow, repeating logic becomes inefficient and error-prone. Functions allow you to encapsulate behavior into reusable blocks. Modules allow you to organize those functions into separate files and reuse them safely.

This project introduces:

* Function definition and return values
* Execution flow inside and outside functions
* Separation between printing and returning
* How Python executes a file
* How importing a file affects execution
* How to reuse functions and variables across files

The order of the exercises is intentional. The project progresses from defining functions to safely organizing code across multiple files.

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

## Resources

* [Python Tutorial — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* [Python Tutorial — Modules](https://docs.python.org/3/tutorial/modules.html)
* [Python Reference — `__name__`](https://docs.python.org/3/library/main.html)
* [PEP8 Style Guide](https://peps.python.org/pep-0008/)

## General Requirements

* Corrections will run on Ubuntu 20.04 LTS.
* Python version used for correction: Python 3.8.x.
* The first line of every Python file must be exactly:

```shell
#!/usr/bin/env python3
```

* All files must:
  * Be executable.
  * End with a newline.
  * Be PEP8 compliant (pycodestyle 2.7.x).
* No external libraries are allowed.
* No use of `sys.argv` in this project.
* Each task must follow its own constraints precisely.