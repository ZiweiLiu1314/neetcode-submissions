class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        while n:
            res += n % 2 
            n = n >> 1 
            # print(f"res {res}")
            # print(f"n {n}")
        return res 