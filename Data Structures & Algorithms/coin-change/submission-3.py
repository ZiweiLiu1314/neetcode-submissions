class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # a positive number that would never be exceeded 
        dp[0] = 0 
        for i in range(1, amount + 1): # i: the amount to make up to 
            for coin in coins: 
                if coin > i: 
                    continue 
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != (amount + 1) else -1 