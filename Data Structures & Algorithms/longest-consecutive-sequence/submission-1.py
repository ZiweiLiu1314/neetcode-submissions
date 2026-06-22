class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # +1 rule, O(n), return value: the length 
        # brute force: sort and then check +1 sequence, O(n logn) 

        # for each element, traverse the array to check if we have its +1, and append it 
        # to a list if that's the case 
        if not nums:
           return 0
        nums = sorted(nums)
        print(f"nums: {nums}")
        seq = 1
        res = 1 
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue 
            if nums[i + 1] == nums[i] + 1:
                seq += 1 
                res = max(res, seq)
            else: 
                seq = 1 
        return res 

        # store the -1 and +1 of each element in a set, and check if the new element 
