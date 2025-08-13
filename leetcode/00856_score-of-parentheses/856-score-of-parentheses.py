class Solution:
    # time O(N), space O(N)
    def scoreOfParentheses(self, s: str) -> int:
        return eval(s.replace(")(", ")+(").replace("()", "1").replace("(", "2*("))

    # time o(N), space O(1)
    def scoreOfParentheses(self, s: str) -> int:
        power = acc = 0
        for idx, char in enumerate(s):
            if char == "(":
                power += 1
            else:
                power -= 1
                if s[idx - 1] == "(":
                    acc += 2**power
        return acc
