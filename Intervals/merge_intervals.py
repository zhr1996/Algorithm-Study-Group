from typing import List


class Solution:
    def mergeInterval(self, intervals: List[List[int]]) -> List[List[int]]:
        def has_overlap(interval1, interval2):
            if not(interval1[1] < interval2[0] or interval2[1] < interval1[0]):
                return True
            return False

        merged_intervals = []

        intervals.sort(key=lambda x: x[0])

        # print(intervals)
        for interval in intervals:
            if len(merged_intervals) == 0:
                merged_intervals.append(interval)
            else:
                if has_overlap(interval, merged_intervals[-1]):
                    old_interval = merged_intervals.pop()
                    new_interval = [old_interval[0], max(
                        old_interval[1], interval[1])]
                    #print("reached" + str(new_interval))
                    merged_intervals.append(new_interval)
                else:
                    merged_intervals.append(interval)
        return merged_intervals


if __name__ == "__main__":
    sol = Solution()
    intervalsRange = int(input())
    intervals = [[int(x) for x in input().split()]
                 for _ in range(intervalsRange)]
    result = sol.mergeInterval(intervals)
    for res in result:
        print(' '.join(str(num) for num in res))
