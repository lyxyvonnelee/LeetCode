class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pre1, pre2 = cost[0], cost[1]

        for i in range(2, len(cost)):
            cur = min(pre1, pre2) + cost[i]
            pre1, pre2 = pre2, cur

        return min(pre1, pre2)