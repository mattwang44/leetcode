# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # time O(N+M), space O(1)
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        if headA == headB:
            return headA

        a, b = headA, headB
        jump_count = 0
        while jump_count < 3:
            if a == b:
                return a

            if a.next:
                a = a.next
            else:
                a = headB
                jump_count += 1

            if b.next:
                b = b.next
            else:
                b = headA
                jump_count += 1

        return None
