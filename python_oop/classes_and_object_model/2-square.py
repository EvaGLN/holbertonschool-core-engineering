#!/usr/bin/env python3
"""Module for a square size validation"""


class Square:
    """Class for a square with a private instance attribute size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
