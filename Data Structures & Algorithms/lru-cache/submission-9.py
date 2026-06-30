class Node:
    def __init__(self, value = 0, prv = None, nxt = None):
        self.val = value 
        self.prev = prv
        self.next = nxt

class LRUCache:
# size: capacity of key->value pairs
# hash map to store the pairs, O(1) get, x track LRU 
# doubly linked list: LRU pattern, move a node to the front when "used", hash map for O(1) find the node
# choose the last 
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2val = defaultdict(int)
        self.left = Node(value = None)
        self.right = Node(value = None)
        self.left.prev, self.right.next = None, None 
        self.left.next, self.right.prev = self.right, self.left 
        self.key2node = defaultdict(Node)
    
    def insert_after_left(self, curr):
        tmp = self.left.next 
        self.left.next, tmp.prev = curr, curr 
        curr.next, curr.prev = tmp, self.left

    def get(self, key: int) -> int:
        if key in self.key2val:
            # update the doubly linked list        
            curr = self.key2node[key] 
            prv = curr.prev 
            nxt = curr.next 
            prv.next, nxt.prev = nxt, prv 
            self.insert_after_left(curr) 
            return self.key2val[key]
        return -1 

    def put(self, key: int, value: int) -> None:
        # remove the least recently used key 
        # i.e. if a get or a put operation is called on it.
        # find the node and remove from the linked list if it already exists 
        if key in self.key2val: 
            curr = self.key2node[key] 
            prv = curr.prev 
            nxt = curr.next 
            prv.next, nxt.prev = nxt, prv 
        else: 
            curr = Node(value = key)
            self.key2node[key] = curr 
        # update the hash map and add to the front of the doubly linked list 
        self.insert_after_left(curr) 
        self.key2val[key] = value 

        # check if cap is exceeded 
        if len(self.key2val) > self.cap: 
            lru = self.right.prev 
            del self.key2val[lru.val] 
            del self.key2node[lru.val] 
            prv = lru.prev 
            prv.next = self.right 
            self.right.prev = prv 
