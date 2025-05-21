# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.getHeight(root) != -1

    def getHeight(self, node):
        if not node:
            return 0
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1  
        