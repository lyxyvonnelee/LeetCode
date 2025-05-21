# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.traverse(root)

        return max(dp)

    def traverse(self, root):
        if not root:
            return (0, 0)
        
        root.left = self.traverse(root.left)
        root.right = self.traverse(root.right)

        v1 = max(root.left) + max(root.right)
        v2 = root.left[0] + root.right[0] + root.val

        return (v1, v2)