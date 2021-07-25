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
1 <= beginWord.length <= 5\
endWord.length == beginWord.length\
1 <= wordList.length <= 1000\
wordList[i].length == beginWord.length\
beginWord, endWord, and wordList[i] consist of lowercase English letters.\
beginWord != endWord\
All the words in wordList are unique.\

Thinking
-------------------
* So a big idea is this has to be backtracking, we have to try before we know which ladder works.

* But the problem is how to choose what word next:
    * is there a way to determine one letter difference?
    * The contraint that is useful here is the word at most have 5 letters. So if we try all possible ways, there are 5 * 24 = 120 ways for each word. 
    * If we can form a one letter difference word and find if the word is in the word list, then we could continue on the path. 

* We could use dfs to search for a path, but since the problems asks for shortest path, we need to use bfs.
    * A problem is how to store what we used on the way, cause we can't make the ladder goes back
    * Create a dict of sets. For each new word, update the key in the map to map to current set.
    * But we also need to store an array to remember the sequence

* I realize this actually doesn't work. Two paths can be different at first, but merge in the end. So we can't use the word as key to store set and list.

* A simple way to do this is actually storing the whole path in set, but that would create memory exceed
    * To optimize it, we can create a data structure to store the paths
    * In this way, the queue won't store as many items as before, rather it stores fewer ladder object
    * The data structure needs to 
        * remember all the paths sharing the same last word
    * reference: https://fizzbuzzed.com/top-interview-questions-4/
* Create a state variable to store whether we have reached the end

* This question is definitely a hard one. Although it only adds a bit more requirement than the word_ladder I. It's definitely a tough problem if met in interview.
    * Familiar with BFS and DFS will definitely help
    * Graph algorithm remains a challenge to me
'''
from typing import List
from collections import deque, defaultdict
import copy


class WordLadder:
    def __init__(self, begin_word):
        self.ladder = [[begin_word]]

    def get_last_word(self):
        return self.ladder[0][-1]

    def merge_ladder(self, other):
        self.ladder += other.ladder

    def append_word(self, word):
        for path in self.ladder:
            path.append(word)

    def get_ladder(self):
        return self.ladder


def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    queue = deque([WordLadder(beginWord)])

    # To avoid circling back to seen words
    seen = set([beginWord])
    word_list = set(wordList)

    final_ladder = None

    while queue:
        n = len(queue)
        # Keep a dictionary of word mapping to ladder
        seen_this_level = {}

        for i in range(n):
            ladder = queue.popleft()
            for candidate in generate_neighbor(ladder.get_last_word(), wordList):
                new_ladder = copy.deepcopy(ladder)
                new_ladder.append_word(candidate)
                if candidate == endWord:
                    if final_ladder:
                        final_ladder.merge_ladder(new_ladder)
                    else:
                        final_ladder = new_ladder
                elif candidate in seen_this_level:
                    seen_this_level[candidate].merge_ladder(new_ladder)
                else:
                    seen_this_level[candidate] = new_ladder
                    queue.append(new_ladder)
        if final_ladder:
            break
        seen |= seen_this_level.keys()
    return final_ladder.get_ladder() if final_ladder else []
# neighbor generator


def generate_neighbor(word, wordList):
    for i in range(len(word)):
        for letter in "abcdefghijklmnopqrstuvwxyz":
            new_word = word[:i] + letter + word[i+1:]
            if new_word in wordList:
                yield new_word


if __name__ == "__main__":
    print(findLadders("hit",
                      "cog",
                      ["hot", "dot", "dog", "lot", "log", "cog"]))
