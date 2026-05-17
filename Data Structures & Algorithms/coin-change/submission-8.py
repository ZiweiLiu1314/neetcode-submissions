class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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