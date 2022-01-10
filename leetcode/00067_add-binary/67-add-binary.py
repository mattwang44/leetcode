class Solution:
    # time O(N), space O(N)
    def add3Chars(self, c1, c2, c3):
        num_ones = [c1, c2, c3].count('1')
        carry = '0'
        digit = '0'
        if num_ones == 3:
            carry = digit = '1'
        elif num_ones == 2:
            carry = '1'
        elif num_ones == 1:
            digit = '1'
        return (carry, digit)

    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        b = b.zfill(len(a))

        ret = ''
        carry = '0'
        for char_a, char_b in zip(a[::-1], b[::-1]):
            carry, digit = self.add3Chars(char_a, char_b, carry)
            ret = digit + ret
        if carry == '1':
            ret = '1' + ret
        return ret
