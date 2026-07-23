from collections import Counter, defaultdict
# two different elements summing up to target 
# such a pair is unique if they exist 
# return [i, j], i < j (no requirement that nums[i] != nums[j] -> keep track of the freq)
# create a hashmap, check for each of the element i, (traversing from the left)
# if its supplement (target - i) is in the hashmap 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2freq = Counter(nums)
        num2idx = defaultdict(list) # list of indices 
        for i in range(len(nums)): 
            num = nums[i]
            num2idx[num] += [i]
            # print(num2idx[num])
        for i in range(len(nums)):
            num = nums[i]
            nums2freq[num] -= 1 
            if (target - num) in nums2freq: 
                # find the idx using the other hashmap 
                indices = num2idx[target - num]
                # find the idx != i 
                for idx in indices: 
                    if idx != i: 
                        j = idx
                        return [i, j]
                        # we would essentially find j, bcs if we found the val in Count 
                        # -> does exist 

            nums2freq[num] += 1 
        raise ValueError("No such pair found.")
