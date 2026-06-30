class RandomizedSet:
# brute force: array, insert O(1), remove O(n), getRandom O(1) 
# optimized: use together with a hash map to store the index for O(1) removal 
    def __init__(self):
        self.nums = []
        self.val2idx = defaultdict(int)

    def insert(self, val: int) -> bool:
        # add if not present 
        if val in self.val2idx:
            return False 
        self.val2idx[val] = len(self.nums)
        self.nums += [val]
        return True 
        

    def remove(self, val: int) -> bool:
        # remove if present, return True 
        # otherwise return False 
        # swap it with the last element, and delete the last element from the hash map 
        if not val in self.val2idx: 
            return False 
        idx = self.val2idx[val]
        last = self.nums[- 1] 
        # update hash map 
        self.val2idx[last] = idx 
        del self.val2idx[val]
        # update array 
        self.nums[idx] = self.nums[- 1] 
        self.nums.pop()
        return True 

    def getRandom(self) -> int:
        return random.choice(self.nums)
        # same probability random 
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()