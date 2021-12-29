# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # time O(kN) & space O(N) for the returned linked list,
    # where k is the number of list and N is total number of nodes
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not any(lists):
            return None

        def find_indices_with_min_val(lists):
            indices = []
            min_val = sys.maxsize
            for index, node in enumerate(lists):
                if node.val < min_val:
                    min_val = node.val
                    indices = [index]
                elif node.val == min_val:
                    indices.append(index)
            return min_val, indices

        prev_head = curr = ListNode()
        while any(lists):
            lists = [l for l in lists if l]
            min_val, indices = find_indices_with_min_val(lists)

            for index in indices:
                curr.next = ListNode(val=min_val)
                curr = curr.next
                lists[index] = lists[index].next

        curr.next = None
        return prev_head.next
