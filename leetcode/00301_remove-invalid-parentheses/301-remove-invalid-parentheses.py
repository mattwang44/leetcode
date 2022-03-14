from collections import deque, defaultdict


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            l = r = 0
            for char in s:
                if char not in ['(', ')']:
                    continue
                elif char == '(':
                    l += 1
                elif l > 0 and char == ')':
                    l -= 1
                else:
                    return False
            return l == 0

        # calculate number of parenthesis that need to be removed
        l = r = 0
        stack = []
        for char in s:
            if char not in ['(', ')']:
                continue
            if char == '(':
                l += 1
            elif l > 0:
                l -= 1
            else:
                r += 1

        # bfs
        ret = set()
        seen = set()
        stack = deque([(s, (l, r))])

        while stack:
            _s, (l_err, r_err) = stack.popleft()

            # check if the string has been processed before
            if _s in seen:
                continue
            seen.add(_s)

            # check if it's valid only when the error counts are exhausted
            if l_err == 0 and r_err == 0 and is_valid(_s):
                ret.add(_s)
                continue

            for idx, char in enumerate(_s):
                if char not in ['(', ')']:
                    continue

                # new string with the current character removed
                new_s = _s[:idx] + _s[idx+1:]

                if char == '(':
                    if l_err == 0:
                        continue
                    stack.append((new_s, (l_err - 1, r_err)))
                elif char == ')':
                    if r_err == 0:
                        continue
                    stack.append((new_s, (l_err, r_err - 1)))

        return list(ret)
