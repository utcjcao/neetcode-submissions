class Solution:
    def filler(self, grid, visited, r, c):
        ROWS, COLS = len(grid), len(grid[0])
        if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visited or grid[r][c] == "0"):
            return
        if grid[r][c] == "1":
            visited.add((r,c))
            self.filler(grid, visited, r+1, c)
            self.filler(grid, visited, r-1, c)
            self.filler(grid, visited, r, c+1)
            self.filler(grid, visited, r, c-1)
        return

    def find(self, grid, visited):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count += 1
                    self.filler(grid, visited, i, j)
                visited.add((i,j))
        return count

    def numIslands(self, grid: List[List[str]]) -> int:
        return self.find(grid, set())
        