class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # input is a mxn grid of heights
        # output: [(r, c)]

        # how large is the grid? 100x100, 1z1
        # 0<1000
        # where do we actually start in the grid/ is it any arbitrary cell? yes
        # is it possible there are no answers?  yes

        # 2 3
        # 3 4

        # [0, 1]
        # [1, 0]
        # [1, 1]

        # pacific and the atlantic

        # 4 2 3 1
        # 5 1 2 3
        # 4 3 1 2
        # 2 2 1 3

        # top right and pottom left are always valid
        # bottom left 
        # 4, 2, 3, 5
        # 3, 3

        ans = []
        p_valid = [[False for i in range(len(heights[0]))] for j in range(len(heights))]
        a_valid = [[False for i in range(len(heights[0]))] for j in range(len(heights))]


        # first, we'll mark all cells along the top/left edge as pacific valid
        # mark all cells along the bottom/right edge as atlantic valid

        pq = []
        aq = []

        for i in range(len(heights[0])):
            p_valid[0][i] = True
            pq.append((0,i))
            a_valid[-1][i] = True
            aq.append((len(heights)-1,i))



        for j in range(len(heights)):
            p_valid[j][0] = True
            pq.append((j, 0))
            a_valid[j][-1] = True
            aq.append((j, len(heights[0])-1))

        print("pq", pq)
        print("aq", aq)
        

        while len(pq) > 0:
            print("pq", pq)
            for _ in range(len(pq)):
                row, col = pq.pop(0)
                neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for dr, dc in neighbors:
                    nr, nc = row+dr, col+dc
                    if not (0<=nr<len(heights) and 0<=nc<len(heights[0])):
                        continue
                    if p_valid[nr][nc]:
                        continue
                    if heights[row][col] <= heights[nr][nc]:
                        p_valid[nr][nc] = True
                        pq.append((nr, nc))

        while len(aq) > 0:
            print("aq", aq)
            for _ in range(len(aq)):
                row, col = aq.pop(0)
                neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for dr, dc in neighbors:
                    nr, nc = row+dr, col+dc
                    if not (0<=nr<len(heights) and 0<=nc<len(heights[0])):
                        continue
                    if a_valid[nr][nc]:
                        continue
                    if heights[row][col] <= heights[nr][nc]:
                        a_valid[nr][nc] = True
                        aq.append((nr, nc))
        # we'll iterate through our entire grid from top bottom, left right. if a cell 
        # is marked both atlantic and pacific valid, reachable, append to our answer array

        for row in range(len(heights)):
            for col in range(len(heights[0])):     
                if p_valid[row][col] and a_valid[row][col]:
                    ans.append([row, col])
        return ans

