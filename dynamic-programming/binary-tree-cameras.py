# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = [0]
        if self.Traverse(root, res) == 0:
            res[0] += 1
        return res[0]


    def Traverse(self, root, res):
        if not root:
            return 2
        
        root.left = self.Traverse(root.left, res)
        root.right = self.Traverse(root.right, res)

        if root.left == 2 and root.right == 2:
            return 0
        
        elif root.left == 0 or root.right == 0:
            res[0] += 1
            return 1
        
        else:
            return 2


