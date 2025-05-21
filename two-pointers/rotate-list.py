# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        cur = head
        while cur.next:
            length += 1
            cur = cur.next
        cur.next = head

        k = k % length
        new_head = head
        for _ in range(length - k - 1):
            new_head = new_head.next

        tail = new_head
        new_head = new_head.next
        tail.next = None

        return new_head
