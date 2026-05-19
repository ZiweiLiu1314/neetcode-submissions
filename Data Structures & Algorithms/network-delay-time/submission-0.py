class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # shortest path to all nodes 
        # bfs, min heap 
        visited = set()
        minHeap = [(0, k)] 
        # the nodes reachable from a node, and the corresponding weights 
        edges = collections.defaultdict(list)
        for u, v, t in times: 
            edges[u].append([v, t])
        t = 0 
        while minHeap: 
            w1, node1 = heapq.heappop(minHeap)
            if node1 in visited: 
                continue 
            visited.add(node1)
            t = max(t, w1)
            for node2, w2 in edges[node1]:
                if node2 in visited: 
                    continue 
                heapq.heappush(minHeap, (w1 + w2, node2))
        if len(visited) != n: 
            return -1 
        return t 


