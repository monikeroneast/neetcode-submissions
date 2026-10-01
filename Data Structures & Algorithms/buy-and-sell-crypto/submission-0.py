class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Two Pointer approach
        left = 0
        right = 1
        maxP = 0
        while right < len(prices):
            if prices[left] < prices[right]: # buying price is less than the selling price
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else: # sell price is smaller than the buy price
                left = right
            right = right + 1
        
        return maxP