class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(board), len(board[0])
        crush_set = set()

        for r in range(ROWS):
            for c in range(COLS - 2):
                if board[r][c] != 0 and abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]):
                    crush_set.update({(r,c), (r, c+1), (r, c+2)})
        
        for r in range(ROWS - 2):
            for c in range(COLS):
                if board[r][c] != 0 and abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]):
                    crush_set.update({(r,c), (r+1,c), (r+2,c)})
        
        if not crush_set:
            return board
        
        for r,c in crush_set:
            board[r][c] = 0
        
        for c in range(COLS):
            stack = [board[r][c] for r in range(ROWS) if board[r][c] != 0]

            for r in range(ROWS - 1, -1, -1):
                board[r][c] = stack.pop() if stack else 0
        
        return self.candyCrush(board)
