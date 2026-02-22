class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        mapping = {}
        total = 0

        for n in sorted(counts.keys()):
            mapping[n] = total
            total += counts[n]

        return [mapping[n] for n in nums]
