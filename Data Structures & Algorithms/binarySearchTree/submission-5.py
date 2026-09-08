class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new = Node(key, val)
        if self.root is None:
            self.root = new
        elif self.root.key == key:
            self.root.val = val
        else:
            curr = self.root
            while True:
                if curr.key > key:
                    if curr.left == None:
                        curr.left = new
                        return
                    curr = curr.left
                else:
                    if curr.right == None:
                        curr.right = new
                        return
                    curr = curr.right
        return None            
            

    def get(self, key: int) -> int:
        curr = self.root
        while curr is not None:
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left
            else:
                return curr.val
        return -1            

    def getMin(self) -> int:
        if self.root is None:
            return -1
        else:
            curr = self.root
            while curr.left is not None:
                curr = curr.left
            return curr.val

    def getMax(self) -> int:
        if self.root is None:
            return -1
        else:
            curr = self.root
            while curr.right is not None:
                curr = curr.right
            return curr.val

    def removeHelper(self, curr, key):
        if curr is None: return

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left is None:
                return curr.right
            elif curr.right is None:
                return curr.left
            else:
                pointer = curr.right
                while pointer.right is not None:
                    pointer = pointer.left
                curr.key, curr.val = pointer.key, pointer.val
                curr.right = self.removeHelper(curr.right, pointer.key)
        return curr

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)   
        return None 


    def getInorderKeys(self) -> List[int]:
        return self.getKeysHelper(self.root)

    def getKeysHelper(self, curr):
        if curr != None:
            key_list = []
            key_list += self.getKeysHelper(curr.left)  
            key_list += [curr.key]
            key_list += self.getKeysHelper(curr.right)
            return key_list
        return []
