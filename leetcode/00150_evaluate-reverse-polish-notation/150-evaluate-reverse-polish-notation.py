class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: y - x,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(y / x),
        }
        stack = []
        for token in tokens:
            if token in ops:
                val = ops[token](stack.pop(), stack.pop())
                stack.append(val)
            else:
                stack.append(int(token))
        return stack[0]
