"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root
            
        queue = deque([root])

        while queue:
            length = len(queue)
            pre = Node()
            for i in range(length):
                cur = queue.popleft()
                pre.next = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                pre = cur

        return root
