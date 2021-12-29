class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False

        for p in [16, 15, 12, 10, 9, 8, 6, 5, 4, 3, 2]:
            while n % p == 0:
                n //= p
        return n == 1