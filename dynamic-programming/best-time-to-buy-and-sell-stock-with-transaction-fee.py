class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        minimum = prices[0]
        for i in range(len(prices)):
            tmp = prices[i]-minimum-fee
            minimum = min(minimum,prices[i])
            if tmp>0:
                profit+=tmp
                minimum = prices[i]-fee
        return profit