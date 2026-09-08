import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        out = []
        for i in range(len(nums)):
            heapq.heappush(h, (-nums[i], i))
            if(i>=k-1):
                while h[0][1] <= i-k:
                    q = heapq.heappop(h)
                print(h)
                out.append(-h[0][0])
        return out
