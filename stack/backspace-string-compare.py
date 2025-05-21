class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def sanitizeStr(st: str) -> str:
            res = []
            for i in st:
                if i != '#':
                    res.append(i)
                elif res:
                    res.pop()
            return ''.join(res)
        
        return sanitizeStr(s) == sanitizeStr(t)

