#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for i in matrix:
        square_i = []
        for n in i:
            if isinstance(n, int):
                square_i.append(n ** 2)
            else:
                square_i.append(n)
        newmatrix.append(square_i)
    return (newmatrix)
