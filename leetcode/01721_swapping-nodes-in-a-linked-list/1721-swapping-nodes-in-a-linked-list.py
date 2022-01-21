# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # time O(N), space O(1)
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 1
        while count < k:
            curr = curr.next
            count += 1

        knode = curr

        prev = head
        curr = curr.next
        while curr:
            prev = prev.next
            curr = curr.next
        rknode = prev

        knode.val, rknode.val = rknode.val, knode.val
        return head
