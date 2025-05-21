# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = None
        self.result = float('inf')

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.result
    
    def dfs(self, cur):
        if not cur:
            return
        
        left = self.dfs(cur.left)
        if self.pre:
            self.result = min(self.result, abs(cur.val-self.pre.val))
        self.pre = cur

        right = self.dfs(cur.right)
