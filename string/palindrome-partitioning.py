class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtrack(s, 0, [], result)
        return result

    def backtrack(self, s, st, path, res):
        if st == len(s):
            res.append(path[:])
            return
        
        for i in range(st, len(s)):
            if self.isPalindrome(s, st, i):
                path.append(s[st:i+1])
                self.backtrack(s, i+1, path, res)
                path.pop()
    
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True