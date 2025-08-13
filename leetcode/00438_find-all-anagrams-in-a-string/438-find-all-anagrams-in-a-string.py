from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        counter_p = Counter(p)

        ret = []
        for i in range(len_s - len_p + 1):
            if i == 0:
                counter_s = Counter(s[:len_p])
            else:
                char_add = s[i + len_p - 1]
                counter_s[char_add] += 1

                char_rm = s[i - 1]
                counter_s[char_rm] -= 1
                if counter_s[char_rm] == 0:
                    del counter_s[char_rm]

            if counter_p == counter_s:
                ret.append(i)

        return ret
