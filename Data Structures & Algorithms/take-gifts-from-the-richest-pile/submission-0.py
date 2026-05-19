class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-n for n in gifts]
        for _ in range(k): 
            heapq.heapify(gifts)
            top = -heapq.heappop(gifts)
            top = int(sqrt(top))
            heapq.heappush(gifts, -top)
        return -sum(gifts) 