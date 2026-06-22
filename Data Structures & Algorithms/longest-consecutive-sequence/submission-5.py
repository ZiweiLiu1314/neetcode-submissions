class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # +1 rule, O(n), return value: the length 
        if not nums:
           return 0

        # brute force: O(n ^ 2) 
        """
        unique_nums = set(nums)
        length = 1 
        res = 1 
        for i in range(len(nums)):
            curr = nums[i]
            while (curr + 1) in unique_nums:
                length += 1 
                curr += 1 
            res = max(res, length)
            length = 1 
        return res 
        """


        # sort and then check +1 sequence, O(n logn) 
        """
        nums = sorted(nums)
        print(f"nums: {nums}")
        seq = 1
        res = 1 
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue 
            if nums[i + 1] == nums[i] + 1:
                seq += 1 
                res = max(res, seq)
            else: 
                seq = 1 
        return res 
        """
        """
        res = 0 
        nums.sort()

        curr, streak = nums[0], 0 
        i = 0
        while i < len(nums):
            if curr != nums[i]: # streak is broken 
                curr = nums[i] # restart by anchoring a new streak at nums[i] 
                streak = 0 
            while i < len(nums) and nums[i] == curr: # skip duplicates 
                i += 1 # advance i past every copy of curr 
            streak += 1 # consumed at least one copy of curr, so the streak grows by one 
            curr += 1 # update the expectation: to keep the streak going, the next value must be curr + 1 
            res = max(res, streak) # track the best streak so far 
        return res 
        """

        # store the -1 and +1 of each element in a set, and check if the new element 
        # is in the set 
        """
        consecutive = set()
        res = 1
        for i in range(len(nums)):
            consecutive.add(nums[i] - 1)
            consecutive.add(nums[i] + 1)
            if nums[i] in consecutive: 
                consecutive.remove(nums[i])
                res += 1 
        return res 
        """
        # my attemp above was actually close 
        # only that I only need to look for the "beginning" of a consecutive sequence 

        numSet = set(nums)
        longest = 0 

        for num in numSet: 
            if (num - 1) not in numSet: 
                length = 1 
                while (num + length) in numSet:
                    length += 1 
                longest = max(length, longest)
        return longest 

                

        
