class Solution:
    def gridDFS(self, grid, r, c, visit):
        ROW, COL = len(grid), len(grid[0])
        if min(r,c)< 0 or r == ROW or c == COL or (r,c) in visit or grid[r][c] == 1:
            return 0
        if r == ROW-1 and c == COL-1:
            return 1
        count = 0
        visit.add((r,c))
        count += self.gridDFS(grid, r-1, c, visit)
        count += self.gridDFS(grid, r+1, c, visit)
        count += self.gridDFS(grid, r, c-1, visit)
        count += self.gridDFS(grid, r, c+1, visit)
        visit.remove((r,c))
        return count
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.gridDFS(grid, 0, 0, set())
        