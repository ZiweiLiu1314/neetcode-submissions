class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        while n: 
            n = n & (n - 1) # a fast way to filter out the 1 and cancel out all the zeros 
            res += 1 
        return res 