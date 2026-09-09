# Python - Abstract Classes & Interfaces

* Novice
* By: Javier Valenzani
* Weight: 1
* Your score will be updated as you progress.

## Introduction and Context

In object-oriented programming, some classes are used to define a common contract for other classes.

Sometimes a class should define what behavior must exist, but not provide the full implementation itself. In Python, this can be modeled using abstract classes.

An abstract class allows you to define methods that subclasses are expected to implement. This helps create consistent designs where different objects share the same interface while keeping their own specific behavior.

A related concept is the idea of an interface. Python does not have a dedicated `interface` keyword, but similar results can be achieved using abstract methods or by relying on duck typing: if an object provides the required behavior, it can be used.

In this project, you will work with:

* abstract base classes
* abstract methods
* interface-like design
* duck typing
* subclassing built-in classes
* multiple inheritance
* mixins

These tools are useful when building flexible and reusable software designs.

## Learning Objectives

By completing this project, you should be able to:

* explain the purpose of an abstract class
* use `ABC` and `@abstractmethod`
* implement subclasses that satisfy an abstract contract
* understand how Python can model interfaces
* explain and apply duck typing
* extend built-in classes while preserving their behavior
* understand the role of multiple inheritance
* use mixins to add reusable behavior to a class

## Resources

Students are encouraged to consult the following resources.

* [Abstract Base Classes](https://intranet.hbtn.io/rltoken/PsGjF-n-V-pVBksLPiHv1A)
* [Python Tutorial — Classes](https://intranet.hbtn.io/rltoken/Cmr2kH1ri4x0usrDEpZ00A)
* [Real Python — Python Interfaces](https://intranet.hbtn.io/rltoken/r6aljYld9Cg1IG0TKWdTLw)
* [Real Python — Mixins and Multiple Inheritance](https://intranet.hbtn.io/rltoken/HcB7mB2RS1vFXURJXeCScw)
* [Geeks for Geeks — Abstract Classes in Python](https://intranet.hbtn.io/rltoken/rOIc14luuZV_B5RLmQrcoQ)

## Concept Guide

### Abstract Classes and Concrete Classes

An abstract class defines behavior that subclasses must implement.

For example, a class may define a method that all subclasses must provide, while leaving the actual implementation to each subclass.

A simplified relationship looks like this:

```
          Animal (Abstract Class)
                 │
        ┌────────┴────────┐
        │                 │
       Dog               Cat
   (Concrete Class)  (Concrete Class)
```

Interpretation:

* `Animal` defines required behavior
* `Dog` and `Cat` provide concrete implementations
* all subclasses share the same contract

### Duck Typing

In Python, objects are often used based on what they can do, not only on what they inherit from.

Example idea:

* if an object provides a method named `draw()`, it may be usable in a function that expects something drawable
* the object does not always need to inherit from a specific class for that use case

This approach is often called duck typing.

## General Requirements

All tasks in this project must follow these requirements unless otherwise specified.

### Environment

* Ubuntu 20.04
* Python 3.8

### Python files

All Python files must:

* be executable
* start with the following line

```python
#!/usr/bin/env python3
```

### Coding requirements

* All files must end with a newline
* Code must follow PEP8
* All modules, classes, and functions must include documentation strings
* Only the Python standard library may be used unless otherwise stated