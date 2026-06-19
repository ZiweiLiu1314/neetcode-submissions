from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find the unique k most frequent elements 
        # hash map for counting frequency 
        # reverse hash map, freq2nums 
        # find the largest keys using maxheap
        # find the values corresponding to the keys 
        # or: keep a list of k elements, and the lowest freq & index & num 
        # and when we encounter each new element, if its freq > lowest 
        # we replace the least frequent element 
        cnt = Counter(nums)
        print(cnt)
        """
        freq2nums = defaultdict(int)
        for key in cnt: 
            freq2nums[cnt[key]] = key 
        print(freq2nums)
        """
        freqs = list(cnt.values())
        maxi = heapq.nlargest(k, freqs)
        mini = min(maxi)
        res = []
        for key in cnt: 
            if cnt[key] >= mini:
                res.append(key)
        return res 

