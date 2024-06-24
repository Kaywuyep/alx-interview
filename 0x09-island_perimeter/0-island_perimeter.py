#!/usr/bin/python3
"""
This module defines a function `island_perimeter` that calculates the perimeter
of an island in a grid of water and land.

The grid is represented by a 2D list where:
- 0 represents water
- 1 represents land

The function assumes there is only one island in the grid.
"""

# Sets to store cells with different numbers of exposed boundaries
bound_4 = set()
bound_3 = set()
bound_2 = set()
bound_1 = set()


def boundary(grid, i, j):
    """
    Find cells with either 4, 3, 2, or 1 exposed boundary and add them to
    the appropriate set.

    Args:
        grid (list): 2D list representing the grid
        i (int): Row number of the cell
        j (int): Column number of the cell
    """
    boundaries = 0
    # Check the upper cell
    if i == 0 or grid[i-1][j] == 0:
        boundaries += 1
    # Check the lower cell
    if i == len(grid) - 1 or grid[i+1][j] == 0:
        boundaries += 1
    # Check the right cell
    if j == len(grid[0]) - 1 or grid[i][j+1] == 0:
        boundaries += 1
    # Check the left cell
    if j == 0 or grid[i][j-1] == 0:
        boundaries += 1

    # Add the cell to the appropriate set based on the number of boundaries
    if boundaries == 1:
        bound_1.add((i, j))
    elif boundaries == 2:
        bound_2.add((i, j))
    elif boundaries == 3:
        bound_3.add((i, j))
    elif boundaries == 4:
        bound_4.add((i, j))


def island_perimeter(grid):
    """
    Calculate and return the perimeter of the island in the grid.
    
    The grid is a rectangular grid where 0s represent water and 1s represent land.
    Each cell is a square with a side length of 1.
    There is only one island.

    Args:
        grid (list): 2D list of integers (0 or 1)

    Returns:
        int: Perimeter of the island
    """
    if not grid:
        return 0

    l = len(grid)
    w = len(grid[0])
    for i in range(l):
        for j in range(w):
            if grid[i][j] == 1:
                boundary(grid, i, j)

    # Calculate the total perimeter
    perimeter = (len(bound_3) * 3) + (len(bound_2) * 2) + len(bound_1) + (len(bound_4) * 4)
    return perimeter

