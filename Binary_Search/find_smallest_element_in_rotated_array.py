# Can be thought of as a boundary problem
# The criteria for boundary is that on right side all elements are smaller or equal !! to the last element of array
# and on left side all elements are bigger than the last element

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        boundary_index = low

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= nums[-1]:
                # could be the boundary point
                # remember the current index as potential result
                boundary_index = mid
                #  The right side couldn't be the boundary point
                high = mid - 1
            else:
                # left part ruled out
                low = mid + 1
        return nums[boundary_index]

        # def findMin(self, nums: List[int]) -> int:
        #         def helper(arr):
        #             if arr[0] <= arr[-1]:
        #                 return arr[0]
        #             mid = len(arr) // 2
        #             return min(helper(arr[:mid]), helper(arr[mid:]))

        #         return helper(nums)
