class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums (distinct, but can be used repeatitively), list; target, int 
        # brute force: for each of the num, add with the elements on its right until target is found 
        # O(n!), factorial time 
        # DP, sub-problem: target - num 
        res = []
        def rec(target, arr, start): 
            for i in range(start, len(nums)):
                # target = target - nums[i]
                # print(f"target = {target}, arr = {arr}")
                if target - nums[i] < 0:
                    continue # continue, not return 
                if target - nums[i] == 0:
                    res.append(arr + [nums[i]]) # no in-place mutation 
                else: # target > 0
                    rec(target - nums[i], arr + [nums[i]], i)
                
        rec(target, [], 0)
        return res 
