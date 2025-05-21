class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.backtrack(nums, 0, [], result)
        return result
    
    def backtrack(self, nums, st, path, res):
        res.append(path[:])

        for i in range(st, len(nums)):
            if i == st or nums[i] != nums[i-1]:
                path.append(nums[i])
                self.backtrack(nums, i+1, path, res)
                path.pop()
            

