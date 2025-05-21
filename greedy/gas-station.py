class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_gas = -1
        total_gas = 0
        index = -1

        for i in range(len(gas)):
            if cur_gas < 0:
                index = i
                cur_gas = 0

            cur_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]
            # print(i, cur_gas, total_gas, index)

        return -1 if total_gas < 0 else index
