class Solution:
    def countBits(self, n: int) -> List[int]:
        temp = [1]
        ret = [0]
        while len(ret) <= n:
            ret += temp
            temp = temp + [n + 1 for n in temp]
        return ret[: n + 1]
