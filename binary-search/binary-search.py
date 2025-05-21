class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        nums.sort()
        while left<right:
            middle = (left+right)//2
            if target > nums[middle]:
                left = middle+1
            elif target < nums[middle]:
                right = middle
            else:
                return middle
        return -1