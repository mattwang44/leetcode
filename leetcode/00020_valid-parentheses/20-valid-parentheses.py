class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        for bracket in s:
            if bracket in mapping:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if mapping[stack[-1]] != bracket:
                    return False
                stack.pop()
        return stack == []
