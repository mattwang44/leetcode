class Solution:
    # time O(N*2^N), space O(N)
    def is_palindrome(self, s: str) -> bool:
        length = len(s)
        if length == 1:
            return True

        half_length = length // 2
        return s[:half_length] == s[-half_length:][::-1]

    def partition(self, s: str) -> List[List[str]]:
        ret = []

        def backtrack(s, current):
            nonlocal ret
            if len(s) == 0:
                ret.append(current.copy())
            else:
                for i in range(1, len(s)+1):
                    if not self.is_palindrome(s[:i]):
                        continue
                    current.append(s[:i])
                    backtrack(s[i:], current)
                    current.pop()

        backtrack(s, [])
        return ret
