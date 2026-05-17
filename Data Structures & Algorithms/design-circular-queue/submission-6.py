class Node:
    def __init__(self, value):
        self.val = value
        self.prev, self.next = None, None 

class MyCircularQueue:
    # enQueue: 
    # if length of the queue < size -> insert to the end, return true 
    # else -> return false
    # deQueue: 
    # if length of the queue > 0 -> pop first element from the start, return true 
    # else -> return false 
    # front:
    # if length of the queue > 0 -> fifo, return first element in the queue, return true 
    # else -> return false 

    # doubly linked list 
    # so that we can always quick access front or back using left or right node 
    # and inserting would be inserting a node, which is O(1)
    # but we'll need a separate variable for keeping track of the length 
    # time comp: O(1)
    # space comp: O(n) # n: elements in the queue 

    def __init__(self, k: int):
        self.cap = k
        self.leng = 0 
        self.left, self.right = Node(0), Node(0)
        self.left.next, self.right.prev = self.right, self.left 

    def enQueue(self, value: int) -> bool:
        if self.leng < self.cap: 
            # insert before the self.right 
            node = Node(value)
            last = self.right.prev 
            node.next, node.prev = self.right, last
            last.next, self.right.prev = node, node 
            self.leng += 1 
            return True 
        return False 

    def deQueue(self) -> bool:
        # pop first element from the start, return true 
        if self.leng > 0: 
            first = self.left.next
            second = self.left.next.next 
            self.left.next, second.prev = second, self.left
            self.leng -= 1
            return True 
        return False 

    def Front(self) -> int:
        if self.leng > 0: 
            return self.left.next.val 
        return -1 

    def Rear(self) -> int:
        if self.leng > 0: 
            return self.right.prev.val 
        return -1 

    def isEmpty(self) -> bool:
        if self.leng == 0:
            return True 
        return False 

    def isFull(self) -> bool:
        if self.leng == self.cap:
            return True 
        return False 


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()