# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDiff = float("inf")
        self.prev = None

        def inOrder(node):
            if not node:
                return

            inOrder(node.left)

            if self.prev is not None:
                self.minDiff = min(self.minDiff, abs(node.val - self.prev))
            self.prev = node.val

            inOrder(node.right)
            return

        inOrder(root)
        return self.minDiff
