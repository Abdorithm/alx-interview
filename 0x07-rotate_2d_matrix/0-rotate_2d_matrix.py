#!/usr/bin/python3
"""
Rotate 2d matrix module
"""


def rotate_2d_matrix(matrix):
    """Rotate the matirx to the right
    """
    matrix[:] = list(map(list, zip(*matrix)))
    for m in matrix:
        m.reverse()
