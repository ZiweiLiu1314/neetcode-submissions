class Solution:
    def rob(self, nums: List[int]) -> int:
        leng = len(nums)
        def robNoLoop(seq): 
            if not seq:
                return 0 
            rob1, rob2 = 0, 0
            for i in range(len(seq)):
                print(i)
                temp = max(rob1 + seq[i], rob2)
                rob1 = rob2
                rob2 = temp
            return rob2 
        mx_beg = robNoLoop(nums[2:-1]) + nums[0]
        mx_end = robNoLoop(nums[1:])
        return max(mx_beg, mx_end)

                                                                            