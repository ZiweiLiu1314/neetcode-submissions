class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force: for every number in nums, traverse the array to find if there's (target - number)
        # O(n^2) time, no extra space 
        # optimized: using a hash map counter, for every number in nums, try to find (target - number)
        # O(n) time, O(n) space 
        val2idx = {}
        for i in range(len(nums)): 
            val2idx[nums[i]] = i 
        for idx_i in range(len(nums)): 
            supp = target - nums[idx_i]
            if supp in val2idx: 
                idx_j = val2idx[supp]
                if idx_j != idx_i:
                    return [idx_i, idx_j]