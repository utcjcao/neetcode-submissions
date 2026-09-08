class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heapify(stones)
        while len(self.heap)>2:
            top_rock = self.pop()
            next_rock = self.pop()
            print(top_rock, next_rock)
            if top_rock != next_rock:
                new_rock = max(top_rock, next_rock) - min(top_rock, next_rock)
                self.push(new_rock)
        
        if len(self.heap) == 1:
            return 0
        if len(self.heap) == 2:
            return self.top()

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap)-1
        while i > 1 and self.heap[i] > self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def top(self):
        if len(self.heap) == 1:
            return -1
        else:
            return self.heap[1]

    def pop(self):
        if len(self.heap) == 1:
            return -1
        elif len(self.heap) == 2:
            return self.heap.pop()
        else:
            val = self.heap[1]
            self.heap[1] = self.heap.pop()
            self.perc_down(1);
            return val

    def heapify(self, arr):
        self.heap = [0] + arr
        curr = len(self.heap)-1//2
        while curr>0:
            self.perc_down(curr)
            curr -= 1


    def perc_down(self, i):
        while 2*i < len(self.heap):
            if 2*i+1 < len(self.heap) and self.heap[i] < self.heap[2*i+1] and self.heap[2*i+1] > self.heap[2*i]:
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i=2*i+1
            elif self.heap[i] < self.heap[2*i]:
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i=2*i
            else:
                break

