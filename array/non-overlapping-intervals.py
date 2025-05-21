class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[0])
        res = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i-1][1]:
                res += 1
            else:
                intervals[i][1] = min(intervals[i][1], intervals[i-1][1])
        
        return len(intervals)-res