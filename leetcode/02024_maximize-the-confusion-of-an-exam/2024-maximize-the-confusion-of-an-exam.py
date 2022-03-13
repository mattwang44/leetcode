class Solution:
    # time O(N), space O(2)
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        memo = {'T': 0, 'F': 0}
        start_idx = 0
        max_length = 0
        for end_idx, ans in enumerate(answerKey):
            memo[ans] += 1
            while min(memo['T'], memo['F']) > k:
                memo[answerKey[start_idx]] -= 1
                start_idx += 1
            max_length = max(max_length, end_idx - start_idx + 1)
        return max_length
