class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 
        for i in range(32):
            bit = (n >> i) & 1 # find the bit at i-th position 
            res = res | (bit << (31 - i)) 
        return res 