class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        first_interval = intervals[0]
        result = [first_interval]

        for i in range(1, len(intervals)):
            (left, right) = result[-1]
            cur = intervals[i]
            if cur[0] > right:
                result.append(cur)
            elif cur[1] > right:
                result[-1][1] = cur[1]

        return result
