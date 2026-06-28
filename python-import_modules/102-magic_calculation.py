#!/usr/bin/python3
def magic_calculation(a, b):
    """Reproduces the given bytecode."""
    result = 0
    for i in range(1, 3):
        if a < i:
            result += b
    return result
