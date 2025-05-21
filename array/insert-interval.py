class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            i += 1

        start, end = newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            intervals.pop(i)
            n -= 1

        intervals.insert(i, [start, end])
        return intervals
