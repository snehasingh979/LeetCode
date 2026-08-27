class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            # Minimum buying price update karo
            if prices[i] < min_price:
                min_price = prices[i]

            # Profit calculate karo
            profit = prices[i] - min_price

            # Maximum profit update karo
            if profit > max_profit:
                max_profit = profit

        return max_profit