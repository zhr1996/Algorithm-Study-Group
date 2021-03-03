

def merge_sort(arr):
    # print(arr)
    # base case
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # print("left" + str(left))
    # print("right" + str(right))
    l, r = 0, 0
    merged_array = []
    while l < len(left) or r < len(right):
        if l >= len(left) or (r < len(right) and right[r] < left[l]):
            merged_array.append(right[r])
            r += 1

        else:
            merged_array.append(left[l])
            l += 1

    # print(merged_array)
    return merged_array


print(merge_sort([1, 2, 4, 3, 2, 1, 4, 2, 31, 32, 12, 53, 1]))
