class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid and not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def bfs(r, c):
            queue = collections.deque([(r,c)])
            grid[r][c] = "0"

            while queue:
                curr_r, curr_c = queue.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_r, next_c = curr_r + dr, curr_c + dc

                    if (0 <= next_r < rows and
                        0 <= next_c < cols and
                        grid[next_r][next_c] == "1"):
                        grid[next_r][next_c] = "0"
                        queue.append((next_r, next_c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    bfs(r, c)
        
        return island_count