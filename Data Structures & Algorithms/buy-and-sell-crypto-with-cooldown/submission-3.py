class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        for i in range(len(prices)):
            prev_buy, prev_sell = i-1, i-2
            buy[i] = prices[i] * -1
            
            if prev_sell >= 0:
                buy[i] += sell[prev_sell]
            if i == 0:
                sell[i] = 0
            else:
                sell[i] = prices[i] + max(buy[:prev_buy+1])
            p = max(max(sell[i], buy[i]), p)
        print(buy, sell)
        return p
