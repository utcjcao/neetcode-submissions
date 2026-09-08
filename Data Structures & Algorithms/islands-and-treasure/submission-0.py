class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        count = 1
        neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
        print(q)
        while len(q) > 0:
            for i in range(len(q)):
                x,y = q.popleft()
                for a,b in neighbors:
                    nx, ny = x+a, y+b
                    if min(nx,ny) < 0 or nx == len(grid) or ny == len(grid[0]) or grid[nx][ny] == -1:
                        continue
                    if grid[nx][ny] == 2147483647:
                        grid[nx][ny] = count
                        q.append((nx, ny))
            count += 1 
                
