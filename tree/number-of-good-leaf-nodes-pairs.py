# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0

        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            left_dis = dfs(node.left)
            right_dis = dfs(node.right)

            for l in left_dis:
                for r in right_dis:
                    if l + r <= distance:
                        self.result += 1

            return [d+1 for d in left_dis + right_dis if d+1 <= distance]
        
        dfs(root)
        return self.result
        