class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)
        while left<right:
            middle = (left+right)//2
            if target < nums[middle]:
                right = middle
            elif target > nums[middle]:
                left = middle+1
            else:
                return middle

        return -1