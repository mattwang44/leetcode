class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        ret = d[digits[0]]
        if len(digits) == 1:
            return ret
        for digit in digits[1:]:
            ret = [r + char for r in ret for char in d[digit]]
        return ret
