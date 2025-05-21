class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backtrack(s, 0, [], result)
        return result
    
    def backtrack(self, s, st, path, res):
        if len(path) == 4:
            if st == len(s):
                res.append('.'.join(path))
            return
        
        if len(path) > 4:
            return
        
        for i in range(1, 4):
            if st + i > len(s):
                break
            if self.isValid(s[st:st+i]):
                path.append(s[st:st+i])
                self.backtrack(s, st+i, path, res)
                path.pop()

    def isValid(self, s):
        return len(s) == 1 or (s[0] != '0' and int(s) < 256)   
     