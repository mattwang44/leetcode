class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        # target = (10**0 * 1 + 10**1 * 1 + ... + 10**n * 1)
        mod = 1 % k
        n = 0
        acc = 0
        while True:
            n += 1
            acc += mod
            mod = (mod * 10) % k

            if acc % k == 0:
                return n
