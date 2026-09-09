#!/usr/bin/env python3
"""Shapes, Interfaces, and Duck Typing"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Class for Shape inheriting ABC"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Class for Circle inheriting Shape"""
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return (pi * (self.__radius * self.__radius))

    def perimeter(self):
        return (2 * pi * self.__radius)


class Rectangle(Shape):
    """Class for Rectangle inheriting Shape"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (2 * (self.__width + self.__height))


def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
