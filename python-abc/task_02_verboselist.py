#!/usr/bin/python3
"""Module defining VerboseList, a list that notifies on changes"""


class VerboseList(list):
    """A list subclass that prints notifications when modified"""

    def append(self, item):
        """Append an item and print a notification"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print a notification"""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove an item and print a notification before removing"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print a notification before popping"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
