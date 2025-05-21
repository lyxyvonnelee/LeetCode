class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, 0, [], result)
        return result
    
    def backtrack(self, nums, st, path, res):
        if len(path) > 1:
            res.append(path[:])

        used = set()
        for i in range(st, len(nums)):
            if nums[i] in used:
                continue
            if not path or nums[i] >= path[-1]:
                path.append(nums[i])
                used.add(nums[i])
                self.backtrack(nums, i+1, path, res)
                path.pop()