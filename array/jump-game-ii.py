class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        cur_end = 0
        count = 0

        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])

            if i == cur_end:
                cur_end = far
                count += 1

                if cur_end >= len(nums) - 1:
                    break
        return count
