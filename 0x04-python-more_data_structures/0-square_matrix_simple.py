#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = [row[:] for row in matrix]
    for idx, rows in enumerate(new_mat):
        for idx2, colms in enumerate(new_mat):
            new_mat[idx][idx2] = rows[idx2] ** 2
    return new_matrix
