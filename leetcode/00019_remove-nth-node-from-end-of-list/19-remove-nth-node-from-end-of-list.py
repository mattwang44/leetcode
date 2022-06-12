# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        ptr1 = head
        ptr2 = head
        i = 1
        while i < n:
            i += 1
            ptr2 = ptr2.next

        prev = None
        while ptr2.next:
            prev = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        if not prev:
            return head.next
        prev.next = prev.next.next

        return head
