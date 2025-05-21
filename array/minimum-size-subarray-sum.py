class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        n = len(nums)
        cur_sum = 0
        start = 0

        for end in range(n):
            cur_sum += nums[end]

            while cur_sum >= target:
                min_len = min(min_len, end - start + 1)
                cur_sum -= nums[start]
                start += 1

        return 0 if min_len == float("inf") else min_len

