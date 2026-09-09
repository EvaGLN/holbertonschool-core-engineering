#!/usr/bin/env python3
"""Square #2"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Class of a square inheriting Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return super().__str__().replace("Rectangle", "Square", 1)
