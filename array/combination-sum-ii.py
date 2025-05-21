class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(st, path, remain):
            if remain == 0:
                result.append(path[:])
                return
            
            elif remain < 0:
                return
            
            for i in range(st, len(candidates)):
                if i > st and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, path, remain-candidates[i])
                path.pop()

        candidates.sort()
        backtrack(0, [], target)
        return result