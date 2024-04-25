#!/usr/bin/python3
"""A pascal traingle module"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []

    if n <= 0:
        return triangle
    for t in range(n):
        tempList = []

        for j in range(t+1):
            if j == 0 or j == t:
                tempList.append(1)
            else:
                tempList.append(triangle[t-1][j-1] + triangle[t-1][j])
        triangle.append(tempList)

    return triangle
