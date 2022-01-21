# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # time O(N)
    # space O(N) for stack, try make it O(1) next time
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        head.val, head.next.val = head.next.val, head.val
        head.next.next = self.swapPairs(head.next.next)

        return head
