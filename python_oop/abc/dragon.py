#!/usr/bin/env python3
"""The Mystical Dragon - Mastering Mixins"""


class SwimMixin:
    """Class of swimmixin"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Class of flymixin"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class of dragon inheriting SwimMixin & FlyMixin"""
    def roar(self):
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()
    dragon.fly()
    dragon.roar()
