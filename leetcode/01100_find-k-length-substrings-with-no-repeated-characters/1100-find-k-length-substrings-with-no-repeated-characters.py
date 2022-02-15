from collections import Counter


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        length = len(s)
        if length < k:
            return 0

        count = 0
        skips = 0
        for i in range(length - k + 1):
            if i == 0:
                curr = Counter(s[:k])
            else:
                # handle char to be removed
                char_rm = s[i-1]
                curr[char_rm] -= 1
                if curr[char_rm] == 0:
                    del curr[char_rm]

                # handle char to be added
                char_add = s[i+k-1]
                curr[char_add] += 1

                # decrease skip count in each iteration
                skips = max(skips - 1, 0)

            if all([v == 1 for v in curr.values()]):
                count += 1
        return count
