class Node():
    def __init__(self, key, value):
        self.key = key 
        self.val = value
        self.prev = self.next = None 

class LRUCache:
# doubly linked list solution from scratch 
    def __init__(self, capacity: int):
        # hash map, key -> Node in the doubly linked list 
        # to enable efficient lru tracking 
        self.cap = capacity 
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
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
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next.key
            self.remove(self.cache[lru])
            del self.cache[lru]
        
