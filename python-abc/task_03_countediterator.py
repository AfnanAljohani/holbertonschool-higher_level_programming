#!/usr/bin/python3
"""Module defining CountedIterator that tracks iteration count"""


class CountedIterator:
    """An iterator wrapper that keeps track of items iterated over"""

    def __init__(self, iterable):
        """Initialize with an iterable and a counter set to zero

        Args:
            iterable: Any iterable to iterate over
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items iterated over so far"""
        return self.count

    def __next__(self):
        """Fetch the next item and increment the counter

        Returns:
            The next item from the iterator

        Raises:
            StopIteration: When there are no more items
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """Return the iterator object itself"""
        return self
