class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_cnt = sys.maxsize
        dp = [0] + [max_cnt] * amount

        for i in range(1, amount + 1):
            for coin in coins:
                if (i - coin) < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[-1] == max_cnt else dp[-1]
