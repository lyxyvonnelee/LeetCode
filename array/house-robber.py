class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        pre1, pre2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cur = max(pre1+nums[i], pre2)
            pre1, pre2 = pre2, cur

        return pre2 