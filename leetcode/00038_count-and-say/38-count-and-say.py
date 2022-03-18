class Solution:
    def countAndSay(self, n: int) -> str:
        ret = "1"

        while n - 1 > 0:
            curr = None
            count = 0
            temp = ""
            for char in ret:
                if curr == None:
                    curr = char
                    count = 1
                elif char == curr:
                    count += 1
                else:
                    temp += f"{count}{curr}"
                    curr = char
                    count = 1

            temp += f"{count}{char}"
            ret = temp

            n -= 1
        return ret
