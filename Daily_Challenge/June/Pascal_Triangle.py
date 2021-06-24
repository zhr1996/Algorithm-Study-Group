
from typing import List


def generate(self, numRows: int) -> List[List[int]]:
    pascalTriangle = []

    # Row No.1
    pascalTriangle.append([1])

    for row in range(2, numRows + 1):
        prevRow = pascalTriangle[row - 2]
        curRow = [1]
        for j in range(2, row):
            curRow.append(prevRow[j-2] + prevRow[j-1])
        curRow.append(1)
        pascalTriangle.append(curRow)
    return pascalTriangle
