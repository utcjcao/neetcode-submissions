class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # input: grid of mxn, with 0, 1, 2
        # output: min number of cycles until all fruit are rotten

        # clarifying qs:
        # how big can the grid be? 1< m ,n <= 10
        # can we wrap around with the grid? no
        # what happens if a fruit is completely isolated? -1

        # 0, 2
        # 0 

        # 0 1 2
        # 1

        # 1 1 2
        # 2

        # 1 0 2
        # -1

        # 2 1 1 1 2
        # 2

        # 1 1 1 1
        # -1

        # 2 2
        # 0 

        # find # of fresh fruit
        # find locations of rotten fruit

        fresh  = 0
        time = 0

        q = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh+=1
                if grid[row][col] == 2:
                    q.append((row, col))
                
        # bfs
        while len(q) > 0:
            if fresh == 0:
                break
            for i in range(len(q)):
                row, col = q.pop(0)
                neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    if not (0 <= nr < len(grid) and 0 <= nc <len(grid[0])):
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
            
            time += 1
        # while len(q)>0
        # iterate through the queue
        # for each item in the queue, 
        # check all of its valid neighbors
        # valid: != 0, in bounds, 1
        # we'll add it  to  the queue
        # immediatelyconvert it to a 2 
        # fresh -= 1
        # time += 1

        # if fresh > 0
        if fresh > 0:
            return -1
        # return -1
        return time
        # return time