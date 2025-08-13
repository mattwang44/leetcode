class Solution:
    idx = 0

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "").replace("--", "+").replace("+-", "-")
        res = 0
        operand = 0
        sign = 1  # 1 -> '+', 0 -> '-'
        while self.idx < len(s):
            char = s[self.idx]
            if char == "(":
                self.idx += 1
                operand = self.calculate(s)
            elif char == ")":
                break
            elif char in ["+", "-"]:
                res += operand if sign else -1 * operand
                sign = 1 if char == "+" else 0
                operand = 0
            else:
                operand = 10 * operand + int(char)
            self.idx += 1
        output = res + (operand if sign else (-1 * operand))
        return output
