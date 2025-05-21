# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        part_head = ListNode(0)
        part = part_head
        dummy = ListNode(next=head)
        cur = head
        pre = dummy
        while cur:
            if cur.val >= x:
                while cur and cur.val >= x:
                    part.next = ListNode(cur.val)
                    part = part.next
                    cur = cur.next
                pre.next = cur
            else:
                cur = cur.next
                pre = pre.next

        pre.next = part_head.next
        return dummy.next
