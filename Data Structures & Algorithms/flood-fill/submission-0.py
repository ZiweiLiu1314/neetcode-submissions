class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # dfs, recursive 
        ori_color = image[sr][sc]
        m, n = len(image), len(image[0]) 
        if color == ori_color:
            return image 
        dirs = [[0, 1,], [0, -1], [1, 0], [-1, 0]]
        def dfs(sr, sc): 
            if sr < 0 or sr >= m or sc < 0 or sc >= n or image[sr][sc] == color:
                return 
            if image[sr][sc] == ori_color:
                image[sr][sc] = color 
                for i, j in dirs: 
                    dfs(sr + i, sc + j)
        dfs(sr, sc)
        return image
            