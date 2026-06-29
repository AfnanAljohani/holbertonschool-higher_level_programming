#!/usr/bin/python3
"""Solves the N queens puzzle.

Places N non-attacking queens on an N*N chessboard and prints
every possible solution, one per line.
"""
import sys


def is_safe(positions, row, col):
    """Check whether a queen can be placed at the given row and column.

    Args:
        positions: List of column indices for queens already placed.
        row: The row of the new queen.
        col: The column of the new queen.
    Returns:
        True if no queen attacks the new position, otherwise False.
    """
    for r in range(row):
        c = positions[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(n, row, positions, solutions):
    """Recursively place queens using backtracking.

    Args:
        n: The size of the board and number of queens.
        row: The current row being filled.
        positions: List of column indices for placed queens.
        solutions: Accumulator list for complete solutions.
    """
    if row == n:
        solutions.append([[i, positions[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(positions, row, col):
            positions[row] = col
            solve(n, row + 1, positions, solutions)


def main():
    """Validate the argument and print all N queens solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    solve(n, 0, [0] * n, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
