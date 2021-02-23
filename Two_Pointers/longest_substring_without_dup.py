# Longest substring without duplicate

def longest_substring_without_repeating_characters(s):
    # WRITE YOUR BRILLIANT CODE HERE
    l = r = 0
    window = set()
    max_length = 0
    while r < len(s):
        if s[r] not in window:
            window.add(s[r])

            max_length = max(max_length, r - l + 1)

            r += 1
            # print("l " + str(l) + "r " + str(r))

        else:
            window.remove(s[l])
            l += 1
    return max_length


if __name__ == '__main__':
    print(longest_substring_without_repeating_characters(input()))
