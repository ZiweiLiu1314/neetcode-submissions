class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find 
        # parent node, path compression 
        # rank, which is the num of elements in the group with it as parent 
        par = [i for i in range(n)]
        rank = [1] * n 
        res = n 
        def find(n1): 
            res = n1 
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res 
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0 
            if rank[p1] > rank[p2]:
                par[p2] = p1 
                rank[p1] += rank[p2]
            else: 
                par[p1] = p2 
                rank[p2] += rank[p1]
            return 1 
        
        for v1, v2 in edges: 
            res -= union(v1, v2)
    
        return res 



                