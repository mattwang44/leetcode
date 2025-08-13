class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        candidates = ["()"]
        if n == 1:
            return candidates

        for i in range(1, n):
            seen = set()
            for cand in candidates:
                for i in range(len(cand)):
                    new_str = cand[:i] + "()" + cand[i:]
                    if new_str not in seen:
                        seen.add(new_str)
            candidates = list(seen)
        return candidates
