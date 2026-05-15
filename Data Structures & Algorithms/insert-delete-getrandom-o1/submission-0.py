class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap: 
            self.arr.append(val)
            self.hashmap[val] = len(self.arr) - 1 
            return True 
        else: 
            return False 

    def remove(self, val: int) -> bool:
        # hash map, for val -> idx pair 
        # stay synchronous without array
        if val in self.hashmap: 
            idx = self.hashmap[val]
            last_val = self.arr[len(self.arr) - 1]
            self.hashmap[last_val] = idx 
            self.arr[idx] = last_val 
            self.arr = self.arr[:-1]
            del self.hashmap[val]
            return True 
        return False 

    def getRandom(self) -> int:
        rdm_idx = random.randint(0, len(self.arr) - 1)
        return self.arr[rdm_idx]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()