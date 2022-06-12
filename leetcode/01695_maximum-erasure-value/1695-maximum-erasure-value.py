class Solution:
    # time O(n), space O(n)
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)

        memo = {}
        curr = 0
        _max = 0
        start_idx = 0
        for idx, num in enumerate(nums):
            if num not in memo or memo[num] == -1:
                memo[num] = idx
                curr += num
                _max = max(_max, curr)
            else:
                for i in range(start_idx, memo[num]):
                    curr -= nums[i]
                    memo[nums[i]] = -1

                start_idx = memo[num] + 1
                memo[num] = idx
        return _max
