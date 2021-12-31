class Solution:
    def getDigits(self, number: int) -> List[int]:
        ret = []
        while number:
            ret.append(number % 10)
            number //= 10
        return ret

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        for number in range(left, right + 1):
            digits = self.getDigits(number)
            if 0 in digits:
                continue

            ok = True
            for digit in digits:
                if not (number % digit == 0):
                    ok = False
                    break
            if ok:
                ret.append(number)
        return ret
