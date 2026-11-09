class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # we just find the first zero
        # we set that row and column to be zero

        sr, sc = -1, -1

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if matrix[i][j] == 0:
                    sr, sc = i,j
                    break
        if sr == -1 and sc == -1:
            return

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if matrix[i][j] == 0:
                    matrix[sr][j] = 0
                    matrix[i][sc] = 0

        R, C = len(matrix), len(matrix[0])

        for i in range(R):
            val = matrix[i][sc]
            if i == sr:
                continue
            if val == 0:
                for a in range(C):
                    matrix[i][a] = 0
                
        for target_col in range(C):
            if target_col == sc:
                continue
            if matrix[sr][target_col] == 0:
                for a in range(R):
                    matrix[a][target_col] = 0

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if i == sr or j == sc:
                    matrix[i][j] = 0


        

        # we'll store that row and col index
        # if we see a zero as we set it to zero, we'll set it to 1

        # we treat that row and col as our bool array

        # we check the rest, set that row col respectively




        