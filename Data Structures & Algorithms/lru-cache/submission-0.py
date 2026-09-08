class Node:
    def __init__(self, key, val):
        self.prev = self.next = None
        self.key, self.val = key, val

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.m:
            self.remove(self.m[key])
            self.insert(self.m[key])
            return self.m[key].val
        else:
            return -1

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.remove(self.m[key])
        self.m[key] = Node(key, value)
        self.insert(self.m[key])

        if len(self.m) > self.capacity:
            leftmost = self.left.next
            self.remove(leftmost)
            del self.m[leftmost.key]

        
