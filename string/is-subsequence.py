class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        ps, pt = 0, 0
        while pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
                if ps == len(s):
                    return True
            pt += 1
        return False
