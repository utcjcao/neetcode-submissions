class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input: 9x9 array of characters
        # output: boolean

        # we use a set for each row/col, and insert each elem in the set if its nonempty
        # if the elem already exists, then we know a duplicate has occured, so we return
        # false


        r = {i: [] for i in range(9)}
        c = {i: [] for i in range(9)}
        s = {(i,j): [] for i in range(3) for j in range(3)}


        # row/col
        # iterate through the rows/cols
        # use a set to find duplicates
        # row
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in r[row]:
                    return False
                r[row].append(board[row][col])
                if board[row][col] in c[col]:
                    return False
                c[col].append(board[row][col])
                if board[row][col] in s[(row//3, col//3)]:
                    return False
                s[(row//3, col//3)].append(board[row][col])

        return True

