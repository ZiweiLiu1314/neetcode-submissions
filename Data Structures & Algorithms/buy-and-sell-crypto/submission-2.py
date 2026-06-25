class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maximum profit, i.e. sell price - buy price 
        # profit = prices[day2] - prices[day1]
        # brute force: nested loop to check for day i, the profit of selling 
        # on day j (i < j < len(prices)), O(n^2)
        # optimized with sliding window: find day 1 and day 2 s.t. max profit
        if not prices:
            return 0 
        l, r = 0, 1
        maxP = 0 
        # if we find a higher value than l, we update the maxP if the profit is larger
        # if we find a lower value than l, then we update l 
        while r < len(prices):
            # profitable ? 
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l] 
                maxP = max(maxP, profit)
            else: 
                l = r 
            r += 1 
        return maxP