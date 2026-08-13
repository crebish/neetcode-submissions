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
            for y in range(COL):
                if x == 0 or y == 0 or x == ROW - 1 or y == COL - 1:
                    dfs(x, y)

        for x in range(ROW):
            for y in range(COL):
                if board[x][y] == "O":
                    board[x][y] = "X"

        for x in range(ROW):
            for y in range(COL):
                if board[x][y] == "I":
                    board[x][y] = "O"