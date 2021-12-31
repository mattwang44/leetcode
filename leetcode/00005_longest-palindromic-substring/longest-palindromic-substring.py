# time O(N^2), space O(1)
class Solution:
    def expand(self, string, start, end):
        # default value
        ret = string[start]
        while string[start] == string[end]:
            ret = string[start: end + 1]
            if start - 1 < 0 or end + 1 > len(string) - 1:
                break
            start -= 1
            end += 1
        return ret

    def longestPalindrome(self, s: str) -> str:
        ret = ''
        for i in range(len(s)):
            string = self.expand(s, i, i)
            if len(string) > len(ret):
                ret = string

            if i + 1 == len(s):
                break

            string = self.expand(s, i, i + 1)
            if len(string) > len(ret):
                ret = string
        return ret
