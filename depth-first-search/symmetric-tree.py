# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isSame(left, right):
            if (left and not right) or (right and not left):
                return False
            if left and right and left.val != right.val:
                return False
            if not left and not right:
                return True

            inner = isSame(left.right, right.left)
            outer = isSame(left.left, right.right)
            return inner and outer

        return isSame(root.left, root.right)
