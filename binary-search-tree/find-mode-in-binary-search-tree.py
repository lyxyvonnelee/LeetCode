# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        from collections import defaultdict

        def inorderTraverse(root):
            if not root:
                return 
            inorderTraverse(root.left)
            count[root.val] += 1
            inorderTraverse(root.right)

        count = defaultdict(int)
        inorderTraverse(root)
        max_freq = max(count.values())

        return [key for key, value in count.items() if value == max_freq]
