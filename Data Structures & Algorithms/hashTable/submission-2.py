class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = [None] * capacity

    def hash(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        newNode = Node(key, value)
        if self.map[index] is None:
            self.map[index] = newNode 
            self.size += 1
            if self.size >= self.capacity // 2:
                self.resize()
            return
        else:
            prev, cur = None, self.map[index]
            while cur is not None:
                if cur.key == key:
                    cur.key, cur.val = key, value
                    return 
                prev, cur = cur, cur.next
            prev.next = newNode
            newNode.prev = prev
            self.size += 1
            if self.size >= self.capacity // 2:
                self.resize()


    def get(self, key: int) -> int:
        index = self.hash(key)
        node = self.map[index]
        while node is not None:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def resize(self) -> None:
        self.capacity *= 2
        newMap = [None] * self.capacity

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for node in oldMap:
            while node is not None:
                self.insert(node.key, node.val)
                node = node.next

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        last, cur = None, self.map[index]
        if not cur:
            return False
        if not last and not cur.next:
            self.map[index] = None
        while cur is not None:
            if cur.key == key:
                if last:
                    last.next = cur.next
                elif cur.next:
                    cur.next.prev = last
                self.size -= 1
                return True
            else:
                last = cur
                cur = cur.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
