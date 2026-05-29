class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # finding missing number in nums 
        # brute force 
        summation = 0 
        n = len(nums)
        for i in range(n + 1): 
            # sum([0, 1, ..., n]) 
            summation += i 
        for j in nums: 
            summation -= j 
        return summation 