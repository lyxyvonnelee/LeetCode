class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre_sum = defaultdict(int)
        cur_sum = 0
        pre_sum[0] = 1

        for num in nums:
            cur_sum += num
            count += pre_sum[cur_sum-k]
            pre_sum[cur_sum] += 1
            

        return count
            