# double linked list class 
class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val 
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # map key to node 
        self.cap = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left 

    def remove(self, node):
        # remove a node from the doubly linked list 
        prv, nxt = node.prev, node.next 
        print(f"Node {node.key}, {node.val}")
        nxt.prev, prv.next = prv, nxt 

    def insert(self, node):
        # add a node to the right of the doubly linked list 
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node 
        node.next, node.prev = nxt, prv 

    def get(self, key: int) -> int:
        if key in self.cache:
            print(self.cache[key])
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        print(f"put {key} in cache, with value {self.cache[key].val}")
        self.insert(self.cache[key])

        while len(self.cache) > self.cap: 
            lru = self.left.next # exceeds cache capacity 
            self.remove(lru)
            del self.cache[lru.key]
        
