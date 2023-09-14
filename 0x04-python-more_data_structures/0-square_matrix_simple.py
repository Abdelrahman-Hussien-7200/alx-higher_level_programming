#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [rows[:] for rows in matrix]
    for idx, rows in enumerate(new_matrix):
        for idx2, col in enumerate(new_matrix):
            new_matrix[idx][idx2] = rows[idx2] ** 2
    return new_matrix
