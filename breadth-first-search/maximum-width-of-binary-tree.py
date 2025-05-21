# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        queue = deque([(root, 1)])

        while queue:
            level_length = len(queue)
            _, first_index = queue[0]

            for i in range(level_length):
                cur, ind = queue.popleft()
                if cur.left:
                    queue.append((cur.left, 2*ind))
                if cur.right:
                    queue.append((cur.right, 2*ind+1))
                if i == level_length-1:
                    last_index = ind
            
            max_width = max(max_width, last_index-first_index+1)

        return max_width