class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot = set()
        total_fruit = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rot.add((i,j))
                if grid[i][j] == 1 or grid[i][j] == 2:
                    total_fruit += 1
        ROWS, COLS = len(grid), len(grid[0])
        ne = [[0,1], [0,-1], [1,0], [-1,0]]
        time = 0
        q = deque()
        for r in rot:
            q.append(r)
        print(total_fruit)
        while len(q) > 0:
            print(len(q))
            if len(rot) == total_fruit:
                break
            for i in range(len(q)):
                r, c = q.popleft()
                for nr, nc in ne:
                    new_r, new_c = r+nr, c+nc
                    if (min(new_r, new_c) < 0 or new_r == ROWS
                    or new_c == COLS or grid[new_r][new_c] == 0 
                    or (new_r, new_c) in rot):
                        continue
                    rot.add((new_r,new_c))
                    q.append((new_r,new_c))                
            time += 1
        if len(rot) == total_fruit:
            return time
        else:
            return -1      
