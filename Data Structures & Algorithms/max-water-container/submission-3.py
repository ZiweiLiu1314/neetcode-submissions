class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # so basically we want to find the combination of i, j, 
        # 0 < i < j < len(heights)
        # with maximum (j - i) * min(heights[i], heights[j]) 
        # instead of brute force, which would be iterating through all 
        # possible combinations, and would be O(n2)
        # if we use two ptrs, we can look at each height[i] only once 
        # and eliminate one column that "cannot make up a better container"
        # at each step 
        # O(n) time 
        # start from left and right boundary, and eliminate one column a time
        l, r = 0, len(heights) - 1
        mx = 0
        water = 0 
        while l < r: 
            mx = max((r - l) * min(heights[l], heights[r]), mx)
            if heights[l] > heights[r]: 
                r -= 1
            else: 
                l += 1
        return mx 
            