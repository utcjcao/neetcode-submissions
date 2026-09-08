class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ne = [(0,1), (0,-1), (1,0), (-1,0)]
        R, C = len(board), len(board[0])
        g = set()
        q = deque()
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    if i == 0 or j == 0 or i == R-1 or j == C-1:
                        g.add((i,j))
                        q.append((i,j))
        while len(q) > 0:
            i, j = q.popleft()
            for a, b in ne:
                ni, nj = i+a, j+b
                if min(ni, nj) < 0 or ni == R or nj == C:
                    continue
                if board[ni][nj] == 'O' and (ni,nj) not in g:
                    q.append((ni,nj))
                    g.add((ni,nj))
        for i in range(R):
            for j in range(C):
                if (i,j) in g:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        

                    

