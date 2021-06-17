''' The Problem
-------------------
You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

1 <= colors.length <= 5*10^4
1 <= colors[i] <= 3
1 <= queries.length <= 5*10^4
queries[i].length == 2
0 <= queries[i][0] < colors.length
1 <= queries[i][1] <= 3


June 17th
-------------------

* Brute Force, start from taht index, and look left and right until find that color, if not, then return -1

* Convert the color list into three list, {"1":[list of index with color 1], "2": [list of idnex with color 2], "3": [list of index with color 3]}
  then the question convert to finding the nearest number in a list and the list is sorted. So clearly using a binary search.

* Find nearest is the same as finding the first samller number, because it is either at index[first_small] or index[first_small+1], so actually we can use bisect.bisect_left here

* bisect.bisect_left will find the insertion point, so actually it will find first greater number, and if the entry is present, it wil return the index on left

* Remember when finding the index, we still need the num at the index of the array to compute the shortest distance
'''


from typing import List
import bisect


def shortestDistanceColor(colors: List[int], queries: List[List[int]]) -> List[int]:
    queryResult = []

    # pre-processing
    colorDict = {}

    for index, color in enumerate(colors):
        if color not in colorDict:
            colorDict[color] = []
        colorDict[color].append(index)

    for query in queries:
        queryIndex = query[0]
        queryColor = query[1]

        if queryColor not in colorDict:
            queryResult.append(-1)
            continue

        colorIndexArray = colorDict[queryColor]

        insertPoint = bisect.bisect_left(colorIndexArray, queryIndex)
        # print(insertPoint)

        leftDistance = abs(
            colorIndexArray[max(insertPoint - 1, 0)] - queryIndex)
        rightOrEqualDistance = abs(
            colorIndexArray[min(insertPoint, len(colorIndexArray) - 1)] - queryIndex)

        queryResult.append(min(leftDistance, rightOrEqualDistance))
    return queryResult


if __name__ == "__main__":
    print(bisect.bisect_left([0, 3, 4], 1))
    print(shortestDistanceColor(
        [2, 1, 2, 2, 1],
        [[1, 1], [4, 3], [1, 3], [4, 2], [2, 1]]))
