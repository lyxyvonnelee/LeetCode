class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, missing = 0, 0

        for i in range(len(nums)):
            val = abs(nums[i])
            ins = val - 1
            if nums[ins] < 0:
                dup = val
            nums[ins] = -abs(nums[ins])

        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1

        return [dup, missing]
