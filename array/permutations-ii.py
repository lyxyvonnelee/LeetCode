class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.backtrack(nums, [False] * len(nums), [], result)
        return result
    
    def backtrack(self, nums, used, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            path.append(nums[i])
            used[i] = True
            self.backtrack(nums, used, path, res)
            path.pop()
            used[i] = False

