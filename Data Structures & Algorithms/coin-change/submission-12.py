class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # optimal sub-structure, dp 
        # bottom-down 
        # for a in range 1 -> amount 
        # f[a] = min(f[a], f[a - c] + 1), c in coins, 
        # f[a] initialized into a impossibly large number
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a >= c: 
                    dp[a] = min(dp[a], dp[a - c] + 1)
        res = dp[amount]
        return res if res != amount + 1 else -1 