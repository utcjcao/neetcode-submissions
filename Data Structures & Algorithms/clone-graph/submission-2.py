"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # input: Node | None, will always have starting value 1
        # output: copy of that Node

        # node: integer value, list of its neighboring nodes. 

        # how many nodes can we have? 100
        # is the integer value the unique identifier for each node?
        # are there any self loops? no 
        # can there be cycles? can be cycles

        # 1
        # 1

        # 1-2

        # 1-2-3->1

        if node is None:
            return None
            
        # we have a data structure that maps the node's value to a pointer of the copy of that node
        # dictionary: (val: int, key: node)
        d = {}

        def recurse(node):
            id = node.val
            if id in d:
                return d[id]
            new = Node(id, [])
            d[id] = new
            for neighbor in node.neighbors:
                d[id].neighbors.append(recurse(neighbor))
            return d[id]

        # when we recieve the root node:
        # initially, we'll insert it into our dictionary, with val=1, key= root node copy
        root = Node(1, [])
        d[1] = root

        for neighbor in node.neighbors:
            d[1].neighbors.append(recurse(neighbor))

        return root


        # we'll recurse through the neighbors using dfs. 
        # recurse(id: int) -> node:
        # does the node copy with id already exist?
        # if it exists, we'll modify the current copy.
        # if it doesn't, we'll make a new copy. 
























