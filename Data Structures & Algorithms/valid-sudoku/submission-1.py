class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input: 9x9 array of characters
        # output: boolean

        # we use a set for each row/col, and insert each elem in the set if its nonempty
        # if the elem already exists, then we know a duplicate has occured, so we return
        # false

        # row/col
        # iterate through the rows/cols
        # use a set to find duplicates
        # row
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # col
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # we would iterate through a 3x3 2d for loop
        # iterate through the 3x3 space within each i, j subbox
        for i in range(3):
            for j in range(3):
                seen = set()
                for x in range(3):
                    for y in range(3):
                        row = i * 3 + x
                        col = j * 3 + y
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])
        
        return True

