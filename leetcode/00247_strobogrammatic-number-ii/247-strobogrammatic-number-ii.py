class Solution:
    concat_choices = [
        ('0', '0'),
        ('1', '1'),
        ('6', '9'),
        ('8', '8'),
        ('9', '6'),
    ]

    def findStrobogrammatic(self, n: int) -> List[str]:
        temp1 = ['0', '1', '8']
        if n == 1:
            return temp1

        temp2 = ['00', '11', '69', '88', '96']

        while n > 2:
            temp1, temp2 = temp2, [
                f"{pre}{e}{post}"
                for pre, post in self.concat_choices
                for e in temp1
            ]
            n -= 1

        return [e for e in temp2 if not e.startswith('0')]
