class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Find the first element larger or equal to x, then search in each side

        boundary = -1

        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] >= x:
                boundary = mid
                high = mid - 1
            else:
                low = mid + 1
        closest_num = []
        # x is smaller than all of the elements
        if boundary == -1:
            for i in range(1, k + 1):
                closest_num.append(arr[-i])
            return sorted(closest_num)

        left = boundary - 1
        right = boundary
        print(boundary)
        while k > 0:
            if left < 0:
                closest_num.append(arr[right])
                right += 1
            elif right >= len(arr):
                closest_num.append(arr[left])
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    closest_num.append(arr[left])
                    left -= 1
                else:
                    closest_num.append(arr[right])
                    right += 1
            k -= 1

        return sorted(closest_num)
