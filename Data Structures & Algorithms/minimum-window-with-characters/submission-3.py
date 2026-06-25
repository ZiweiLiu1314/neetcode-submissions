class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        minL = 1e4
        shortest = ""
        # check substrings of s, s.t. the substring includes all chars in t
        # increment right boundary until it does include, and then constract left boundary
        
        # update have and need as we go, instead of checking every time
        l, r = 0, 0
        cnt_t = Counter(t) 
        cnt_substring = defaultdict(int)
        minL = 1e4
        shortest = ""
        have = 0
        need = len(cnt_t.keys())
        # print(f"have: {have}, need: {need}")
        while r < len(s): 
            c = s[r]
            cnt_substring[c] += 1 
            if c in cnt_t and cnt_substring[c] == cnt_t[c]: 
                have += 1 
            while have == need: 
                if r - l + 1 < minL: 
                    shortest = s[l:r+1] 
                    # print(f"new shortest: {shortest}")
                    minL = r - l + 1
                cnt_substring[s[l]] -= 1 
                if s[l] in cnt_t and cnt_substring[s[l]] < cnt_t[s[l]]:
                    have -= 1 
                l += 1 
            r += 1 
        return shortest 
                
                

        
        
        
        
        
        
        
        
        """
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
        """
            
