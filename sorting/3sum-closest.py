class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                sum_ = nums[i]+nums[l]+nums[r]

                if (sum_ - target) == 0:
                    return sum_
                
                if abs(sum_ - target)<abs(res-target):
                    res = sum_
                    
                if sum_ <target:
                    l += 1
                else:
                    r -= 1
                    
        return res