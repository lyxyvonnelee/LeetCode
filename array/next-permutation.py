class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i]>nums[i-1]:
                j = i
                while (j+1) <len(nums) and nums[j+1]>nums[i-1]:
                    j += 1
                nums[i-1], nums[j] = nums[j], nums[i-1]
                nums[i:] = sorted(nums[i:])
                return 
        nums.sort()   
        return