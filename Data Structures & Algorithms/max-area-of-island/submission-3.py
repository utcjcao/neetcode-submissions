class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # input: nxm grid consistenting of either 1 or 0
        # output: max size of an island within the grid

        # grid is empty: 0
        # how large can the grid be: 1 '= 50

        # 1 0
        # 0 0

        # 1 island, 1

        # 1 0
        # 0 1

        # 2 islands, 1

        # 1 0
        # 1 1

        # 1 island, 3

        # 1 0 0 0
        # 1 1 1 1
        # 0 1 0 0
        # 0 1 1 0

        # 1 island, 8

        # iterating through the entire nxm grid, 
        
        # graph traversal algo

        seen = set()
        m = 0

        # dfs algo: input: the location of where we run it from
        # output: the total area of unseen islands that are connected to it
        def dfs(row, col, grid):
            total = 1
            seen.add((row, col))
            neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in neighbors:
                nr, nc = row + dr, col + dc
                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                    continue
                if not ((nr, nc) in seen) and grid[nr][nc] == 1:
                    total += dfs(nr, nc, grid)
            return total

        # we'll iterate through the enitre grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                val = grid[row][col]
                if not ((row, col) in seen) and val == 1:
                    area = dfs(row, col, grid)
                    m = max(m, area)

        # if we come across an island cell that hasn't been seen before
        return m

        # use a seen set to track what we've trveled to before