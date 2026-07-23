from collections import Counter 
# anagram: containing the same characters 
# 1. same chars; 2. appear for the same amount of the time. 
# build char2freq hashmaps for both, check if they got the same hasmaps 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char2freq_s = Counter(s)
        char2freq_t = Counter(t)
        for char in char2freq_s:
            if char2freq_t[char] != char2freq_s[char]:
                return False
            else: 
                del char2freq_t[char]
        if char2freq_t:
            return False 
        return True 