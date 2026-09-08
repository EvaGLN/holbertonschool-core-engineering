#!/usr/bin/env python3
"""Module for the area of a square"""


class Square:
    """Class to return the area of the square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return self.__size * self.__size
