from collections import Counter 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force: iterate the array for n times, to check each of the element. O(n^2)
        # no extra space 

        # optimized: using a hash map to keep track of frequencies, and then check each of the element in O(1)
        # O(n) in total 
        # O(n) space for the hash map 

        cnt = Counter(nums)
        # print(cnt)
        for key in cnt: 
            if cnt[key] > 1: 
                return True

        return False 