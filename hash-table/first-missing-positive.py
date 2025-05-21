class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Swap numbers to their correct positions
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Check for the first missing positive number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
