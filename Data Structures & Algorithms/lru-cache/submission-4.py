class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = []

    def get(self, key: int) -> int:
        for i in range(len(self.cache)): 
            if self.cache[i][0] == key: 
                temp = self.cache.pop(i)
                self.cache.append(temp)
                return temp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)): 
            if self.cache[i][0] == key:
                print(f'pop{i}')
                temp = self.cache.pop(i)
                break 
        self.cache.append([key, value])
        print(f'after putting {key, value}, cache is {self.cache}')
        if len(self.cache) > self.cap: 
            print(self.cache)
            print(f'{len(self.cache)} exceeded {self.cap}, deleted')
            self.cache.pop(0)
        
