class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grids = [[0] * (n+1) for _ in range(m+1)]
        grids[1][1] = 1 
        # state transition formula 
        for i in range(1, m+1): 
            for j in range(1, n+1): 
                if i == 1 and j == 1:
                    continue 
                grids[i][j] = grids[i-1][j] + grids[i][j-1]
        return grids[m][n]