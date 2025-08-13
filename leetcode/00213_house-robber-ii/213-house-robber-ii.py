class Solution:
    def rob(self, nums: List[int]) -> int:
        # max(house[0:n-2], house[1:n-1])

        if len(nums) <= 3:
            return max(nums)

        def helper(nums):
            n = len(nums)
            if n <= 2:
                return max(nums)

            dp = [0] * n
            dp[0], dp[1] = nums[0], max(nums[1], nums[0])
            for i in range(2, n):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

            return dp[-1]

        return max(helper(nums[1:]), helper(nums[:-1]))
