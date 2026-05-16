class Node:
    def __init__(self, key, value, Next = None):
        self.key, self.val = key, value 
        self.next = Next 

class MyHashMap:
    # 3. a balanced approach, by hash mapping keys into 1000 buckets 
    # handle collsions using linked list 

    def __init__(self):
        # define a list (len: 1000) of nodes, acting as the start node for each bucket 
        # self.map = [Node(0, 0)] * (1000 + 1)
        self.map = [Node(0, 0) for _ in range(1000 + 1)] 
    
    def hash(self, key): 
        idx = key % 1000 
        return self.map[idx]

    def put(self, key: int, value: int) -> None:
        node = self.hash(key)
        while node.next: 
            if node.next.key == key: 
                node.next.val = value 
                return 
            node = node.next # keeps the linked list intact 
        node.next = Node(key, value)
        print(f'done putting {key, value}')
        return 

    def get(self, key: int) -> int:
        node = self.hash(key)
        print(f'looking for key {key}')
        while node.next: 
            print(f'at {node.next.val} to the key {node.next.key}')
            if node.next.key == key: 
                print(f'found value {node.next.val} to the key {key}')
                return node.next.val
            node = node.next # keeps the linked list intact 
        return -1 

    def remove(self, key: int) -> None:
        node = self.hash(key)
        while node.next: 
            if node.next.key == key: 
                node.next = node.next.next 
                return 
            node = node.next # keeps the linked list intact 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)