#!/usr/bin/python3
"""
returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Represent Pascal's Triangle of size n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        trian = triangle[-1]
        tmep = [1]
        for i in range(len(trian) - 1):
            tmep.append(trian[i] + trian[i + 1])
        tmep.append(1)
        triangle.append(tmep)
    return triangle
