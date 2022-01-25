class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        rs = ''
        m = 0
        for i, c in enumerate(s):
            if c in rs:
                m = max(m, len(rs))
                rs = rs[rs.index(c)+1:]
            rs += c
        return max(m, len(rs))
