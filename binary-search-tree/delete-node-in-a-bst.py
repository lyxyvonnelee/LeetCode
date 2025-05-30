# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        return root


        