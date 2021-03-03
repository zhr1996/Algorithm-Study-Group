class Solution:
    #  First reverse whole string, and then reverse each word in the string

    def reverse(self, l, start, end):
        while start < end:
            l[start], l[end] = l[end], l[start]
            start += 1
            end -= 1

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)
        self.reverse(s, 0, n - 1)

        start_word = 0
        end_word = 0

        while start_word < n:
            while s[start_word] == " ":
                start_word += 1

            # if the last character is space and space
            if start_word >= n:
                break

            end_word = start_word  # point end to start first

            # Move end pointer to the next " "
            while end_word < n and s[end_word] != " ":
                end_word += 1

            self.reverse(s, start_word, end_word - 1)

            start_word = end_word + 1

        return
