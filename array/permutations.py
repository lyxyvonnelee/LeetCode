class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, [], result)
        return result
    
    def backtrack(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for num in nums:
            if num not in path:
                path.append(num)
                self.backtrack(nums, path, res)
                path.pop()

        