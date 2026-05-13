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
        # don't use recursion if we can use DP 
        # bcs recursion introduces more cost, cost of using a function \
        """
        memo = {}
        def helper(i):
            if i < 0: 
                return 0 
            if i in memo:
                return memo[i]
            memo[i] = max(helper(i-2) + nums[i], helper(i-1))
            return memo[i]
        return helper(len(nums) - 1) # optimal 
        """
        # ***
        # calculate from 0 to nums 
        # same logic as DP, but 
        memo = {}
        def dfs(i):
            if i >= len(nums): # iterate until len(nums) - 1
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dfs(i +  1), nums[i] + dfs(i + 2))
            return memo[i]

        return dfs(0)
