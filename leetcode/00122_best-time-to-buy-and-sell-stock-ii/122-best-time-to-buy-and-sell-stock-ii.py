class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # STATE MACHINE
        buy, sell = -prices[0], 0

        for p in prices[1:]:
            buy = max(buy, sell - p)
            sell = max(sell, buy + p)
        return sell
