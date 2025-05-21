class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtracking(st, path):
            if len(path) == k:
                result.append(path[:])
                return
            
            for i in range(st, n+1):
                path.append(i)
                backtracking(i+1, path)
                path.pop()

        backtracking(1, [])
        return result