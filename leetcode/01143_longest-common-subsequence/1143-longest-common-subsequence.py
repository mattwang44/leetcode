class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1, length2 = len(text1), len(text2)
        dp = [[0] * length2 for _ in range(length1)]
        if text1[0] == text2[0]:
            dp[0][0] = 1
        for i in range(1, length1):
            dp[i][0] = 1 if text1[i] == text2[0] else dp[i - 1][0]
        for j in range(1, length2):
            dp[0][j] = 1 if text1[0] == text2[j] else dp[0][j - 1]

        for i in range(1, length1):
            for j in range(1, length2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]
