class Solution:
    # time O(N), space O(1)
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        if k >= len(s):
            return len(s)

        counter = defaultdict(int)
        max_length = 1
        start_idx = 0
        for end_idx, char in enumerate(s):
            counter[char] += 1
            max_length = max(max_length, counter[char])

            if end_idx - start_idx + 1 > max_length + k:
                counter[s[start_idx]] -= 1
                start_idx += 1

        return end_idx - start_idx + 1
