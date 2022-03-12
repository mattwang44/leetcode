# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # time O(N), space O(1)
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # count #nodes
        num_nodes = 0
        curr = head
        while curr:
            num_nodes += 1
            curr = curr.next

        # decrease k if it's larger than #nodes
        k = k % num_nodes

        if k == 0:
            return head

        # find the pivot nodes
        l, r = head, head
        offset = 0
        while offset < k:
            r = r.next
            offset += 1

        while r.next:
            r = r.next
            l = l.next

        # break at pivot point and concat them with altered sequence
        r.next, head, l.next = head, l.next, None
        return head
