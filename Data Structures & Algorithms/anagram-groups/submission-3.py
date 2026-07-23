from collections import defaultdict, Counter 
# group strs into anagrams 
# compare each of the strings with each of the previous groups 
# comparison: using Counters, compare if they have the same chars&freqs
# go through the strings for once only 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        def compare_anagrams(cnt1, cnt2): 
            for char in cnt1:
                if (char in cnt2) and (cnt2[char] == cnt1[char]):
                    del cnt2[char]
                    continue 
                else: 
                    return False 
            if not cnt2: 
                return False 
            return True 
            # return True if anagrams, False otherwise 
        """
        def compare_anagrams(str1, str2): 
            # print(f"compare strings {str1, str2}")
            cnt1 = Counter(str1)
            cnt2 = Counter(str2)
            for char in cnt1:
                if (char in cnt2) and (cnt2[char] == cnt1[char]):
                    del cnt2[char]
                    continue 
                else: 
                    # print(f"false since missing char")
                    return False 
            if cnt2: 
                # print(cnt2)
                # print(f"false since excessive char")
                return False 
            # print(f"true anagrams")
            return True 
            # return True if anagrams, False otherwise 
        # cnt2group = defaultdict(list)
        res = []
        for i in range(len(strs)):
            string = strs[i]
            # str_cnt = Counter(string)
            found = False 
            # check against each of the existing anagram group, if find its group -> append 
            # otherwise, create a new group 
            # for cnt in cnt2group: 
            for i in range(len(res)): 
                group = res[i]
                if compare_anagrams(group[0], string):
                    # print(f"found anagrams {group[0], string}")
                    # cnt2group[cnt] += [string]
                    res[i] += [string]
                    found = True 
                    break 
            if not found: 
                # cnt2group[str_cnt] = [string]
                res.append([string])
        return res # list(cnt2group.values())
                

