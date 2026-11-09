import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # input: square, 250
        # all of the value are unique
        # we can only move horz/vert

        # at least 1x1 in size

        # output: int

    #  grid = [
    #   [0,1,2,10],
    #   [9,14,4,13],
    #   [12,3,8,15],
    #   [11,5,7,6]
    # ]

    # we wanna explore the next cheapest path

    # min heap (val, i, j)


    # 0, 1
    # 2, 3

    # min_heap = [(3, 1, 1)]
    # seen = {(0, 0), (0, 1), (1, 0), (1, 1)}
    # N = 2
    # curr_max = 3

    # curr_val = 3, x = 1, y = 1
    # nx, ny =

        min_heap = []
        seen = set()
        N = len(grid)
        curr_max = 0

        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        seen.add((0, 0))

        while True:
            curr_val, y, x = heapq.heappop(min_heap)

        # while we havent reached the end

        # we'll check what the top of the heap (cheapest path rn)

        # we'll explore it. 
        # we'll add its adjacent members to the heap if we haven't seen them before

            for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_y, new_x = dy+y, dx+x

                if ((new_y, new_x) in seen):
                    continue
                if not (0 <= new_y < N and 0 <= new_x < N):
                    continue

                heapq.heappush(min_heap, (grid[new_y][new_x], new_y, new_x))

                seen.add((new_y, new_x))
            
            if curr_val > curr_max:
                curr_max = curr_val

            if (y, x) == (N-1, N-1):
                break

        return curr_max

        # if curr > curr_max:
        #   curr_max = curr

        # if we have reached (n-1, n-1): break out of this loop

        # we want to maintain what the highest water level needed is so far