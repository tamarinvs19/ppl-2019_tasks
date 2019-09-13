from spiral_matrix import *


def test_spiral_matrix_1():
    n = 1
    expected = [[1]]
    assert expected == spiral_matrix(n)

def test_spiral_matrix_2():
    n = 3
    expected = [
            [9, 8, 7],
            [2, 1, 6],
            [3, 4, 5],
            ]
    assert expected == spiral_matrix(n)

def test_spiral_matrix_3():
    n = 5
    expected = [
            [25, 24, 23, 22, 21],
            [10,  9,  8,  7, 20],
            [11,  2,  1,  6, 19],
            [12,  3,  4,  5, 18],
            [13, 14, 15, 16, 17]
            ]
    assert expected == spiral_matrix(n)

