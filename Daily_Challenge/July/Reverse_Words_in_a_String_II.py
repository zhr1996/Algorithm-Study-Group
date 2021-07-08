'''
Problem
-------------------
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

1 <= s.length <= 105
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.

Thinking
-------------------
* First instinct is use two pointers, one at start of word and one continue to reach the end of the word, and then do a reverse

* But this instinct is not right, the problem is asking us to reverse the words order in the string, not the words themselves.

* Combining this, we can
    * First reverse the whole string
    * reverse each word, since now the word is in reverse

* The problem ask the solution to be in place

* Note: don't forget to reverse the last word
'''
from typing import List


def reverseWords(s: List[str]) -> None:
    # First reverse the whole string
    def swap(index1, index2):
        temp = s[index2]
        s[index2] = s[index1]
        s[index1] = temp

    def swap_string(left, right):
        while left < right:
            swap(left, right)
            left += 1
            right -= 1

    swap_string(0, len(s) - 1)
    # Swap each word
    left = 0
    right = 0
    while right < len(s):
        if s[right] == " ":
            swap_string(left, right - 1)
            left = right + 1
        right += 1

    swap_string(left, right - 1)
    return


if __name__ == "__main__":
    s = ["t", "h", "e", " ", "s", "k",
         "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    print(reverseWords(s))
    print(s)
