class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        digit = 0
        ret = 0
        BASE = ord('A')
        for char in columnTitle:
            ret *= 26
            ret += ord(char) - BASE + 1
        return ret
