# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev, curr = None, head
        while curr:
            curr.next, curr, prev = prev, curr.next, curr

        return prev

    # time O(N)
    # space O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        # reverse both lists
        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)

        # add l2 to l1
        carry = 0
        head1, head2 = l1, l2
        while head1 or head2:
            head1.val += carry
            if head2:
                head1.val += head2.val
            carry = head1.val // 10
            head1.val %= 10

            if not head1.next and head2:
                head1.next, head2.next = head2.next, head1.next

            head1 = head1.next
            head2 = head2.next if head2 else head2

        # reverse back
        ret = self.reverse_list(l1)

        # handle last carry
        if carry:
            head = ListNode(val=carry)
            head.next = ret
            return head

        return ret
