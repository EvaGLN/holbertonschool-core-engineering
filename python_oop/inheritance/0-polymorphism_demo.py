#!/usr/bin/env python3
"""Introduction to Inheritance and Polymorphism"""


class Animal:
    """Class for Animal"""
    def speak(self):
        return "Some sound"

class Dog(Animal):
    """Class for Dog"""
    def speak(self):
        return "Woof"

class Cat(Animal):
    """Class for Cat"""
    def speak(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))
