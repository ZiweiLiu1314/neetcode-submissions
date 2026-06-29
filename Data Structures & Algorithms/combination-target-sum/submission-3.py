class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums (distinct, but can be used repeatitively), list; target, int 
        # DP, sub-problem: target - num 
        # O(2^(t/m)) time, where t is the target and m is minimum value in nums. 
        nums.sort()
        res = []
        def dfs(target, arr, start): 
            for i in range(start, len(nums)):
                # target = target - nums[i]
                # print(f"target = {target}, arr = {arr}")
                if target - nums[i] < 0:
                    break # break / continue, not return 
                if target - nums[i] == 0:
                    res.append(arr + [nums[i]]) # no in-place mutation 
                    continue 
                else: # target > 0
                    dfs(target - nums[i], arr + [nums[i]], i)
                
        dfs(target, [], 0)
        return res 
