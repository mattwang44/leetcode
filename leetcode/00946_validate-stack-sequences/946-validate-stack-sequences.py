class Solution:
    # time O(N), space O(N)
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        idx = 0
        stack = []
        for e in pushed:
            if e == popped[idx]:
                idx += 1
            else:
                stack.append(e)

            while stack and stack[-1] == popped[idx]:
                idx += 1
                stack.pop()

        return len(stack) == 0 and idx == len(popped)
