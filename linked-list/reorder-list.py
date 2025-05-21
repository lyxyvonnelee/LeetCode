# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """ 
        if not head or not head.next:
            return head

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pre, cur = None, slow
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        first, second = head, pre
        while second.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2   
        