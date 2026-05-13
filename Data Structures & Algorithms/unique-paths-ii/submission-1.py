class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grids = [[0] * (n+1) for i in range(m+1)]
        if obstacleGrid[0][0] == 0: 
            grids[1][1] = 1 
        else: 
            grids[1][1] = 0 
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1: 
                    continue 
                if obstacleGrid[i-1][j-1] == 1: 
                    continue 
                else: 
                    grids[i][j] = grids[i-1][j] + grids[i][j-1]
        return grids[m][n]


