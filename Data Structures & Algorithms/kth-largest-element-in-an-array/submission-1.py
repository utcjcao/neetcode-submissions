class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heapify(nums)
        print(self.heap)
        ans = self.top()
        while k > 0:
            ans = self.pop()
            k -=1
        return ans

    def heapify(self, nums):
        nums.append(nums[0])
        self.heap = nums
        cur = (len(nums)-1)//2
        while cur > 0:
            self.perc_down(cur)
            cur-=1
    
    def top(self):
        return self.heap[1]

    def pop(self):
        if len(self.heap) == 1:
            return -1
        elif len(self.heap) == 2:
            return self.heap.pop()
        else:
            val = self.heap[1]
            self.heap[1] = self.heap.pop()
            self.perc_down(1)
            return val
            
    def perc_down(self, i):
        while i * 2 < len(self.heap):
            if 2*i+1 < len(self.heap) and self.heap[2*i+1] > self.heap[i] and self.heap[2*i+1] > self.heap[2*i]:
                self.heap[2*i+1], self.heap[i] = self.heap[i], self.heap[2*i+1]
                i = 2*i+1
            elif self.heap[2*i] > self.heap[i]:
                self.heap[2*i], self.heap[i] = self.heap[i], self.heap[2*i]
                i = 2*i
            else:
                break
