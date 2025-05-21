class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins = []
        for t in timePoints:
            h, m = map(int, t.split(":"))
            total = h * 60 + m
            mins.append(total)

        mins.sort()
        min_diff = float('inf')
        for i in range(1, len(mins)):
            min_diff = min(min_diff, mins[i]-mins[i-1])

        min_diff = min(min_diff, 1440-mins[-1]+mins[0])

        return min_diff