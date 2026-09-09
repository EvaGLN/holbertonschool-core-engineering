#!/usr/bin/env python3
"""Extending the Python List"""


class VerboseList(list):
    """Class for verboselist"""
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
