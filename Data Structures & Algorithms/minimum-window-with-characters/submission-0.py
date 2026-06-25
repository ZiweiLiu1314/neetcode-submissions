class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        minL = 1e4
        shortest = ""
        # check substrings of s, s.t. the substring includes all chars in t
        # increment right boundary until it does include, and then constract left boundary
        def check_containing(string):
            cnt_s = Counter(string)
            for c in cnt_t:
                if cnt_s[c] < cnt_t[c]:
                    return False 
            return True 
        l, r = 0, 0
        while r < len(s): 
            # print(f"substring: {substring}")
            while not check_containing(s[l:r + 1]) and r < len(s): 
                # expand the substring while 
                # print(f"substring: {s[l:r + 1]}")
                r += 1 
            while check_containing(s[l:r + 1]):
                # print(f"substring: {substring}")
                if r - l + 1 < minL:
                    shortest = s[l:r + 1]
                    minL = r - l + 1 
                l += 1 
        return shortest

            
