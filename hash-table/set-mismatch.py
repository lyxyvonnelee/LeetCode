class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = 0
        dup = 0
        flag = True

        for i in range(len(nums)):
            if nums[i] != i + 1 and flag:
                flag = False
                missing = i + 1
            if i != 0 and nums[i] == nums[i - 1]:
                dup = nums[i]

        return [dup, missing]
