class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        q = []
        for char in s:
            if char == '(':
                q.append(char)
            elif q and q[-1] == '(':
                q.pop()
            else:
                q.append(char)
        return len(q)
