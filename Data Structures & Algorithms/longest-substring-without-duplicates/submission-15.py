class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substring without duplicate characters 
        # brute force: for each starting point i, check for every starting point j 
        # (i < j < len(s)), if it's such a substring, O(n^2)
        # optimized: sliding window, expand when it's a "unique substring"
        # contract on the left if it's not, until it is again 
        l, r = 0, 0
        maxL = 0 
        val2freq = defaultdict(int)
        while r < len(s):
            c = s[r]
            val2freq[c] += 1 
            while val2freq[c] > 1: 
                # not unique anymore; need to subtract on the left 
                val2freq[s[l]] -= 1 
                l += 1 
            # print(f"sliding window: {l}, {r}")
            # print(val2freq)
            # surely unique now; update maxL 
            maxL = max(maxL, (r - l + 1))
            r += 1 
        return maxL 