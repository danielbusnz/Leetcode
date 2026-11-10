class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        copy = [row[:] for row in board]

        for r in range(rows):
            for c in range(cols):
                live = 0

                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if dr == 0 and dc == 0:
                            continue
                         
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < rows and 0 <= nc < cols:
                            live += copy[nr][nc]
                    
                if copy[r][c] == 1:
                    if live < 2 or live> 3:
                        board[r][c] = 0
                else:
                    if live == 3:
                        board[r][c] = 1