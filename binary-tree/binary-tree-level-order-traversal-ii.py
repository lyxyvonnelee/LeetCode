# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        que = [root]
        while que:
            length = len(que)
            level = []
            for _ in range(length):
                cur = que.pop(0)
                level.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            result.append(level)
        result.reverse()
        return result
        