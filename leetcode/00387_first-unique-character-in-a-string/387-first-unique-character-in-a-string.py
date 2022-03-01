class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for idx, char in enumerate(s):
            if counter[char] == 1:
                return idx
        return -1
