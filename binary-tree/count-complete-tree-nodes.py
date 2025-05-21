# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        left, right = root.left, root.right
        count = 1
        while left and right:
            count += 1
            left = left.left
            right = right.right
        if not left and not right:
            return 2**count-1
        return self.countNodes(root.left) + self.countNodes(root.right)+1