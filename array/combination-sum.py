class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtracking(st, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            elif remaining < 0:
                return
            
            for i in range(st, len(candidates)):
                path.append(candidates[i])
                backtracking(i, path, remaining-candidates[i])
                path.pop()

            return
        
        backtracking(0, [], target)
        return result