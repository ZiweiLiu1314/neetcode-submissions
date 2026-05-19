class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)
        while len(stones) >= 2: 
            x = -1 * heapq.heappop(stones) # largest 
            y = -1 * heapq.heappop(stones) # smallest 
            if x > y: 
                z = y - x 
                heapq.heappush(stones, z)
        if len(stones) == 0: 
            return 0 
        else: 
            return -stones[0]
            