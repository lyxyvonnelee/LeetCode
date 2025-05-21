class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(0, nums, [], result)
        return result
    
    def backtrack(self, st, nums, path, res):
        res.append(path[:])
        for i in range(st, len(nums)):
            path.append(nums[i])
            self.backtrack(i+1, nums, path, res)
            path.pop()

