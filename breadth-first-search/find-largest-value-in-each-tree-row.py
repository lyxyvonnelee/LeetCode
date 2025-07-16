# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        que = [root]
        while que:
            max_node = max(que,key=lambda x:x.val)
            result.append(max_node.val)
            length = len(que)
            for _ in range(length):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return result