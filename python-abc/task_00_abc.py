#!/usr/bin/python3
"""Module that defines an abstract Animal class and its subclasses"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing a generic animal"""

    @abstractmethod
    def sound(self):
        """Abstract method that returns the sound the animal makes"""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal"""

    def sound(self):
        """Return the sound a dog makes"""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal"""

    def sound(self):
        """Return the sound a cat makes"""
        return "Meow"
