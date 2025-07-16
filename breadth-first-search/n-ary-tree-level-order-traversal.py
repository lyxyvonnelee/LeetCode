"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        que = [root]
        while que:
            level = []
            length = len(que)
            for _ in range(length):
                cur = que.pop(0)
                level.append(cur.val)
                if cur.children:
                    que.extend(cur.children)
            result.append(level)
        return result