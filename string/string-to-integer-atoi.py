class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0: return 0
        
        MAX = 2**31 - 1
        MIN = -2**31
        
        index = 0
        if s[0] in ['-','+']:
            index = 1
        sign = -1 if s[0]=='-' else 1
        res = 0
        
        while index<len(s) and s[index].isdigit():
            cur = ord(s[index]) - ord('0')
            if res > MAX//10:
                return MAX if sign==1 else MIN
            res = res*10 + cur
            index += 1
            
        if sign == 1:
            return min(res, MAX)
        else:
            return max(-res, MIN)
        