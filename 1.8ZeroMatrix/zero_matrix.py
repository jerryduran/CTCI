import unittest
#O(MxN)

def zero_matrix(matrix):
    """-------"""
    row = []
    col = []
    m = len(matrix)  # num of column
    n = len(matrix[0])  # num of rows

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)
    for i in row:
        nullify_row(matrix, i)

    for i in row:
        nullify_col(matrix, i)

    return matrix


def nullify_row(matrix, i):
    for y in range(len(matrix[0])):
        matrix[i][y] = 0



def nullify_col(matrix, i):
    for x in range(len(matrix)):
        matrix[x][i] = 0


class TestZeroMatrix(unittest.TestCase):
    """Test Case"""
    matrix = [
        [1, 0, 3, 4],
        [0, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    zeroMatrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 11, 12],
    ]

    def test_zero_matrix(self):
        self.assertEqual(zero_matrix(self.matrix), self.zeroMatrix)


if __name__ == "__main__":
    unittest.main()

