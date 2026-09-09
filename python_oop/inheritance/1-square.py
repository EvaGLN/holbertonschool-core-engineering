#!/usr/bin/env python3
"""Square"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Class of a square inheriting Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
