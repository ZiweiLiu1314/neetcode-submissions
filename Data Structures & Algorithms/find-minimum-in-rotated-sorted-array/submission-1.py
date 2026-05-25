class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force: iterating and keep track of the min 
        # optimization 
        # what we have: originally ascending (all elements unique)
        # rotated for 1~n times 
        # how can we tell which half the min is in? 
        # [1, 2, 3, 4, 5]
        # [3 (l), 4, 5 (m), 1, 2 (r)] (after rotated for 4 times)
        # right sorted part is always smaller than the left sorted part 
        # binary search: is mid pointer on the left or right sorted part? 
        # if nums[m] >= nums[l]: mid on the left sorted part
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1 
        mini = nums[left]
        while left < right: 
            mid = left + ((right - left) // 2)
            print(f"left {left, nums[left]}, right {right, nums[right]}, mid {mid, nums[mid]}")
            mini = min(mini, nums[mid], nums[right])
            if nums[mid] > nums[left]: 
                left = mid 
            else: 
                right = mid 
        return mini 
        # [3,4,5,6,1,2] # mid = 0 + (5 // 2) = 2, nums[mid] = 5 > 3, left = 2 
        # [5, 6, 1, 2] # mid = 2 + ((5 - 2) // 2) = 3, left = 3 
        # [6, 1, 2], mid = 3 + ((5 - 3) // 2) = 4, right = 4 
        # [6, 1], mid = 3 + ((4 - 3) // 2) = 3, right = 3 
        # 
