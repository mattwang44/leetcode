class Solution:
    # time O(N), space O(N)
    # try optimize space to O(1) next time
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        memo = [0] * len(s)

        q = []
        for idx, p in enumerate(s):
            if not q or p == '(':
                q.append((idx, p))
            elif q and q[-1][1] == '(':
                pair_idx, _ = q.pop()
                memo[pair_idx] = memo[idx] = 1

        count = 0
        max_streak = 0
        for n in memo:
            if n == 1:
                count += 1
                max_streak = max(max_streak, count)
            else:
                count = 0
        return max_streak
