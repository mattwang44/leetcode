from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = defaultdict(list)

        for string in strs:
            memo[tuple(sorted(string))].append(string)

        return memo.values()
