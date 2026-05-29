class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # finding missing number in nums 
        # approach 1 with formula 
        """
        summation = 0 
        n = len(nums)
        # for i in range(n + 1): 
            # sum([0, 1, ..., n]) 
            # summation += i 
        summation = int(n * (n + 1) / 2)
        for j in nums: 
            summation -= j 
        return summation 
        """
        # bit manipulation 
        # a ^ a = 0 (0000000)
        # a ^ b ^ a = a ^ a ^ b = b (0 ^ b = b)
        n = len(nums)
        mul = 0 
        for i in range(n + 1): 
            mul ^= i 
            print(f"after XOR {i}, mul is {mul}")
        for j in nums:
            mul ^= j 
        return mul 
