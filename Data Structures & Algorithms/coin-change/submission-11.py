class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # prob: finding smallest possible number of coins needed to make up to amount 
        # optimal sub-structure: coinChange(amount - coin) + 1, coin in coins 
        # 0 -> 0 
        # negative -> -1 
        memo = {}
        memo[0] = 0
        def dfs(amount):
            if amount < 0:
                return -1
            elif amount in memo: 
                return memo[amount]
            else: 
                res = float('inf')
                for coin in coins: 
                    subProb = dfs(amount - coin)
                    if subProb != -1: 
                        res = min(res, subProb + 1)
                memo[amount] = res if res != float('inf') else -1 
                return memo[amount] 
        return dfs(amount)
