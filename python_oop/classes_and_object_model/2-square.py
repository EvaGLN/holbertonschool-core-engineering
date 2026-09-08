#!/usr/bin/env python3
"""Module to ensure that object state is valid."""


class Square:
    """Class for a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
