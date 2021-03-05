# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive find the path that sums to the given target sum
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        count_result = 0

        def helper(cur_sum, cur_path, root, target):
            if root is None:
                return
            nonlocal count_result

            # add in the current node value
            # path now contains current node
            cur_sum += root.val
            cur_path.append(root)

            if cur_sum == target:
                count_result += 1

            temp_sum = cur_sum

            # Notice here the last element is current node, we don't want to pop out the last element
            for i in range(0, len(cur_path) - 1):
                temp_sum -= cur_path[i].val
                if temp_sum == target:
                    count_result += 1

            # left
            helper(cur_sum, cur_path, root.left, target)

            # right
            helper(cur_sum, cur_path, root.right, target)

            cur_path.pop()
            return

        helper(0, [], root, sum)

        return count_result
