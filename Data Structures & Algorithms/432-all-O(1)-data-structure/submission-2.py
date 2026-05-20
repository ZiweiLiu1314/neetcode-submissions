class Node:
    def __init__(self, key, val, prv = None, nxt = None):
        self.key, self.val = key, val 
        self.prev, self.next = prv, nxt 


class AllOne:
    # store strings' count 
    # return strings with min / max counts 
    # key (string) -> count of the string 
    # O(1)
    # things to achieve 
    # 1. mapping 
    # 2. finding max / min 
    # approaches 
    # 1. brute force: store [key, count] in an array, all operations would be O(n) (traverse the entire array)
    # 2. hash map, to enable quick insertion and deletion 
    # in parallel, use a doubly linked list, enables finding max / min in O(1) (sorted). (descending )
    def __init__(self):
        self.key2count = collections.defaultdict(list)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node): 
        # remove node from doubly linked list 
        prv, nxt = node.prev, node.next 
        # print(f'prv: {prv.key}, {prv.val}')
        # print(f'nxt: {nxt.key}, {nxt.val}')
        temp = prv 
        prv.next = nxt 
        nxt.prev = temp 
    
    def add_node_after(self, node, prv): 
        # add node after prv, between prv and nxt 
        nxt = prv.next 
        node.prev, node.next = prv, nxt 
        nxt.prev = node 
        prv.next = node 
        """
        print('doubly linked list')
        root = self.left 
        while root: 
            print(root.key, root.val)
            root = root.next  
        """

    def inc(self, key: str) -> None:
        # exist -> increment 1 
        # no -> insert 1  
        value = 1            
        if key in self.key2count: 
            # already have a node 
            node = self.key2count[key]
            value = node.val + 1 
            
            # # conpare with previous node and move ahead if became larger than the previous node 
            prv = node.prev
            """
            print(f'node: {node.key}, {node.val}')
            print(f'prv: {prv}')
            print(f'found {key} after {prv.val}')
            """
            if value > prv.val: 
                while value > prv.val and prv.val != 0: 
                    prv = prv.prev # find the prv, the node with val just larger than value 
                self.remove(node)

                nnode = Node(key, value)
                self.add_node_after(nnode, prv)
                del self.key2count[key]
                self.key2count[key] = nnode 
                """print(f'added {key} after {prv.val}')"""
            else: 
                node.val = value 
                self.key2count[key] = node 
        
        else: 
            nnode = Node(key, value)
            self.add_node_after(nnode, self.right.prev)
            """print(f'added {key} before self.right')"""
            self.key2count[key] = nnode 

    def dec(self, key: str) -> None:
        # always exists -> decrements 1; key == 0 -> remove 
        if key in self.key2count: 
            # already have a node 
            node = self.key2count[key]
            value = node.val - 1 
            del self.key2count[key]
            self.remove(node)
            if value > 0: # add the new node to the double linked list, and the hash map 
                # # conpare with next node and move ahead if became smaller than the next node 
                nxt = node.next
                while value < nxt.val and nxt.val != 0: 
                    nxt = nxt.next # find the prv, the node with val just larger than value 
                self.remove(node)

                nnode = Node(key, value)
                self.add_node_after(nnode, nxt.prev)
                self.key2count[key] = nnode 
        

    def getMaxKey(self) -> str:
        # element(s) exist -> return (one of) key corresponding to the max count 
        # no element -> ""
        if self.left.next.val != 0:
            return self.left.next.key
        else: 
            return ""

    def getMinKey(self) -> str:
        # element(s) exist -> return (one of) key corresponding to the min count 
        # no element -> ""
        if self.right.prev.val != 0:
            return self.right.prev.key
        else: 
            return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()