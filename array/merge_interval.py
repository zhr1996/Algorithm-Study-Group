class Solution:
    # note here, case like this : [1,4], [2,3], so when updating end, should use the biggest end
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]

        result = []
        for index in range(1, len(intervals)):
            interval = intervals[index]
            # No overlap
            if end < interval[0]:
                result.append([start, end])
                start = interval[0]
                end = interval[1]

            else:
                end = max(end, interval[1])

        # Inser last one if any
        result.append([start, end])
        return result
