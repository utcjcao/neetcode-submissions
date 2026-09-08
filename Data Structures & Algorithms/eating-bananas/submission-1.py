class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bottom, top = 1, max(piles)
        best_k_so_far = top
        while top >= bottom:
            mid = (bottom+top)//2
            hour_counter = 0
            for pile in piles:
                hour_counter += math.ceil(pile/mid)
            if hour_counter > h:
                bottom = mid + 1
            else:
                best_k_so_far = min(best_k_so_far, mid)
                top = mid - 1 
            
        return best_k_so_far
            