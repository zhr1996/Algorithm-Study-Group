''' The Problem
-------------------
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108


Thinking
--------------------
* Add up all the path length and divide by 4, find a to determine if the result can be made up by the matchstick

* Brute force: try all the combinations possible, but this takes too much trails, the length of matchstick is too long

* Surprisingly, this could work, by adding a small trick sorting the match length from long to short


'''

from typing import List


def makesquare(matchsticks: List[int]) -> bool:
    # Initialize four sides, in this initial solution, I plan to try out all the possibilities
    # First try dfs search, recursively try all the possible combinations
    # dfs means that we form a complete combination before forming the next one. If current formed combination works, we return True,
    # If not, we continue on next iteration

    sumArray = [0 for i in range(4)]

    matchSum = sum(matchsticks)

    if matchSum % 4 != 0:
        return False

    sideLength = matchSum // 4

    matchsticks.sort(reverse=True)

    def dfs(index):
        if index == len(matchsticks):
            return sumArray[0] == sumArray[1] == sumArray[2] == sideLength

        for i in range(4):
            # print(i, index)
            if sumArray[i] + matchsticks[index] <= sideLength:
                sumArray[i] += matchsticks[index]
                if dfs(index + 1):
                    return True
                sumArray[i] -= matchsticks[index]

        return False
    return dfs(0)


if __name__ == "__main__":
    print(makesquare([1, 3, 5, 7]))
