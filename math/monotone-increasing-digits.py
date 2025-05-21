class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        strN = str(n)

        for i in range(len(strN)-1, 0, -1):
            if strN[i-1] > strN[i]:
                strN = strN[:i-1] + str(int(strN[i-1])-1) + '9'*(len(strN)-i)
        
        return int(strN)