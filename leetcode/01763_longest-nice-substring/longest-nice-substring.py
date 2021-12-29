class Solution:
    def isValidNiceString(self, s: str) -> bool:
        d = collections.Counter(s)
        for char in s:
            if not char.lower() in d or not char.capitalize() in d:
                return False
        return True
            
        
    def longestNiceSubstring(self, s: str) -> str:
        length = len(s)
        curr_longest = ''
        for i in range(length):
            for j in range(i + 1, length + 1):
                if j - i <= len(curr_longest):
                    continue
                if self.isValidNiceString(s[i:j]):
                    curr_longest = s[i:j]
        return curr_longest
            
            