class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        q = deque()
        v = set()
        ROWS, COLS = len(grid), len(grid[0])
        v.add((0,0))
        q.append((0,0))
        length = 0
        while len(q) > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return length
                nbs = [[1,0], [-1,0], [0,1], [0,-1]]
                for nr, nc in nbs:
                    if (min(r+nr,c+nc) < 0 or
                    r +nr == ROWS or c+nc == COLS  or
                    grid[r+nr][c+nc] == 1 or
                    (r+nr,c+nc) in v):
                        continue
                    q.append((r+nr, c+nc))
                    v.add((r+nr, c+nc))
            length += 1
        return -1