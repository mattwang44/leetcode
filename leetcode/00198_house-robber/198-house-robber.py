class Solution:
    # DYNAMIC PROGRAMING
    def rob(self, nums: List[int]) -> int:
        # rob(i) = max(rob(i-2)+houst[i], rob(i-1))
        n = len(nums)
        if n <= 2:
            return max(nums)

        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]

    # STATE MACHINE
    def rob(self, nums: List[int]) -> int:
        s1, s2 = 0, 0
        for n in nums:
            s1, s2 = s2 + n, max(s2, s1)
        return max(s1, s2)
