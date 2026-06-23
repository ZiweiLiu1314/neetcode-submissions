class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices of a NeetCoin over the days 
        # brute force: check every combination, O(n^2) 
        res = 0 
        # idea: sell at the highest point, and buy at the lowest point 
        # left pointer starts at 0, and right starts at 1 
        # if value at right > left: calculate the price and compare 
        # else: we found a new low value, update left 
        l, r = 0, 1 
        maxP = 0 
        profit = 0
        while r < len(prices): 
            # profitable? 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
            else: 
                l = r 
            maxP = max(maxP, profit)
            r += 1 
                


        return maxP