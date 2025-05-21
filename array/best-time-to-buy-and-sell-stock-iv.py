class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0] * (2*k + 1)

        for i in range(1, 2*k, 2):
            dp[i] = -prices[0]

        for i in range(len(prices)):
            for j in range(1, 2*k+1):
                if j%2 == 1:
                    dp[j] = max(dp[j], dp[j-1] - prices[i])
                else:
                    dp[j] = max(dp[j], dp[j-1] + prices[i])

        return dp[2*k]

