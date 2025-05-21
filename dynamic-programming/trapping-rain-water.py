class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right, result = 0, len(height)-1, 0
        max_left, max_right = 0, 0

        while left <= right:
            if max_left < max_right:
                max_left = max(max_left, height[left])
                result += max(0, max_left - height[left])
                left += 1
            else:
                max_right = max(max_right, height[right])
                result += max(0, max_right - height[right])
                right -= 1
        
        return result
