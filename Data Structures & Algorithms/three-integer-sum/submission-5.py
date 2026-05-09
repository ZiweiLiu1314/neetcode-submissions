class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # After sorting the array, we can fix one number 
        # and then search for the other two using the two-pointer technique.
        res = []
        nums.sort() # ascending, O(n log n)
        for i, a in enumerate(nums):
            if a > 0: 
                break 
            if i > 0 and a == nums[i - 1]: 
                continue 
            l, r = i + 1, len(nums) - 1 
            while l < r: 
                sum = a + nums[l] + nums[r]
                if sum < 0: 
                    l += 1 
                elif sum > 0: 
                    r -= 1 
                else: 
                    res.append([a, nums[l], nums[r]])
                    l += 1 
                    r -= 1 
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1 
        return res 

