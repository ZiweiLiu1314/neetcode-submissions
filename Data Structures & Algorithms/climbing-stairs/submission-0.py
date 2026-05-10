class Solution:
    def climbStairs(self, n: int) -> int:
        # basically we want to find the number of distinct ways 
        # to reach the staircase n 
        # since we can climb either 1 or 2 steps at a time 
        # ways to reach n = ways to reach n - 1 + ways to reach n - 2 
        # Dynamic programming, O(n), O(n) 
        ways = [0] * (n + 1)
        if n == 0: 
            return 1 
        ways[0] = 1 
        if n == 1: 
            return 1 
        ways[1] = 1 
        for i in range(2, n + 1): 
            ways[i] = ways[i - 1] + ways[i - 2]
            print(f"at step {i}, there are {ways[i]} ways")
        return ways[n] 
        