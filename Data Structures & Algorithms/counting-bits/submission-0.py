class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        def count(num):
            res = 0 
            while num: 
                num = num & (num - 1)
                res += 1 
            return res 
        for i in range(n + 1):
            output[i] = count(i) 
        return output 