class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap)-1
        while self.heap[i//2] > self.heap[i] and i>1:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        elif len(self.heap) == 2:
            return self.heap.pop()
        else:
            val = self.heap[1]
            self.heap[1] = self.heap.pop()
            self.percolate_down(1)
            return val


    def top(self) -> int:
        if len(self.heap) == 1:
            return -1
        else:
            return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        for num in nums:
            self.heap.append(num)
        cur = len(self.heap)//2 - 1
        while cur > 0:
            i = cur
            self.percolate_down(i)
            cur -= 1
        
    def percolate_down(self, i):
        while 2 * i < len(self.heap):
            if (2*i+1<len(self.heap) and self.heap[2*i+1] < self.heap[2*i] 
            and self.heap[2*i+1] < self.heap[i]):
                self.heap[2*i+1], self.heap[i] = self.heap[i], self.heap[2*i+1]
                i = 2*i+1
            elif (self.heap[2*i] < self.heap[i]):
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2*i
            else:
                break