# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            
        return res

