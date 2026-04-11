class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r,c):
            if (min(r,c) < 0 or r == rows or c == cols or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"

            dirs = ((1,0), (-1,0), (0,1), (0,-1))
            for dr, dc in dirs:
                next_r, next_c = r + dr, c + dc
                dfs(next_r, next_c)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c)
        
        return count