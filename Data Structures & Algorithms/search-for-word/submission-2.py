class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        ne = [[1,0], [-1,0], [0,-1], [0,1]]
        def search(word, a, b, visited):
            if len(word) == 0:
                return True
            if a == ROWS or b == COLS or min(a,b) < 0:
                return False
            if word[0] == board[a][b]:
                visited.add((a,b))
                for nx, ny in ne:
                    na, nb = a + nx, b + ny
                    if (na,nb) in visited:
                        continue
                    if search(word[1:], na, nb, visited):
                        return True
                visited.remove((a,b))
            else:
                return False
        
        for i in range(ROWS):
            for j in range(COLS):
                if search(word, i, j, set()):
                        return True
                    
        return False
