class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        s = s.split(' ')[0]

        memo = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }

        is_neg = None
        n = 0
        for char in s:
            if char in ['+', '-']:
                if is_neg is not None:
                    break
                if char == '-':
                    is_neg = True
                else:
                    is_neg = False
                continue

            if char.isdigit():
                is_neg = is_neg if is_neg is not None else False
                n = n * 10 + memo[char]
                continue

            break

        n = -n if is_neg else n
        n = min(n, 2 ** 31 - 1)
        n = max(n, -2 ** 31)
        return n
