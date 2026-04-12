class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(r,c):
            if min(c,r) < 0 or c >= COLS or r >= ROWS or grid[r][c] != "1":
                return

            grid[r][c] = "0"

            dirs = ((1,0), (-1,0), (0,1), (0,-1))
            for dr, dc in dirs:
                next_r, next_c = r + dr, c + dc
                dfs(next_r, next_c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c)
        
        return count