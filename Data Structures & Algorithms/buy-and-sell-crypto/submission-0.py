class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a, b = 0, 0
        best = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
            
                best = max(best, prices[j]-prices[i])
            
        
        return best