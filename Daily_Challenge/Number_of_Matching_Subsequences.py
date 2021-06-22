''' The Problem
-------------------
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.


Thinking
-------------------
Brute force, for each word in word list, compare to see if it's a subsequence of s

Optimize 1: Use a hash map to check if the letters are the same (Time Out)
-------------------
Still don't work, example test case: word is "gp", s is 5*10^4 - 1 "g", and the last one is "p"

what makes hash map not enought to determine whether the word is a subsequence? the relative position of characters

How to memorize what characters we have checked and what position did we put it in ?

Optimize 2: Use a hashmap to store index of character of s, and use a pointer to point where we are matching s (Accepted)
-------------------
In this way, we can check if there is next char available in s quickly. The way we achieve this is using binary search.

In python, bisect can be used to find a num in list using binary search

Note:
-------------------
* index_s should start from -1. Since we are ensuring each found index greater than the index_s

Time complexity: O(len(words) * len(word) * log(len(s)))
'''


from typing import List, Mapping
from bisect import bisect_left


def numMatchingSubseq(s: str, words: List[str]) -> int:
    numOfSubsequences = 0
    s_map = {}

    for index, character in enumerate(s):
        if character not in s_map:
            s_map[character] = []
        s_map[character].append(index)

    # test_list = [7, 8, 9, 10, 15]
    # print(bisect_left(test_list, 9))  # expect 2

    for word in words:
        # First check whether the characters are in s
        # word_map = {}
        # for character in word_map:
        #     word_map[character] += 1

        # char_exist = True
        # for character in word_map:
        #     if word_map[character] > s_map[character]:
        #         char_exist = False
        #         break

        # if not char_exist:
        #     continue
        index_s = -1
        is_subsequence = True
        for character in word:
            if character not in s_map:
                is_subsequence = False
                break
            index_list = s_map[character]
            index_in_list = bisect_left(index_list, index_s)

            if index_in_list == len(index_list):
                # print(character)
                # print(index_in_list)
                is_subsequence = False
                break

            if index_list[index_in_list] == index_s:
                index_in_list += 1
                if index_in_list == len(index_list):
                    is_subsequence = False
                    break

            index_s = index_list[index_in_list]
        if is_subsequence:
            numOfSubsequences += 1
    return numOfSubsequences


if __name__ == "__main__":
    print(numMatchingSubseq("abcde", [
          "a"]))
