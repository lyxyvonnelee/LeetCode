class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [n**2 for n in nums]
        
        result = [0] * len(nums)
        l, r = 0, len(nums)-1
        pos = r
        while l <= r:
            ls, rs = nums[l] ** 2, nums[r] ** 2
            if rs >= ls:
                result[pos] = rs
                r -= 1
            else:
                result[pos] = ls
                l += 1
            pos -= 1

        return result


        