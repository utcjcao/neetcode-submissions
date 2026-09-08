class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    # input will be a mxn grid, with -1, 0, INF
    # output will be the same mxn grid, with the land cell values replaced 
    # with the min distance to a treasure chest

    # how large and how small can our grid be? 1<= 100
    # can the grid be empty?
    # which directions can we go? lrup

    # -1 0
    # INF -1

    # INF 0
    # 1 0

    # 0 INF INF INF 0
    # 0 1 2 1 0

    # 0 INF INF -1 0
    # INF INF INF INF INF

    # 0 1 2 -1 0
    # 1 2 3 2 1

    # INF -1 0 INF
    # INF INF INF -1
    # INF -1 INF -1
    # 0 -1 INF INF

    # 3 -1 0 1
    # 2 2 1 -1
    # 1 -1 2 -1
    # 0 -1 3 4

    # [[4,-1,0,1],
    # [3,2,1,-1],
    # [1,-1,2,-1],
    # [0,-1,3,4]]

    # we want to collect all the locations of our treasure chest

        queue = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))

        counter = 0

        seen = set()
        for item in queue:
            seen.add(item)

        while len(queue) > 0:
            new = []
            for row, col in queue:
                grid[row][col] = counter
                neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    if not (0<= nr < len(grid) and 0<= nc < len(grid[0])):
                        continue
                    if (nr, nc) in seen:
                        continue
                    if grid[nr][nc] == -1:
                        continue
                    if grid[nr][nc] != 2147483647:
                        continue
                    seen.add((nr, nc))
                    new.append((nr, nc))
            queue = new
            counter += 1

        
                    

        # we want to define our bfs algo
        # queue = treasure
        # counter = 0
        # while queue > 0:
        # for every item in the queue:
        # mark its location with counter
        # look at all its valid neighbors (unseen and within bounds and not water)
        # append it to our queue
        # ignore
        # counter += 1

        # bfs (treasure)

    
