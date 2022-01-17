class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        _s = s.split(' ')
        if len(_s) != len(pattern):
            return False

        memo = {}
        for p, e in zip(pattern, _s):
            if p in memo and e != memo[p]:
                return False
            memo[p] = e
        return len(memo) == len(set(memo.values()))
