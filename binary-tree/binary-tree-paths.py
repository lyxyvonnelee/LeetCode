# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return
        paths = []
        self.dfs(root, [], paths)
        return paths

    def dfs(self, node, path, paths):
        if not node:
            return
        path.append(str(node.val))

        if not node.left and not node.right:
            paths.append('->'.join(path))

        self.dfs(node.left, path, paths)
        self.dfs(node.right, path, paths)
        path.pop()