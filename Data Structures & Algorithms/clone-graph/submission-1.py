"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        q = deque()
        q.append(node)
        adjList = {}
        while len(q) > 0:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.val not in adjList:
                    new_n = Node(cur.val)
                    adjList[cur.val] = new_n
                for ne in cur.neighbors:
                    if ne.val not in adjList:
                        ne_node = Node(ne.val)
                        adjList[ne.val] = ne_node
                        q.append(ne)
                    adjList[cur.val].neighbors.append(adjList[ne.val])

                        # adjList[ne.val].neighbors.append(adjList[cur.val])
                        

                    
        return adjList[node.val]
        
        
        