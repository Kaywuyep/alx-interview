#!/usr/bin/python3
"""
A N-queen board
"""

import sys


def is_valid(board, row, col):
    # Check this column on upper side
    for i in range(row):
        if board[i] == col:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, len(board), 1)):
        if board[i] == j:
            return False
    return True


def solve_nqueens(board, row, solutions):
    if row == len(board):
        solutions.append(board[:])
        return
    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, solutions)
            board[row] = -1


def nqueens(N):
    if not isinstance(N, int):
        print_usage_and_exit("N must be a number")
    if N < 4:
        print_usage_and_exit("N must be at least 4")

    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, solutions)

    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")
    nqueens(N)


if __name__ == "__main__":
    main()
