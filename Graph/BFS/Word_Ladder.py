from typing import List
from collections import deque


def get_list_distance_of_one(word, word_list):
    result = []
    for element in word_list:
        difference = 0
        for index in range(len(word)):
            if word[index] != element[index]:
                difference += 1
        if difference == 1:
            result.append(element)
    return result


def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    graph = {}
    # build graph
    for word in word_list:
        graph[word] = get_list_distance_of_one(word, word_list)

    print(graph)
    # Do a bfs on graph, remember to keep visited points
    level = 0
    queue = deque([begin])
    visited = set()

    while len(queue) != 0:
        n = len(queue)
        for i in range(len(queue)):
            word = queue.popleft()
            if word == end:
                return level
            visited.add(word)
            for neighbor in graph[word]:
                if neighbor not in visited:
                    queue.append(neighbor)
        level += 1
    return -1


if __name__ == "__main__":
    start = input()
    end = input()
    word_list = input().split()
    print(word_ladder(start, end, word_list))
