# Find all possible position to set the comma
# And for comma seperated left and right, generate possible decimal number, and put those decimal numbers together

from typing import List


class Solution:
    # If no zeros (no exception cases) and no decimal, then just loop through each comma position, and return a list

    def ambiguousCoordinates(self, s: str) -> List[str]:
        num_str = s[1:-1]  # string only contains the number
        n = len(num_str)

        final_list = []

        def insert_decimal(num):
            num_arr = []
            if len(num) == 1 or num[0] != '0':
                num_arr.append(num)
            for i in range(1, len(num)):
                left = num[:i]
                right = num[i:]
                if left[0] == '0' and len(left) > 1:
                    break
                if right[-1] == '0':
                    break
                num_arr.append(left + "." + right)
            return num_arr

        for comma_position in range(1, n):

            left_num = num_str[:comma_position]
            right_num = num_str[comma_position:]
            # print(left_num)
            left_possible = insert_decimal(left_num)
            right_possible = insert_decimal(right_num)

            for left in left_possible:
                for right in right_possible:
                    coord = "(" + left + ", " + right + ")"
                    final_list.append(coord)
        return final_list


sol_obj = Solution()
print(sol_obj.ambiguousCoordinates("(0123)"))
