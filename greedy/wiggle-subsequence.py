class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        preDiff, curDiff, result = 0, 0, 1

        for i in range(len(nums)-1):
            curDiff = nums[i+1] - nums[i]
            if preDiff * curDiff <= 0 and curDiff != 0:
                preDiff = curDiff
                result += 1

        return result
        