#!/usr/bin/python3
"""This module defines a lazy matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the product of m_a and m_b computed with numpy.matmul."""
    return np.matmul(m_a, m_b)
