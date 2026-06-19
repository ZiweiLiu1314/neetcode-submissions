class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort characters in strings, 
        # so that they become identical if they're anagrams 
        # sorted characters: a key 
        # append the original string to the list corresponding to this key 
        # in the hashmap 
        res = defaultdict(list)
        for s in strs: 
            key = "".join(sorted(s))
            res[key].append(s)
        return list(res.values())
        # O(m * n log n)

