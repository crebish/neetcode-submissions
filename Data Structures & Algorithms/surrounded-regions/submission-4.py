class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL:
                return

            if board[r][c] == "X" or board[r][c] == "I":
                return

            board[r][c] = "I"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        for x in range(ROW):
            if board[x][0] == "O":
                dfs(x, 0)
            if board[x][COL - 1] == "O":
                dfs(x, COL - 1)
        
        for y in range(COL):
            if board[0][y] == "O":
                dfs(0, y)
            if board[ROW - 1][y] == "O":
                dfs(ROW - 1, y)

        for x in range(ROW):
            for y in range(COL):
                if board[x][y] == "O":
                    board[x][y] = "X"
                if board[x][y] == "I":
                    board[x][y] = "O"