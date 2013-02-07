# -*- coding: utf-8 -*-
__author__ = 'S1ndb@d'

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.


def transporting_square(p):
    length = len(p)
    column = []
    i = 0
    while i < length:
        j = 0
        column.append([])
        while j < length:
            column[i].append(p[j][i])
            j += 1
        i += 1
    return column



def check_sudoku(p):
    length = len(p)
    transported = transporting_square(p)
    if p == transported:
        for e in p:
            i = 0
            while i < length - 1:
                if e[i] == e[i+1]:
                    return False
                elif e[i] > length or e[i] < 0:
                    return False
                i += 1
        return True
    else:
        return False
