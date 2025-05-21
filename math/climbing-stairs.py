class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        pre1, pre2 = 1, 2
        for i in range(3, n+1):
            cur = pre1 + pre2
            pre1, pre2 = pre2, cur

        return pre2