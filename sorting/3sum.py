class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            while l < r:
                cur = nums[l] + nums[r]
                if cur == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif cur > target:
                    r -= 1
                else:
                    l += 1

        return result
