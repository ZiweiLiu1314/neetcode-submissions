class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # unique combinations of nums that sums to target, reusing elements is allows 
        # backtracking, add elements together in uniques ways until they either reach or 
        # exceed the target, 
        # [2], 5, 6, 9 
        # [2, 2], [[2, 5]], [2, 6], x[2, 9]
        # x[2, 5, 5], x[2, 5, 6], x[2, 5, 9] (only add numbers on its right, avoid duplicates)
        # [2, 2, 2], [2, 2, 5], x[2, 2, 6]
        res = []
        n = len(nums)
        nums.sort()
        def dfs(target, arr, start_idx): # arr: elements already there
            nonlocal res 
            # target = target - nums[i]
            for i in range(start_idx, n):
                if target - nums[i] == 0: 
                    res.append(arr + [nums[i]])
                    break 
                    # continue # target = 4, found 4, but we also have element 2, in which case we want 
                    # to continue searching 
                if target - nums[i] < 0: 
                    break # continue 
                if target - nums[i] > 0: # continue searching 
                    dfs(target - nums[i], arr + [nums[i]], i)
        dfs(target, [], 0)
        return res 