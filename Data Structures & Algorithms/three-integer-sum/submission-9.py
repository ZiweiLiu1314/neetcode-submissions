class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # hash map solution 
        # sort to avoid duplicate and enable efficient search 
        nums.sort()
        res = []
        cnt = Counter(nums)
        for i in range(len(nums)):
            cnt[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            for j in range(i+1, len(nums)): 
                cnt[nums[j]] -= 1 
                if j > i+1 and nums[j] == nums[j-1]:
                    continue 
                if cnt[-nums[i] - nums[j]] > 0: 
                    res.append([nums[i], nums[j], - nums[i] - nums[j]])
            for j in range(i+1, len(nums)): 
                cnt[nums[j]] += 1 
        return res 

