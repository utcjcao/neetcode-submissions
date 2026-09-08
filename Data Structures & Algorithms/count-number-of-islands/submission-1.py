class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # input: group of 1s and 0s
        # output: integer representing the number of islands

        # 2d grid is empty: 0 
        # diagonal does not count as one island
        # dims are 1 to 100

        # 1 0
        # 0 1

        # 2 islands

        # 1 1
        # 1 0

        # 1 island

        # 1 0 0
        # 1 1 1
        # 0 0 1

        # 1 island

        # 1 0 0
        # 0 0 0 
        # 0 0 1

        # 2 islands


        # o n^2 time complexity, n^2 space complexity
        # as we iterate through the nxm grid, 
        # if we find a 1, we check if its neighbor has been seen before
        # set: we can track the land grid cells we've seen before, and if the neighbor
        # is in this set, then we know we've already been to this distinct island
        # if it has, then we dont need to increment the # of islands we have
        # if it hasnt, we know that we have a new island.

        # 1 1
        # 0 1
        # 1 1 


        seen = set()

        island_count = 0

        def dfs(row, col, grid):
            seen.add((row, col))
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                nr, nc = row+dr, col + dc
                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                    continue
                if grid[nr][nc] == '1' and (nr, nc) not in seen:
                    dfs(nr, nc, grid)

        # iterate through our grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in seen:
                    dfs(row, col, grid)
                    island_count += 1
        # if we see an island that hasn't been in our seen set
        # we'll run our dfs algo, and add each new island cell to our seen set
        # once we're finished, we'll increment our island count by one. 

        return island_count







