# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # Try Floyd's Tortoise and Hare next time
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        curr = head
        while curr is not None:
            if curr in seen:
                return curr
            seen.add(curr)
            curr = curr.next
        return None
