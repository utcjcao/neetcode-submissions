"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nl = []
        d = {}
        q = head
        while q:
            nl.append(Node(q.val))
            d[q] = nl[-1]
            q = q.next
        nl.append(None)
        for i in range(len(nl)-1):
            nl[i].next = nl[i+1]
        q = head
        for q in d:
            if q.random is None:
                d[q].random = None
            else:
                d[q].random = d[q.random]
        return nl[0]