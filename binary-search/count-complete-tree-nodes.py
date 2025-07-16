# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getDepth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        left = getDepth(root.left)
        right = getDepth(root.right)

        if left == right:
            return (1 << left) + self.countNodes(root.right)
        else:
            return (1 << right) + self.countNodes(root.left)
