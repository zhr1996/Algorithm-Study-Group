# class Solution:
#     # Chain will be disrupted by 0 or negative number, but if met with a negative number, still could hope for the next negative number to turn the sign around
def maxProduct(nums):
    min_array = [1 for x in range(len(nums))]
    max_array = [1 for x in range(len(nums))]

    min_array[0] = nums[0]
    max_array[0] = nums[0]

    max_result = nums[0]
    for i in range(1, len(nums)):
        min_array[i] = min(nums[i], nums[i] * max_array[i-1],
                           nums[i] * min_array[i-1])
        max_array[i] = max(nums[i], nums[i] * max_array[i-1],
                           nums[i] * min_array[i-1])
        max_result = max(max_result, max_array[i])

    arr = []
    max_index = max_array.index(max_result)
    temp = max_result
    if temp == 0:
        print([0])
    else:
        for i in range(max_index, -1, -1):
            arr.append(nums[i])
            if temp == nums[i]:
                break
            temp /= nums[i]
        arr = arr[::-1]
        print(arr)
    return max_result


print(maxProduct([-2, 1, 2, 0.3, -1, 2, 3, -1, 4]))
print(maxProduct([0, 0, 0, 0]))
