class Node:
    def __init__(self, key, val): 
        self.key, self.val = key, val 
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0 ,0)
        self.left.next, self.right.prev = self.right, self.left 

    def remove(self, node):
        prv, nxt = node.prev, node.next 
        prv.next, nxt.prev = nxt, prv  

    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        print(f'after get, cache is {self.cache}')
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        print(f'after put and before checking cap, cache is {self.cache}')
        root = self.left
        while root: 
            print(root.key)
            root = root.next
        if len(self.cache) > self.cap: 
            lru = self.left.next 
            print(f"lru: {lru.key}, {lru.val}")
            self.remove(lru)
            del self.cache[lru.key]
        print(f'after put, cache is {self.cache}')
        
