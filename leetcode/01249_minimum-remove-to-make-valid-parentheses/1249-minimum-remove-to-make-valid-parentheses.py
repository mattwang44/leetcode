class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rm_idx = []

        l = r = 0
        for idx, char in enumerate(s):
            if char not in ["(", ")"]:
                continue
            if char == "(":
                l += 1
            elif l > 0:
                l -= 1
            else:
                rm_idx.append(idx)

        l = r = 0
        for idx, char in enumerate(s[::-1]):
            if char not in ["(", ")"]:
                continue
            if char == ")":
                r += 1
            elif r > 0:
                r -= 1
            else:
                rm_idx.append(len(s) - idx - 1)

        return "".join([char for idx, char in enumerate(s) if idx not in rm_idx])
