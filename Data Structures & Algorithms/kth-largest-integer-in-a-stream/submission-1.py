class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.minHeap = nums 
        heapq.heapify(nums)
        while len(self.minHeap) > k: 
           heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # O(log n) 
        if len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap) # O(log n) 
        return self.minHeap[0] 
        

        
