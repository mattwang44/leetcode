class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_lowest_price = sys.maxsize
        max_profit = -sys.maxsize

        for price in prices:
            max_profit = max(price - curr_lowest_price, max_profit)
            curr_lowest_price = min(curr_lowest_price, price)

        return max(0, max_profit)
