class KthLargest:
    # how does heap work again? i forgot
    # the idea is that a value points the 2i and 2i+1 index
    # such that they are both less/greater than that number
    
    # to add elements: add it as a leaf. if its bigger/smaller
    # than its parent, switch positions. (might be sm else here)

    # 1: 2, 3
    # 2: 4, 5
    # 3: 6, 7
    # 4: 8, 9
    # 5:
    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k
        for n in nums:
            self.heap.append(n) 
            i = len(self.heap)-1
            while i > 1 and self.heap[i//2] > self.heap[i]:
                self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
                i = i//2
            while len(self.heap) > self.k+1:
                self.pop()
        print(self.heap)

    def add(self, val: int) -> int:
        self.heap.append(val)
        i = len(self.heap)-1
        while i > 1 and self.heap[i//2] > self.heap[i]:
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i//2
        while len(self.heap) > self.k + 1:
            self.pop()
        return self.heap[1]

    def pop(self):
        if len(self.heap) == 1:
            return
        if len(self.heap) == 2:
            return self.heap.pop()
        
        original = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2*i < len(self.heap):
            if (2*i+1 < len(self.heap) and self.heap[2*i+1] < self.heap[i] and self.heap[2*i+1] < self.heap[2*i]):
                self.heap[2*i+1], self.heap[i] = self.heap[i], self.heap[2*i+1]
                i = 2*i+1
            elif self.heap[2*i] < self.heap[i]:
                self.heap[2*i], self.heap[i] = self.heap[i], self.heap[2*i]
                i = 2*i
            else:
                break
        return original

        
        