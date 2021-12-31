
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        if length == 0:
            return 0
        if length > len(haystack):
            return -1

        base = 26
        mod = 10 ** 4

        def charcode(char: str) -> int:
            return ord(char) - ord('a')

        def custom_hash(string: str) -> int:
            _hash = 0
            for char in string:
                _hash = (_hash * base + charcode(char)) % mod
            return _hash

        needle_hash = custom_hash(needle)
        first_digit_mod = base ** (length - 1)

        # the hash of first (length - 1) characters
        haystack_hash = custom_hash(haystack[:length - 1]) % mod

        for idx in range(len(haystack) - length + 1):
            # rolling hashing
            haystack_hash = (base * haystack_hash + charcode(haystack[idx + length - 1])) % mod

            if haystack_hash == needle_hash and haystack[idx:idx + length] == needle:
                return idx

            haystack_hash = (haystack_hash - charcode(haystack[idx]) * first_digit_mod) % mod

        return -1
