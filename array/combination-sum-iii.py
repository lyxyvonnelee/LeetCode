class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtracking(st, path, remaining):
            if len(path) == k and remaining == 0:
                result.append(path[:])
                return

            elif len(path) == k or remaining < 0:
                return
            
            for i in range(st, 10):
                path.append(i)
                backtracking(i+1, path, remaining-i)
                path.pop()

        backtracking(1, [], n)
        return result