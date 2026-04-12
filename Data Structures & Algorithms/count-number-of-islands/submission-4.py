class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        
        def bfs(r,c):
            q = collections.deque([(r,c)])
            grid[r][c] = "0"

            while q:
                cur_r, cur_c = q.popleft()

                dirs = ((0,1), (0,-1), (1,0), (-1,0))
                for dr, dc in dirs:
                    next_r, next_c = cur_r + dr, cur_c + dc
                    if (0 <= next_r < ROWS and
                        0 <= next_c < COLS and
                        grid[next_r][next_c] == "1"):
                        grid[next_r][next_c] = "0"                        
                        q.append((next_r, next_c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r,c)
        return count
