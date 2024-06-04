#!/usr/bin/python3
"""
Generate Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    result = []
    for i in range(n):
        append_list = [1]
        if i == 0:
            result.append(append_list)
            continue
        if i > 1:
            for j in range(1, i):
                append_list.append(result[i-1][j-1] + result[i-1][j])
        append_list.append(1)
        result.append(append_list)
    return result
