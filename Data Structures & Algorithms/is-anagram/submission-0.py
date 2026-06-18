from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force: for each of the character in s, 
        # iterate through t to find if there's same amount of same char 
        # optimized: compare hash maps of s and t 
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        for key in cnt1: 
            if cnt1[key] != cnt2[key]:
                return False 
            else: 
                del cnt2[key]
        if cnt2: 
            return False 
        else: 
            return True
