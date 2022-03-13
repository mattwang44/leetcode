class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []

        def helper(s, curr=[]):
            if len(curr) == 4:
                if s == '':
                    ret.append('.'.join(curr))
                return

            acc = ''
            for idx, char in enumerate(s):
                acc += char
                if acc == '0':
                    helper(s[idx+1:], curr+[acc])
                    break
                elif 0 <= int(acc) <= 255:
                    helper(s[idx+1:], curr+[acc])
                else:
                    break

        helper(s)
        return ret
