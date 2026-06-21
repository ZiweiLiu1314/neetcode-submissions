class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force: iterating over the array each time, multiplying all other elements 
        # optimized: multiply all and divide by the current element (given its not zero)
        # without division: prefix / suffix, prefix: 
        # multiplication of all elements before it / after it, both of which can be calculate in one traversal
        res = [1] * len(nums)
        pre_postfix = 1 
        for i in range(len(nums)):
            res[i] *= pre_postfix 
            pre_postfix *= nums[i]
        pre_postfix = 1 
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= pre_postfix 
            pre_postfix *= nums[i]
        return res 