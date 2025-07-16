class Solution:
    def reverse(self, x: int) -> int:
        if 0 <= x < 10:
            return x
        s = str(abs(x))
        res = s[::-1]
        if x < 0:
            if int(res) > 2**31:
                return 0
            return -int(res)
        else:
            if int(res) > 2**31 - 1:
                return 0
            return int(res)