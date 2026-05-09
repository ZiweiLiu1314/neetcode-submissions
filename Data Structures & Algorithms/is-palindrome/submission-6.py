class Solution:
    def isPalindrome(self, s: str) -> bool:
        # basically we want to check if the string is symmetrical 
        # two ptrs, from the beginning and the end respectively 
        l, r = 0, len(s) - 1
        while l < r: 
            while l < r and not s[l].isalnum(): 
                l += 1 
            while l < r and not s[r].isalnum(): 
                r -= 1 
            if s[l].lower() != s[r].lower(): # we found that it's not symmetrical
                return False 
            l, r = l + 1, r - 1 
        return True 