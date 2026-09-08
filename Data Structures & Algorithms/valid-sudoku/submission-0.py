class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        print('a')
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                if board[j][i] == '.':
                    continue
                if board[j][i] in s:
                    return False
                s.add(board[j][i])
        print('b')
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for a in range(3):
                    for b in range(3):
                        if board[i+a][j+b] == '.':
                            continue
                        if board[i+a][j+b] in s:
                            return False
                        s.add(board[i+a][j+b])
        print('c')
        return True