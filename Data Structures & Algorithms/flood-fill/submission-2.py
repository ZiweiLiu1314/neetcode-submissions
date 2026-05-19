class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # bfs, iterative 
        q = deque()
        q.append([sr, sc])
        ori_color = image[sr][sc]
        m, n = len(image), len(image[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if ori_color == color: 
            return image 
        while q: 
            for _ in range(len(q)): 
                r, c = q.popleft()
                if image[r][c] == ori_color:
                    image[r][c] = color 
                else:
                    continue
                for dr, dc in dirs:
                    if 0 <= r + dr and r + dr < m and 0 <= c + dc and c + dc < n:
                        q.append([r + dr, c + dc])
        return image 
                
        