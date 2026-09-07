# Python - Classes & Object Model

* Novice
* By: Javier Valenzani
* Weight: 1
* Your score will be updated as you progress.

## Introduction and Context

In previous Python projects you worked primarily with functions and data structures such as lists, dictionaries, and tuples. These constructs allow you to organize data and logic, but as software systems grow, managing complexity becomes increasingly difficult.

Object-Oriented Programming (OOP) provides a way to structure programs by modeling entities as objects that combine both data and behavior.

An object represents a concept from a system (for example, a user, a file, or a geometric shape). Each object contains:

* Attributes, which store data
* Methods, which define behavior

Objects are created from classes, which act as templates describing what data and behavior objects should have.

In this project, you will learn how to:

* Define classes
* Create objects (instances)
* Store and manage object state
* Implement methods that operate on object data
* Represent objects in a meaningful way

The goal of this project is to build a solid understanding of the Python object model, which is the foundation for more advanced concepts such as inheritance, polymorphism, and abstract classes.

## Learning Objectives

By completing this project, you should be able to:

* Explain the difference between a class and an instance
* Create classes that model simple entities
* Define and initialize instance attributes using `__init__`
* Implement instance methods that operate on object state
* Apply basic encapsulation principles
* Validate input when constructing objects
* Control access to internal attributes
* Implement string representations of objects using special methods
* Design simple classes that model real-world concepts

## Resources

Students should consult the following resources while working on the project:

* [Python documentation – Classes](https://intranet.hbtn.io/rltoken/6iU7VqCerKgnJs2fZFNnOg)
* [Python documentation – Special methods (`__init__`, `__str__`, `__repr__`)](https://intranet.hbtn.io/rltoken/hP-EBvnSM4zcWWMs3WnR5g)
* [Real Python: Object-Oriented Programming in Python](https://intranet.hbtn.io/rltoken/XquUh9ZnR8C1zerc9ZHumg)

Additional recommended reading:

* [Encapsulation in Python](https://intranet.hbtn.io/rltoken/mIezXm9d6YK5KZyh1OKWHg)
* [Python Classes and Objects](https://intranet.hbtn.io/rltoken/TtlqBpJ-4uetT1CwmQnhaw)

Students are encouraged to experiment with small examples in the Python interpreter while implementing each task.

## General Requirements

All tasks in this project must follow these requirements unless explicitly stated otherwise.

* The development environment used for evaluation is Ubuntu 20.04.
* Python version used for correction: Python 3.8.
* All Python files must be executable.
* The first line of all Python files must be:

```python
#!/usr/bin/env python3
```

This ensures the script uses the Python interpreter available in the system environment rather than relying on a fixed system path.

* All files must end with a new line.
* Code must follow PEP8 style guidelines.
* All modules, classes, and functions should include clear and concise documentation strings.
* No external libraries may be imported unless explicitly allowed.
* All scripts must behave exactly as specified in the task instructions.