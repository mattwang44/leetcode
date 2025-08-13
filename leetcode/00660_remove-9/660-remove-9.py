class Solution:
    def newInteger(self, n: int) -> int:
        # 12 -> 9 + 3 -> 13
        # 98 -> 81 + 9 + 8 -> 118
        acc = 0
        digit = 0
        while n:
            remainder = n % 9
            n = n // 9
            acc = acc + remainder * (10**digit)
            digit += 1
        return acc
