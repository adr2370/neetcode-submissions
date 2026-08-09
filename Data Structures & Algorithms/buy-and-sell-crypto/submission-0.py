class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxSoFar = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            profit = max(profit, maxSoFar - prices[i])
            maxSoFar = max(maxSoFar, prices[i])
        return profit