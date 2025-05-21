class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        def clean_window(i):
            if window and window[0] == i-k:
                window.popleft()
            
            while window and nums[i] > nums[window[-1]]:
                window.pop()

        res = []
        window = deque()

        for i, num in enumerate(nums):
            clean_window(i)
            window.append(i)
            if i >= k-1:
                res.append(nums[window[0]])
        return res