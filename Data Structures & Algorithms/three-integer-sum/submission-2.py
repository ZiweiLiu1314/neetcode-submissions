class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for each number, we find the other two elements that woud make a triplet 
        # using the two pointers technique 
        res = []
        nums.sort() # ascending by default 
        for i, a in enumerate(nums): 
            if a > 0: 
                break # impossible to find a triplet 
            if i > 0 and a == nums[i - 1]: 
                continue # to avoid duplicates 
            l, r = i + 1, len(nums) - 1 
            while l < r: 
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: 
                    r -= 1 
                elif threeSum < 0: 
                    l += 1 
                else: 
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1 
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1 # to avoid duplicates 
        return res 


