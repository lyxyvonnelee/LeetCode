class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        result = []

        for i in range(n):
            if i + 1 not in counts.keys():
                result.append(i + 1)

        return result
