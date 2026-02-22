class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
