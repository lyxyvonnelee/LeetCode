class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        rec = defaultdict(int)
        res = 0
        for i in nums1:
            for j in nums2:
                rec[i+j] += 1

        for i in nums3:
            for j in nums4:
                res += rec.get(0-i-j, 0)
        return res