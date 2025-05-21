class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_length = 1

                while num + 1 in nums_set:
                    num += 1
                    cur_length += 1

                max_length = max(max_length, cur_length)

        return max_length
