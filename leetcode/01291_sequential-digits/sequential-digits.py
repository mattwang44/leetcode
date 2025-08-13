class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ret = []
        num_digits = len(str(low))

        def l2n(l):
            return int("".join(str(n) for n in l))

        while num_digits <= len(str(high)):
            for i in range(1, 10 - num_digits + 1):
                curr = list(range(i, num_digits + i))
                n = l2n(curr)
                if low <= n <= high:
                    ret.append(n)
            num_digits += 1

        return ret
