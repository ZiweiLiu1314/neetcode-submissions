class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # longest substring with one repeating char 
        # return maxL 
        # brute force: for each of the i, we check the substring s[i:j] (i < j < len(s))
        # to see if the window_length - maxF (maximum frequency of any char) <= k 
        # if so we can update the maxL with it, O(n^2) time 

        # optimized: sliding window, j increments, if s[i:j] can be 
        # a "longest substring" after k replacements 
        # we update the maxL
        # otherwise we substract i 
        l, r = 0, 0 
        val2freq = defaultdict(int)
        maxL = 0 
        while r < len(s): 
            c = s[r]
            val2freq[c] += 1 
            while (r - l + 1) - max(val2freq.values()) > k: 
                val2freq[s[l]] -= 1 
                l += 1 
            # print(val2freq)
            # print(f"sliding window: {l}, {r}")
            maxL = max(maxL, r - l + 1)
            r += 1 
        return maxL 

        

            
