class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # brute force: for every index i in s, check every substring s[i:j+1], i < j < len(s)
        # O(n^2) time 
        # optimized: sliding window, l, r = 0, 0, move r to the right until we find a substring
        # that includes all char (includ. dup.), and see if we can contract on the left 
        # O(n) time 
        minL = 1e4
        cnt_t = Counter(t)
        cnt_substring = defaultdict(int)
        l, r = 0, 0
        need = len(cnt_t.values())
        have = 0 
        substring = ""
        while r < len(s):
            c = s[r]
            cnt_substring[c] += 1 
            if c in cnt_t and cnt_substring[c] == cnt_t[c]: 
                have += 1 
            while have == need: 
                window_length = r - l + 1 
                if window_length < minL:
                    substring = s[l : r + 1]
                    minL = window_length
                cnt_substring[s[l]] -= 1 
                if s[l] in cnt_t and cnt_substring[s[l]] < cnt_t[s[l]]: 
                    have -= 1 
                l += 1 
            r += 1 

        return substring 
