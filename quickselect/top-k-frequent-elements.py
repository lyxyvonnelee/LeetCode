class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)

        h = []
        for num, freq in count.items():
            heapq.heappush(h, (freq,num))
            if len(h) > k:
                heapq.heappop(h)
        
        res = [num for freq, num in h]
        return res