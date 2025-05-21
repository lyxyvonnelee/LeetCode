class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * 5
        dp[1], dp[3] = -prices[0], -prices[0]

        for i in range(len(prices)):
            dp[1] = max(dp[1], dp[0]-prices[i])
            dp[2] = max(dp[2], dp[1]+prices[i])
            dp[3] = max(dp[3], dp[2]-prices[i])
            dp[4] = max(dp[4], dp[3]+prices[i])

        return dp[4]

