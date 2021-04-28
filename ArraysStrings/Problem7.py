# Given an image of an N - by - N matrix with each pixel being 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do it in place?

# Notes: This problem is actually a bit tricky thanks to index gymnastics.
# Debugging took me awhile to find the error, originally had col in
# range(row, rows - row), but you want to stop one less than that otherwise
# it performs extra rotations and messes the whole thing up.

import random

def rotate_matrix(matrix):

    rows = len(matrix)

    for row in range(rows):
        for col in range(row, rows - row - 1):
            u = matrix[row][col]
            # r = matrix[col][rows -1 - row]
            # d = matrix[rows - 1 - row][rows - 1 - col]
            # l = matrix[rows -1 - col][row]

            matrix[row][col] = matrix[rows -1 - col][row]
            matrix[rows - 1 - col][row] = matrix[rows - 1 - row][rows - 1 - col]
            matrix[rows - 1 - row][rows - 1 - col] = matrix[col][rows -1 - row]
            matrix[col][rows - 1 - row] = u

    return




def main():

    mat = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6],
           [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
    ans = [[5, 4, 3, 2, 1], [6, 5, 4, 3, 2],
           [7, 6, 5, 4, 3], [8, 7, 6, 5, 4],
           [9, 8, 7, 6, 5]]

    rotate_matrix(mat)
    assert mat == ans

    mat = []
    for idx in range(4):
        mat.append([314 * random.lognormvariate(0, 1) for _ in range(4)])

    print("Original matrix: ", mat)
    rotate_matrix(mat)
    print("Rotated matrix: ", mat)




if __name__ == "__main__":
    main()
    print("Problem 7")