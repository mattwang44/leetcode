class Solution:
    # time O(N), space O(k)
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s) == 0 or k == 0:
            return 0

        start_idx = 0
        max_length = 0
        counter = defaultdict(int)
        for end_idx, char in enumerate(s):
            counter[char] += 1
            if len(counter) > k:
                rm_char = s[start_idx]
                counter[rm_char] -= 1
                if counter[rm_char] == 0:
                    del counter[rm_char]

                start_idx += 1

            max_length = max(max_length, end_idx - start_idx + 1)
        return max_length
