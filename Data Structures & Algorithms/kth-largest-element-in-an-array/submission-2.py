class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sorting, kth largest element 
        # quick sort, recursion, divide-and-conquer 
        # find a pivot, smaller than it -> left, bigger -> right 
        # we know which side of it k lies in 
        # recursion, continuing doing this in the correct side 
        # master theorem: average time complexity, O(n log n)
        if not nums: 
            return None 
        if len(nums) == 1:
            # print(f"found {nums[0]}")
            return nums[0]
        pivot = nums[0]
        i, j = 0, len(nums) - 1
        # def partialSort(): #p: pivot, i, j: starting & end point 
        while i < j: 
            # on the side of j 
            while nums[j] <= pivot and i < j: 
                j -= 1 
                # case 1 found nums[j] < p 
                # case 2 reached the end 
            if not i < j: 
                break 
            else: # j reached a position > p 
                nums[i] = nums[j]
                # cannot update j because we need to keep the empty index 
            # on the side of i 
            while nums[i] > pivot and i < j: 
                i += 1
            if not i < j: 
                break 
            else: # found a element smaller than p
                nums[j] = nums[i]
                # cannot update i because it's the empty space for p 
            # what if we found elements == 0 
            # i: index of p after sorted 
        nums[i] = pivot
        if i != k - 1: # we want to find the index k - 1 
            if i < k - 1: 
                # print(f"pivot {pivot} landed at position {i}, moving to the right")
                # print(nums) 
                # recursion debug 
                # print the state, input to the recursion 
                return self.findKthLargest(nums[i+1:], k - i - 1)
            else: 
                # print(f"pivot {pivot} landed at position {i}, moving to the left")
                # print(nums) # the state 
                # 
                return self.findKthLargest(nums[:i], k)
        if i == k - 1:
            return nums[i]
        # if i == k - 1:
        #     return nums[i]


                