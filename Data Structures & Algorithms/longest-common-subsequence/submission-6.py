from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache 
        def rec(t1, t2):
            # print(f"len(t1) = {len(t1)}, len(t2) = {len(t2)}")
            
            if min(len(t1), len(t2)) <= 0:
                return 0 
            if t1[0] == t2[0]:
                # print(f"t1: {t1}, t2: {t2}")
                # print(f"input to recursion: t1: {t1[1:]}, t2: {t2[1:]}")
                return 1 + rec(t1[1:], t2[1:])
            else: 
                return max(rec(t1[1:], t2), rec(t1, t2[1:]))
        
        return rec(text1, text2)
