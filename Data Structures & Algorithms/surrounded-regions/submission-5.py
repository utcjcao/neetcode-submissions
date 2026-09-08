class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # input: grid of X/O char
        # output: grid modified in place to convert surrounded O characters to X characters

        # if its on the border, is it surrounded? no
        # does it have to be more than one O? no
        # if the O is not touching the border, its surrounded. true

        # o
        # x

        # x o o o x
        # x o o o x

        # x o o
        # x o o
        # x x x

        # x x x x
        # x o o x
        # x x x x
        # x o o x

        # x x x x
        # x x x x
        # x x x x
        # x o o x

        # identify all border o

        seen = set()
        q = deque()

        for i in range(len(board)):
            if board[i][0] == 'O':
                q.append((i, 0))
                seen.add((i, 0))

            if board[i][-1] == 'O':
                q.append((i, len(board[0])-1))

                seen.add((i, len(board[0])-1))

        for i in range(len(board[0])):
            if board[0][i] == 'O':
                q.append((0, i))

                seen.add((0, i))
            if board[-1][i] == 'O':
                q.append((len(board)-1, i))

                seen.add((len(board)-1, i))

        while len(q) > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    if not (0 <= nr < len(board) and 0 <= nc < len(board[0])):
                        continue
                    if (nr, nc) in seen:
                        continue
                    if board[nr][nc] != 'O':
                        continue
                    seen.add((nr, nc))
                    q.append((nr, nc))


        # run a graph traversal algorithm to see if we can reach any other os starting from our border os
        # seen() -> contain all visited and therefore unsurrounded os 
        # dfs(loc):
        # check all of our neighbors
        # if our neighbor is an o, we'll add it to our seen
        # dfs()

        for row in range(len(board)):
            for col in range(len(board[0])):
                board[row][col] = 'X'
            
        for row, col in seen:
            board[row][col] = 'O'

        # convert the entire board to x. 
        # for all os in seen, we can convert the grid locaitons back to o


