class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
