class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_map = defaultdict(int)

        for i, num in enumerate(nums):
            if num in nums_map and i - nums_map[num] <= k:
                return True

            nums_map[num] = i

        return False
