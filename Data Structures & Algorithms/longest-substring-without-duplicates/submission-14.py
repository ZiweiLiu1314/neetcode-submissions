from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force: examine every substring, O(n^2)
        # optimized: sliding window, append the right as long as there's no dup
        # and shrink on the left, then continue 
        # until r reaches the end of the string 
        if not s: 
            return 0 
        l, r = 0, 1
        maxL = 1 
        while r < len(s):
            uniques = set()
            uniques.add(s[l])
            while r <= len(s) - 1 and s[r] not in uniques:
                # find longest substring with l as the left boundary
                uniques.add(s[r])
                maxL = max(maxL, r - l + 1)
                r += 1 
            l += 1 
            r = l + 1
        return maxL 