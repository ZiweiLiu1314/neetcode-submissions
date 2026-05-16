class MyHashMap:

    def __init__(self):
        self.key2val = []

    def find_idx(self, key): 
        for i in range(len(self.key2val)): 
            if self.key2val[i][0] == key: 
                return i
        return -1 

    def put(self, key: int, value: int) -> None:
        idx = self.find_idx(key)
        if idx != -1: 
            self.key2val[idx][1] = value 
        else: 
            self.key2val.append([key, value])

    def get(self, key: int) -> int:
        idx = self.find_idx(key)
        if idx != -1: 
           return self.key2val[idx][1]
        return -1

    def remove(self, key: int) -> None:
        idx = self.find_idx(key)
        if idx != -1: 
            popped = self.key2val.pop(idx)
            print(f'removed {key}')
            print(popped)
            print(self.key2val)
            # self.key2val[idx][1] = -1 
        return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)