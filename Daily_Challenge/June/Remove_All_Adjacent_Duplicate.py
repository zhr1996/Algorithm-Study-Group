'''
Problem
-------------------
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

1 <= s.length <= 105
s consists of lowercase English letters.

Thinking
-------------------
* Finding anagram in a string? First find the pivot and then compare left and right, if they are the same, left-- and right++ until they are different

* Store all the index of character to be removed in a set and later create an array to include only the not removed characters

* next round start with right if right != left, compare right and right + 1

* This algorithm is wrong!!!, this not equivalent anagrams, for example, "aaaaa", the remove has to form pairs, but anagram doesn't

* According to hint, use a stack to gradually add and compare

Summary
-------------------
* Using the most suit data structure is very important

* Consider stack when the problem asks to delete something and compare the item before it
'''
from typing import List


def removeDuplicates(s: str) -> str:
    stack = [s[0]]
    for i in range(1, len(s)):
        if len(stack) != 0 and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    return "".join(stack)


if __name__ == "__main__":
    print(removeDuplicates("abcddd"))
