from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            count = [0] * 26 
            for char in string: 
                count[ord(char) - ord("a")] += 1 
                # Negative index for uppercase 
            res[tuple(count)].append(string) 
            # keys have to be of immutable type 
        return list(res.values())
