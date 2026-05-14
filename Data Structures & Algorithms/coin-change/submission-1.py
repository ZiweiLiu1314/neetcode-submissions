class Solution:
    def __init__(self):
        self.memo = []

    def coinChange(self, coins: List[int], amount: int) -> int:
        # solve sub-problem: after deducting a coin 
        # dynamic programming 
        # state transition: solve for amount -> solve for amount - coin 
        self.memo = [-100] * (amount + 1)
        return self.dp(amount, coins)

    def dp(self, amount, coins):
        if amount == 0: return 0 
        if amount < 0: return -1 
        if self.memo[amount] != -100: return self.memo[amount]
        res = float("inf")
        for c in coins: 
            subProblem = self.dp(amount - c, coins)
            if subProblem == -1: 
                continue 
            res = min(res, subProblem + 1)
        self.memo[amount] = res if res != float("inf") else -1 
        return self.memo[amount]