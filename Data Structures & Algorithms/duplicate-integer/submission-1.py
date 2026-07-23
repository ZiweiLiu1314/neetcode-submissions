# from collections import defaultdict 
# check if there's ANY element in the array that appeared > once 
# checking freq: dict 
# keep a dict of values in nums, while going through it once 
# if we encounter a duplicate -> return True 
# x until the end -> False 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num2freq = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in num2freq: 
                return True 
            num2freq[num] = 1 
        return False 