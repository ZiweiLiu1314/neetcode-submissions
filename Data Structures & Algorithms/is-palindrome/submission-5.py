class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we want to check if the string is symmetrical 
        # a way to do this would be to use two pointers, 
        # one starting in the beginng and one in the end 
        # each moves one step at a time (excluding blank spaces)
        string = list(s)
        if len(string) == 0: 
            return False 
        left = 0 
        right = len(string) - 1 
        while left < right: 
            while left < right and not string[left].isalnum(): 
                left += 1 
            while left < right and not string[right].isalnum(): 
                right -= 1 
            if string[left].lower() != string[right].lower(): 
                return False 
            left += 1 
            right -= 1 
        return True 

        
