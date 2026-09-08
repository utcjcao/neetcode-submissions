class Solution:
    def filler(self, grid, visited, i, j):
        ROWS, COLS = len(grid), len(grid[0])
        if min(i,j) < 0 or i == ROWS or j == COLS:
            return 0
        elif grid[i][j] == 0 or (i,j) in visited:
            return 0
        count = 1
        visited.add((i,j))
        count += self.filler(grid, visited, i+1, j)
        count += self.filler(grid, visited, i-1, j)
        count += self.filler(grid, visited, i, j+1)
        count += self.filler(grid, visited, i, j-1)
        return count
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    count = max(count, self.filler(grid, visited, i, j))
        return count
        