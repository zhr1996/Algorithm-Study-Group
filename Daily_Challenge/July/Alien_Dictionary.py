'''
Problem
-------------------
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

Constraints
-------------------
1 <= words.length <= 100\
1 <= words[i].length <= 100\
words[i] consists of only lowercase English letters.\

Thinking
-------------------
* Kind of like prerequisite. If we can form a graph, we can check if such order is possible by going over and detect if there is any loop

* Create a graph, then do a topological sort

* First create a hashmap with mapping from letter to graph node

* Second create the graph by iterating through all the words in list

* Third do a topological sort for all the nodes in graph
    * Iterate through the keys in hashmap
    * Using BFS to do topological sort
        * create a queue for node to be visited, for each node in current queue, add it in the result array (they come after the parent node)
    * Keep a set to store visited node

* Just use a hashmap with letters as keys,

* Correction: Use DFS is more intuitive than using BFS. Using DFS we can start on a random node, but using BFS we have to start at node having in-degree 0.
    * Always visit child node and when finish, put current node to the first, so that to make sure that parent node is before child node.
    * Checking loop is easy, for each dfs, we maintain a stack to track current visited node. It's also more intuitive.

* I literally take one day to finish writing this. Although I know I should use topological sort and have the letters turned into a graph. It's so hard to write a bugless typological sort.
  Let alone there are tricky corner cases.
'''
from typing import List
from collections import deque, defaultdict


def alienOrder(words: List[str]) -> str:
    letter_next_map = defaultdict(set)
    letter_set = set()

    # add all character into set
    for word in words:
        letter_set.update(set(word))
    for i in range(len(words) - 1):
        letter_differ = False
        word_one = words[i]
        word_two = words[i+1]
        for j in range(min(len(word_one), len(word_two))):
            if word_one[j] != word_two[j]:
                letter_next_map[word_one[j]].add(word_two[j])
                letter_differ = True
                break
        if len(word_one) > len(word_two) and not letter_differ:
            return ""

    alien_order = deque()
    letter_visited = set()

    def helper(letter, visited):
        if letter in letter_visited:
            return False
        letter_visited.add(letter)

        letter_next_set = letter_next_map[letter]
        visited.add(letter)
        for next_letter in letter_next_set:
            # detect loop
            if next_letter in visited:
                return True

            visited.add(next_letter)
            if helper(next_letter, visited):
                return True
            visited.remove(next_letter)

        alien_order.appendleft(letter)
        return False

    for letter in letter_set:
        if helper(letter, set([letter])):
            return ""
    return "".join(alien_order)


if __name__ == "__main__":
    print(alienOrder(["abc", "ab"]))
