# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def findSum(root, path):
            if not root:
                return 0

            path += str(root.val)

            if not root.left and not root.right:
                self.sum += int(path)
                return int(path)

            return findSum(root.left, path) + findSum(root.right, path)

        return findSum(root, "")
