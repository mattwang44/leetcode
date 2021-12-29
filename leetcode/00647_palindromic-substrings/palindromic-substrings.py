class Solution:
    def expand_and_count_pal(self, s, l, r):
        length = len(s)
        count = 0
        while True:
            if not 0 <= l < length or \
              not 0 <= r < length or \
              s[l] != s[r]:
                break
                
            count += 1
            l -= 1
            r += 1
        return count

    def countSubstrings(self, s: str) -> int:
        count = 0
        for idx, char in enumerate(s):
            count += self.expand_and_count_pal(s, idx, idx)

            if idx == len(s) - 1:
                break
            
            count += self.expand_and_count_pal(s, idx, idx + 1)
            
        return count