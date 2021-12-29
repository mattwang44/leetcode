class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for idx, n in enumerate(nums):
            if n in memo:
                return [memo[n], idx]
            memo[target - n] = idx
        