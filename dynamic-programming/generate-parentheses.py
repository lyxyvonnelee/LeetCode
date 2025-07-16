class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(l, r, path):
            if len(path) == 2*n:
                res.append(path)
                return 0
            if r <= l < n:
                a = backtrack(l+1, r, path+'(')
                a = backtrack(l, r+1, path+')')
            elif l==n:
                a = backtrack(l, r+1, path+')')
            
        backtrack(1, 0, '(')
        return res