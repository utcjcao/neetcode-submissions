import heapq

class MedianFinder:

    def __init__(self):
        self.smaller, self.larger = [], []

    def addNum(self, num: int) -> None:
        if (len(self.smaller) == 0):
            self.smaller.append(num*-1)
            return

        if (self.smaller[0]*-1 >= num):
            heapq.heappush(self.smaller, num*-1)
        else:
            heapq.heappush(self.larger, num)
        
        if ((len(self.larger)-len(self.smaller)) >= 2):
            smallest = heapq.heappop(self.larger)
            heapq.heappush(self.smaller, smallest * -1)
        if ((len(self.smaller)-len(self.larger)) >= 2):
            largest = heapq.heappop(self.smaller)
            heapq.heappush(self.larger, largest * -1)
        
        
    def findMedian(self) -> float:
        # print(self.smaller)
        # print(self.larger)
        if (len(self.smaller) > len(self.larger)):
            
            return self.smaller[0] *-1
        elif (len(self.larger) > len(self.smaller)):
            return self.larger[0]
        else:
            return (self.larger[0] + self.smaller[0] *-1)/2
        
        
        