class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            pre1, pre2 = nums[0], max(nums[0], nums[1])

            for i in range(2, len(nums)):
                cur = max(pre1+nums[i], pre2)
                pre1, pre2 = pre2, cur

            return pre2
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        case1 = helper(nums[:-1])
        case2 = helper(nums[1:])

        return max(case1, case2)