class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remain = [0] * 60
        count = 0

        for t in time:
            remainder = t % 60
            completion = (60-remainder) % 60
            count += remain[completion]
            remain[remainder] += 1

        return count

