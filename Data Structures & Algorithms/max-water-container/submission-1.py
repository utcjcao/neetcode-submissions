class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a, b = 0, len(heights)-1
        m = (b-a) * min(heights[a], heights[b])
        while a < b:
            if heights[a] < heights[b]:
                a += 1
            else:
                b -= 1
            m = max(m, (b-a) * min(heights[a], heights[b])) 
        return m