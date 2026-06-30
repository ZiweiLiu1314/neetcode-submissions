class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # finding word in the 2D grid 
        # backtracking, find a path with predefined letters 
        # try to find each of the letter by following neighbors, if we do find a path, proceed / True 
        # if a step is invalid, undo and continue the search, no path recording needed 
        ROWS = len(board)
        COLS = len(board[0])
        # seen = set()
        def dfs(r, c, idx):
            nonlocal seen 
            if idx == len(word):
                return True 
            
            if min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] != word[idx] or (r, c) in seen:
                return False 
            # print(f"on {r, c}, we found {word[idx]}, and seen is {seen}")
            seen.add((r, c))
            res = dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1)
            seen.remove((r, c))
            return res 

        for i in range(ROWS):
            for j in range(COLS):
                seen = set()
                if dfs(i, j, 0):
                    return True 
        
        return False 