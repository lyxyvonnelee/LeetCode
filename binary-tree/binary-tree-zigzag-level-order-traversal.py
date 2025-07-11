# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = deque([root])
        order = 1
        while queue:
            level = []
            length = len(queue)
            for i in range(length):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            if order == 1:
                res.append(level)
            else:
                res.append(level[::-1])

            order *= -1

        return res

