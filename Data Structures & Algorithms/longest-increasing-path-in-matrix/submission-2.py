import heapq

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = matrix[0][0]

        ROWS, COLS = len(matrix), len(matrix[0])

        dist = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        heap = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                heapq.heappush(heap, (matrix[row][col], row, col))

        ans = 0        
        seen = set()

        # print(heap)

        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while len(heap) > 0:
            val, r, c = heapq.heappop(heap)
            if (r, c) in seen:
                continue
            # print(val)
            seen.add((r, c))
            best = 0
            for dr, dc in d:
                nr, nc = dr + r, dc + c
                if not (0 <= nr < ROWS and 0<= nc < COLS):
                    continue
                if (nr, nc) in seen and matrix[r][c] > matrix[nr][nc]:
                    best = max(best, dist[nr][nc]) 
                else:
                    heapq.heappush(heap, (matrix[nr][nc], nr, nc))

            dist[r][c] = best+1
            ans = max(ans, dist[r][c])

        for row in dist:
            print(row)

        return ans

                
                





