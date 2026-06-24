class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k replacements 
        # longer substring of repeating char 
        # brute force: for every char, replace different chars on its right 
        # with itself for k times, and count how long the repeating seq is 
        # time O(n ^ 2)
        # corrected: for each index i, 
        # extend the substring by increasing j from i to the end 
        # and keep track of the maximum frequency of s[j] 
        # update maxf (most frequent character in the current window) 
        # if window size - maxf <= k 
        # update res with current window size 
        if not s: 
            return 0 
        res = 1 
        for i in range(len(s)):
            cnt = defaultdict(int)
            cnt[s[i]] += 1 
            maxf = 1 
            window_size = 1 
            for j in range(i + 1, len(s)):
                window_size += 1 
                cnt[s[j]] += 1 
                if cnt[s[j]] > maxf:
                    maxf = cnt[s[j]] 
                if window_size - maxf <= k: 
                    res = max(res, window_size)
                    # print(f"updated res to {res}")
                # print(f"i: {i}, j: {j}, cnt: {cnt}, window_size: {window_size}, maxf: {maxf}, res: {res}")
        return res 


        # optimized: build a counter for chars as we go from left to right
        # 