class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c, dist):
            if r < 0 or r >= ROW or c < 0 or c >= COL:
                return

            if grid[r][c] < dist:
                return

            grid[r][c] = min(grid[r][c], dist)

            dfs(r+1, c, dist+1)
            dfs(r-1, c, dist+1)
            dfs(r, c+1, dist+1)
            dfs(r, c-1, dist+1)

        for x in range(ROW):
            for y in range(COL):
                if grid[x][y] == 0:
                    dfs(x, y, 0)

        