class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.distance = {}
        self.heapify(points)
        print(self.heap)
        answer = []
        while len(answer) < k:
            answer.append(self.pop())
        return answer

    def calc_dist(self, val):
        print(val[0], val[1], math.sqrt((val[0])**2 + (val[1])**2))
        return math.sqrt((val[0])**2 + (val[1])**2)

    def string_hash(self, val):
        return str(val[0]) + "_" + str(val[1])

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]   
        # Move last value to root
        self.heap[1] = self.heap.pop()
        i = 1
        # Percolate down
        while 2 * i < len(self.heap):
            parent_key = self.string_hash(self.heap[i])
            first_key = self.string_hash(self.heap[2 * i])
            
            if (2 * i + 1 < len(self.heap)):
                second_key = self.string_hash(self.heap[2 * i + 1])
                if self.distance[second_key] < self.distance[first_key] and self.distance[parent_key] > self.distance[second_key]:
                    # Swap right child
                    self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                    i = 2 * i + 1
                    continue
            if self.distance[parent_key] > self.distance[first_key]:
                # Swap left child
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2 * i
            else:
                break
            
        return res

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def heapify(self, arr):
        # 0-th position is moved to the end
        for val in arr:
            key = self.string_hash(val) 
            self.distance[key] = self.calc_dist(val)
            print(key, self.distance[key])
        arr.append(arr[0])
        
            
        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # Percolate down
            i = cur
            while 2 * i < len(self.heap):
                
                parent_key = self.string_hash(self.heap[i])
                first_key = self.string_hash(self.heap[2 * i])

                print(self.distance[parent_key])
                
                if (2 * i + 1 < len(self.heap)):
                    second_key = self.string_hash(self.heap[2 * i + 1])
                    if self.distance[second_key] < self.distance[first_key] and self.distance[parent_key] > self.distance[second_key]:
                        # Swap right child
                        self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                        i = 2 * i + 1
                        continue
                if self.distance[parent_key] > self.distance[first_key]:
                    # Swap left child
                    self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                    i = 2 * i
                    
                else:
                    print('swap')
                    break
            cur -= 1