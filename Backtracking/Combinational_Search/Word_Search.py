# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Combination Search
# Backtraking try every direction

from typing import List

# State: 1. current index of character pairing, 2. current node coordinate 3. visited[][] store all position visited
#        4. word we are searching, 5. possible moves
# Return: True or False


def helper(board, word, index, x, y, visited, moves):
    # base case, index is same with word length
    if index == len(word):
        return True
    if word[index] != board[x][y]:
        return False

    visited[x][y] = True
    for move in moves:
        if x + move[0] >= 0 and x + move[0] < len(board) \
                and y + move[1] >= 0 and y + move[1] < len(board[0]) \
                and not visited[x + move[0]][y + move[1]]:
            # print("reached")
            if helper(board, word, index + 1, x + move[0], y + move[1], visited, moves):
                return True
    visited[x][y] = False
    return False


def exist(board: List[List[str]], word: str) -> bool:
    if board == None:
        return False

    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited = [[False for x in range(len(board[0]))]
               for x in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if helper(board, word, 0, i, j, visited, moves):
                return True
    return False


if __name__ == "__main__":
    word = input()
    rows = int(input())
    board = [[str(x) for x in input().split()] for _ in range(rows)]
    result = exist(board, word)
    if result:
        print('true')
    else:
        print('false')
