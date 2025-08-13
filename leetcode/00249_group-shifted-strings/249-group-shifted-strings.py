from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        for string in strings:
            if len(string) == 1:
                memo[tuple()].append(string)
                continue

            keys = []
            for idx, char in enumerate(string[:-1]):
                diff = ord(string[idx + 1]) - ord(char)
                if diff < 0:
                    diff += 26
                keys.append(diff)

            memo[tuple(keys)].append(string)
        return list(memo.values())
