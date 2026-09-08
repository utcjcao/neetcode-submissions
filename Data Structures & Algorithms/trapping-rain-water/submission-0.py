class Solution:
    def trap(self, height: List[int]) -> int:
        # how do i get the water amount at a specific location?
        # i find the max heights from left to right it seems, minus the 
        # bottom amount
        # can i do this with a prefix/suffix?
        ml = [0] * (len(height)+1)
        mr = [0] * (len(height)+1)
        # imagine that the zeros are just before the heights start
        for i in range(len(height)):
            ml[i+1] = max(ml[i], height[i])
        for i in range(len(height)-1, -1, -1):
            mr[i] = max(mr[i+1], height[i])
        print(ml)
        print(mr)
        
        total = 0
        for i in range(len(height)):
            lm = ml[i]
            rm = mr[i+1]
            if (height[i] >= min(lm, rm)):
                continue
            else:
                total += min(lm, rm) - height[i]
        return total
