class Solution:
    def countDigitOne(self, n: int) -> int:
        ret = 0

        digit = 1
        while n >= 10 ** (digit - 1):
            temp = n
            interval = 10**digit
            skip = 10 ** (digit - 1) - 1

            temp -= skip
            ret += (temp // interval) * 10 ** (digit - 1)
            if temp % interval:
                ret += min(temp % interval, interval // 10)

            digit += 1

        return ret
