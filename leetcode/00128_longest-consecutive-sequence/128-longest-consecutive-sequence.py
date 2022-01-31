from collections import Counter


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_streak = 0
        for key, val in counter.items():
            if key - 1 in counter:
                continue

            streak = 1
            curr = key
            while curr + 1 in counter:
                curr += 1
                streak += 1
            max_streak = max(max_streak, streak)
        return max_streak
