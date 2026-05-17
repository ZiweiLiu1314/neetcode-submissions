class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # find smallest number of coin in coins, to make up the amount 
        # smallest # of coins needed to make up an amount = 
        # 1 + smallest # of coins needed to make up (amount - coin), coin in coins 
        # bottom-up, with a dp table 
        # for a in range(1, amount)
        # dp[a] = min(dp[a], dp[a - c] (for c in coins)
        # dp[a]: initialized into a impossible value, so that we'd know when it didn't find a 
        # possible combination of coins 
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 
        for a in range(1, amount + 1): 
            for c in coins: 
                if a >= c:
                    dp[a] = min(dp[a], dp[a - c] + 1) 
        
        return dp[amount] if dp[amount] != amount + 1 else -1 