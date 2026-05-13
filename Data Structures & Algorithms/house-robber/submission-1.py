class Solution:
    def rob(self, nums: List[int]) -> int:
        # find the maximum money to rob, 
        # contraint: cannot rob two adjacent houses 
        # can be decomposed into two sub-problems: 
        # nums[0] + rob(nums[2:]), rob([1:])
        # if we took nums[0], we have to skip nums[1]
        # or we just start from nums[1]
        # in-order, find optimal before i, which consists of two cases 
        # case 1: we took i-1, then: rob([:i-1])
        # case 2: we didn't take i-1, then: nums[i] + rob([:i-2])
        # so to know the optimal answer until i, we only need to know: 
        # rob[:i-1] and rob([:i-2]) 
        # DP 
        rob1, rob2 = 0, 0
        for n in nums:
            # find maximum value at each step 
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp 
        return rob2 