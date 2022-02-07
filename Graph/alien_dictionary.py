'''
Problem
-------------------
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

Constraints
-------------------
* 1 <= words.length <= 100
* 1 <= words[i].length <= 100
* words[i] consists of only lowercase English letters.

Thinking
-------------------
* topological sorting

* problem is how should we build the graph?
    * every time there is a letter that is different, we have an order
    * we can go through each letter in each word pair, which would need
        * O(N*N*L), L is max length of words
        * 100 * 100 * 100 = 10^6

* then we can build the topological sorting
'''
import collections
from typing import List
from collections import deque, defaultdict


def alienOrder(words: List[str]) -> str:
    graph = defaultdict(set)

    in_degree = {c: 0 for word in words for c in word}

    zero_degree_queue = deque()

    for i in range(len(words)):
        for j in range(i+1, len(words)):
            char_different = False
            for k in range(min(len(words[i]), len(words[j]))):
                if words[i][k] != words[j][k]:
                    if words[j][k] not in graph[words[i][k]]:
                        graph[words[i][k]].add(words[j][k])
                        in_degree[words[j][k]] += 1
                    # break the loop if a different char is found
                    char_different = True
                    break
            if not char_different and len(words[j]) < len(words[i]):
                return ""
    for key in in_degree:
        if in_degree[key] == 0:
            zero_degree_queue.appendleft(key)

    result_arr = []
    while zero_degree_queue:
        cur_char = zero_degree_queue.pop()
        result_arr.append(cur_char)
        for next_char in graph[cur_char]:
            in_degree[next_char] -= 1
            if in_degree[next_char] == 0:
                zero_degree_queue.appendleft(next_char)
    return "".join(result_arr) if len(result_arr) == len(in_degree) else ""


if __name__ == "__main__":
    print(alienOrder(["abc", "ab"]))
