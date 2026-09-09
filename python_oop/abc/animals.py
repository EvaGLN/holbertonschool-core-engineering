#!/usr/bin/env python3
"""Abstract Animal Class and its Subclasses"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Class of Animal"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Class of Dog inheriting Animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Class of Cat inheriting Animal"""
    def sound(self):
        return "Meow"
