'''
Problem
-------------------
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].



Constraints
-------------------


Thinking
-------------------
* First BFS, then DFS
'''
from typing import List
from collections import deque, defaultdict


def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    queue = deque([beginWord])
    seen = set([beginWord])

    word_list = set(wordList)

    parents = defaultdict(set)

    def generate_neighbor(word, wordList):
        for i in range(len(word)):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + letter + word[i+1:]
                if new_word in wordList:
                    yield new_word
    while queue:
        n = len(queue)
        finished = False
        seen_this_level = set()
        for i in range(n):
            queue_item = queue.popleft()
            for candidate in generate_neighbor(queue_item, word_list):
                if candidate == endWord:
                    finished = True
                elif candidate in seen:
                    continue
                if candidate not in seen_this_level:
                    queue.append(candidate)
                parents[candidate].add(queue_item)
        if finished:
            break
        seen |= seen_this_level

    def create_all_paths(parentDict, word, beginWord):
        if word == beginWord:
            return [[beginWord]]
        output = []
        for w in parentDict[word]:
            x = create_all_paths(parentDict, w, beginWord)
            for l in x:
                l.append(word)
                output.append(l)
        return output
    return create_all_paths(parents, endWord, beginWord)


if __name__ == "__main__":
    print(function)
