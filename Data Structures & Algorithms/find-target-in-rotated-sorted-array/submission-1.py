class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the idx of a number in a sorted and rotated array 
        # array: a sorted part (larger), a sorted part (smaller)
        # left, right, mid: which part it is in? 
        # nums[mid] >= nums[right]: left ~ mid: the sorted part (larger)
            # nums[mid] < target -> search in the right part 
            # nums[mid] > target, nums[left] > target, -> search in the right part 
            # nums[left] < target < nums[mid] -> search in the left part 
        # nums[mid] < nums[right]: right ~ mid: the sorted part 
            # nums[mid] < target, target <= nums[right] -> search in the right part 
            # nums[mid] < target, target > nums[right] -> search in the left part 
            # target < nums[mid] -> search in the left part 
        left, right = 0, len(nums) - 1 
        while left <= right: 
            mid = (left + right) // 2 
            if nums[mid] == target: 
                return mid 
            if nums[mid] >= nums[right]:
                if nums[mid] < target: 
                    left = mid + 1 
                else: 
                    if nums[mid] > target and nums[left] > target: 
                        left = mid + 1 
                    else: 
                        right = mid 
            if nums[mid] < nums[right]: # the right part is ascending 
                if nums[mid] < target and target <= nums[right]: 
                    left = mid + 1 
                else: 
                    right = mid 
        return -1 


