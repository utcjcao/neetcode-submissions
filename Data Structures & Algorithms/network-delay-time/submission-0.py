import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # keep a time t = 0
        # then inc

        adj = defaultdict(list)

        for source, target, time in times:
            adj[source].append((target, time))

        t = 0
        h = []
        seen = set()

        h.append((0, k))

        # then keep a heap of all nodes we can currently access, map by 
        # (node id, time we can access)

        # base case (k, 0)

        # while heap len > 0
        while len(h) > 0:
            
            access_time, cur = heapq.heappop(h)
            if cur in seen:
                continue
            t = max(t, access_time)
            seen.add(cur)

            for neighbor, time in adj[cur]:
                if neighbor in seen:
                    continue
                
                heapq.heappush(h, (t+time, neighbor))

        return t if len(seen) == n else -1



        # check if current time is past time we can access of top node
        # if yes, continue
        # else, set t = top node time

        # add current node to seen
        
        # go thru all the adj nodes
        # if the node is unvisited, add (node, curtime + edge time) to heap
        

