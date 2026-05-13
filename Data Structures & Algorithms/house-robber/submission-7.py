class Solution:
    def rob(self, nums: List[int]) -> int:
        # recursion 1 
        # or, we can solve this using recursion 
        # the logic of which is similar, but we do it in a 
        # top-down fashion 
        # for each index, solve for two options: 
        # i + solve([:i-2])
        # solve[i-1]
        # O(2^n) without memoization 
        # but can be reduced to O(n) time with memorization 
        memo = {}
        def helper(i):
            if i < 0: 
                return 0 
            if i in memo:
                return memo[i]
            memo[i] = max(helper(i-2) + nums[i], helper(i-1))
            return memo[i]
        return helper(len(nums) - 1) # optimal 


