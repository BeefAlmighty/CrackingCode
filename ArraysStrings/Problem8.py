# Zero matrix. If an element in a matrix is zero, the row and column containing
# that entry are set to zero as well.


def zeros(matrix):
    if len(matrix) == 0:
        return
    rows = set()
    cols = set()

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)

    for row in rows:
        for col in range(num_cols):
            matrix[row][col] = 0

    for col in cols:
        for row in range(num_rows):
            matrix[row][col] = 0

    return



def main():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    zeros(mat)
    assert mat ==  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 0, 0]]
    zeros(mat)
    assert mat ==  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    mat =  [[1, 2, 3], [4, 0, 6], [7, 8, 9], [3, 1, 4]]
    zeros(mat)
    assert mat == [[1, 0, 3], [0, 0, 0], [7, 0, 9], [3, 0, 4]]

    mat = []
    zeros(mat)
    assert mat == []

    mat = [[1, 2, 3], [0, 5, 6], [7, 8, 0], [3, 1, 4]]
    zeros(mat)
    assert mat == [[0, 2, 0], [0, 0, 0], [0, 0, 0], [0, 1, 0]]




if __name__ == "__main__":
    main()
    print("Problem 8")