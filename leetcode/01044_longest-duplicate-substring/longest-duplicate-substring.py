from typing import Tuple


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ########## With Rabin-Karp ###########
        # Need to tune these two parameters in order to pass the test cases
        base = 26
        mod = 10000000000000

        def charcode(char: str) -> int:
            return ord(char) - ord('a')

        def _hash(string: str) -> int:
            h = 0
            for char in string:
                h = (h * base + charcode(char)) % mod
            return h

        def is_valid_length(length: int) -> Tuple[bool, str]:
            d = {}
            string_hash = _hash(s[:length - 1])
            first_digit_mod = base ** (length - 1) % mod
            for idx in range(len(s) - length + 1):
                string_hash = (string_hash * base +
                               charcode(s[idx + length - 1])) % mod

                if string_hash in d:
                    return True, s[idx:idx + length]
                d[string_hash] = idx

                string_hash = (string_hash - first_digit_mod *
                               charcode(s[idx])) % mod
            return False, None

        ########## Without Rabin-Karp ###########
        # def is_valid_length(length: int) -> Tuple[bool, str]:
        #     d = {}
        #     for idx in range(len(s) - length + 1):
        #         fragment = s[idx:idx + length]
        #         if fragment in d:
        #             return True, fragment
        #         d[fragment] = 1
        #     return False, None

        start = 1
        end = len(s) - 1
        ret = ""
        while start <= end:
            mid = start + (end - start) // 2
            is_valid, searched = is_valid_length(mid)
            if is_valid:
                start = mid + 1
                ret = searched
            else:
                end = mid - 1

        return ret
