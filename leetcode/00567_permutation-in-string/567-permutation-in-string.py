from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False

        target = Counter(s1)

        for i in range(l2 - l1 + 1):
            if i == 0:
                curr = Counter(s2[:l1])
            else:
                char_rm = s2[i - 1]
                curr[char_rm] -= 1
                if curr[char_rm] == 0:
                    del curr[char_rm]

                char_add = s2[i + l1 - 1]
                curr[char_add] += 1

            if target == curr:
                return True

        return False
