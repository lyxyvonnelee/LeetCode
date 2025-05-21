class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        pre1, pre2 = 0, 1
        for i in range(2, n+1):
            cur = pre1 + pre2
            pre1, pre2 = pre2, cur

        return pre2