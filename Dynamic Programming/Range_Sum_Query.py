# @classmethod is a decrator is a decrator for creating class function

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sum_matrix = [[0 for x in range(len(matrix[0]) + 1)]
                           for y in range(len(matrix) + 1)]
        for i in range(m):
            for j in range(n):
                self.sum_matrix[i+1][j+1] = self.sum_matrix[i+1][j] + self.sum_matrix[i][j+1] + \
                    matrix[i][j] - self.sum_matrix[i][j]
        # Test
        # for row in self.sum_matrix:
        #     for col in row:
        #         print(col, end=" ")
        #     print()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.sum_matrix)
        return self.sum_matrix[row2 + 1][col2 + 1] - self.sum_matrix[row2 + 1][col1] \
            - self.sum_matrix[row1][col2 + 1] + \
            self.sum_matrix[row1][col1]


sum_obj = NumMatrix([[1, 1], [1, 1]])
print(sum_obj.sumRegion(0, 0, 1, 1))
