# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

# Examples
# Example 1:
# Input: pattern = "abab", str = "redblueredblue"
# Output: true
# Example 2:
# Input: pattern = "aaaa", str = "asdasdasdasd"
# Output: true
# Example 3:
# Input: pattern = "aabb", str = "xyzabcxzyabc"
# Output: false

# State : 1. start index of remaining pattern to pair 2. start index of remaining string to pair 2. mapping from word to character
# Return : whether this mapping of words worked

# Drawing a state tree is a very good way to get clear about which state is to keep and which step to take next

# Draw a state tree! Draw a state tree! Draw a state tree!
class Solution:
    def wordPatternMatch(self, pattern: str, word: str) -> int:
        mapping = {}

        def helper(index_pattern, index_word):
            if index_pattern == len(pattern) and index_word == len(word):
                return True

            if index_pattern == len(pattern):
                return False

            if index_word == len(word):
                return False

            cur_pattern = pattern[index_pattern]
            if cur_pattern in mapping:
                mapping_word = mapping[cur_pattern]
                if word[index_word:].startswith(mapping_word):
                    return helper(index_pattern + 1, index_word + len(mapping_word))
                else:
                    return False

            # Backtracking
            for i in range(index_word+1, len(word) + 1):
                mapping_word = word[index_word:i]
                mapping[cur_pattern] = mapping_word
                if helper(index_pattern + 1, i):
                    return True
                del mapping[cur_pattern]

            return False
        return helper(0, 0)


if __name__ == "__main__":
    sol = Solution()
    pattern = input()
    word = input()
    if sol.wordPatternMatch(pattern, word):
        print('true')
    else:
        print('false')
