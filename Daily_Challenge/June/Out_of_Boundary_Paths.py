''' 
The Problem
-------------------
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. 
You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). 
You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary.
Since the answer can be very large, return it modulo 10^9 + 7.


1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n


Thinking
-------------------
* Write a function to find the moves of a small matrix

Brute Force
-------------------
* DFS the square, add one to total ways if the position is out of boundary

Optimization 1
-------------------
* Since the moves are not constrained, every extra double moves can count towards one more since the ball could simply return and back


Solution
-------------------
* Dynamic Programming
    * build a 3D matrix arr[d][i][j], where each cell equal to way to get out of boundary using d steps
    * Then gradually build up to [maxMove][i][j]


Reflection
-------------------
* Dynamic Programming is definitely a hard topic. The problem is dynamic programming can't be come up with easily
  If I don't associate the problem with dp, I may think the problem to be very complex and don't have a clue
  That means, if I don't have a sense of what problem could be solved by DP, DP could be a very hard thing to solve

* Move somewhere using maximum step is hard to calculate, but move somewhere using exact x steps are easier. The situtaions are easier to think

* Don't think too hard on sophistacted rules, the grid problem should be easy to solve and only consider one step around it.
'''


def findPaths(m, n, maxMove, startRow, startColumn):
    dp = [[[0 for j in range(n)] for i in range(m)]
          for d in range(maxMove + 1)]

    # Initialize the matrix dp[1][i][j], four corner = 2, edge = 1

    corner_x = [0, 0, m - 1, m - 1]
    corner_y = [0, n - 1, 0, n - 1]

    for j in range(0, n):
        dp[1][0][j] += 1
        dp[1][m-1][j] += 1

    for i in range(0, m):
        dp[1][i][0] += 1
        dp[1][i][n-1] += 1

    # print(dp[1])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for d in range(2, maxMove + 1):
        for i in range(m):
            for j in range(n):
                for k in range(4):
                    if i + dx[k] >= 0 and i + dx[k] < m and j + dy[k] >= 0 and j + dy[k] < n:
                        dp[d][i][j] += dp[d-1][i + dx[k]][j + dy[k]]
                        # dp[d][i][j] %= 10e9 + 7

    total_paths = 0
    for d in range(1, maxMove + 1):
        total_paths += dp[d][startRow][startColumn]
        # total_paths %= 10e9 + 7
    return int(total_paths)


if __name__ == "__main__":
    print(findPaths(1, 3, 3, 0, 1))
