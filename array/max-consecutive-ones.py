class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur, res = 0, 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            if nums[i] == 0 or i == len(nums) - 1:
                res = max(cur, res)
                cur = 0

        return res
