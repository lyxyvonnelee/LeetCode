class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p, n = 0, len(s)
        while p < n:
            p2 = p + k
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p += 2 * k
        return s