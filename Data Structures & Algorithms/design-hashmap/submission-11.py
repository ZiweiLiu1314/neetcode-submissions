class Node: 
    def __init__(self, key, value, nxt = None):
        self.key, self.val = key, value
        self.next = nxt

class MyHashMap:
    # put: y -> update; n -> add 
    # get: y -> return; n -> -1 
    # remove: y -> del; n -> x 
    # a few things to confirm: 
    # time comp of each operation? 
    # range of the numbers (key, value, # operations)? 
    # approaches 
    # 1. list, [key, value], O(n) time, O(n) space (n: total number of elements 
    # 2. list, [value] and the idx would be the key, O(1) time, O(1,000,000) 
    # 3. hashing + linkedlist, O(n/k) time, O(k + n) (k: num of buckets / 1000 
    # key % 1000, store the elements falling into the same buckets using linked list 

    def __init__(self):
        self.map = [Node(0, 0) for _ in range(1001)]
    
    def hash(self, key):
        idx = key % 1000
        return self.map[idx]

    def put(self, key: int, value: int) -> None:
        node = self.hash(key)
        while node.next: 
            if node.next.key == key: 
                node.next.val = value 
                return 
            node = node.next 
        node.next = Node(key, value)
        return 

    def get(self, key: int) -> int:
        node = self.hash(key)
        while node.next: 
            if node.next.key == key: 
                return node.next.val
            node = node.next 
        return -1 

    def remove(self, key: int) -> None:
        node = self.hash(key)
        while node.next: 
            if node.next.key == key: 
                node.next = node.next.next 
                return 
            node = node.next 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)