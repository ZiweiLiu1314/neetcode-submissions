class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # find if the start of the word exist, and put them in a list if there are several 
        # if yes: find next letter within its neighbors, and repeat, until we find the whole word 
        # if cannot: False 
        starts = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    starts.append([i, j])
        if not starts:
            return False 
        if len(word) == 1:
            return True 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = False 
        def dfs(i, j, idx):
            nonlocal res, seen 
            if res == True:
                return 
            for v, h in directions:
                # print(f"i = {i}, v = {v}, j = {j}, h = {h}")
                if (i + v) >= 0 and (i + v) < len(board) and (j + h) >= 0 and (j + h) < len(board[0]):
                    if (i + v, j + h) not in seen and board[i + v][j + h] == word[idx]:
                        seen.add((i + v, j + h))
                        # print(f"found {idx + 1}-th letter {word[idx]} at {i + v, j + h}")
                        if idx == len(word) - 1:
                            res = True 
                            break 
                        else: 
                            dfs(i + v, j + h, idx + 1)
                        seen.discard((i + v, j + h))  # backtrack
        for start in starts:
            seen = set()
            seen.add((start[0], start[1]))
            dfs(start[0], start[1], 1)
            if res == True:
                return res 

        return res 

