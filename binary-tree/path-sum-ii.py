# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        path = []
        
        if not root:
            return []
        self.Traverse(root, targetSum-root.val,path,res)
        
        return res
        
    def Traverse(self,root,targetSum,path,res):
            path.append(root.val)
            if not root.left and not root.right and targetSum == 0:
                res.append(path[:])
                return True
            if not root.left and not root.right:
                return False
            if root.left:
                targetSum -= root.left.val
                self.Traverse(root.left, targetSum,path,res)
                targetSum += root.left.val
                path.pop()
            if root.right:
                targetSum -= root.right.val
                self.Traverse(root.right, targetSum,path,res)
                targetSum += root.right.val
                path.pop()
                    