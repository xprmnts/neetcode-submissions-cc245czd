class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def bfs(r, c):
            q = collections.deque([(r,c)])
            grid[r][c] = 0
            area = 1

            while q:
                curr_r, curr_c = q.popleft()

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    next_r, next_c = curr_r + dr, curr_c + dc

                    if (0 <= next_r < rows and
                        0 <= next_c < cols and
                        grid[next_r][next_c] == 1):
                            grid[next_r][next_c] = 0
                            q.append((next_r, next_c))
                            area += 1
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island_area = bfs(r,c)
                    max_area = max(max_area, island_area)
        return max_area

                    
        