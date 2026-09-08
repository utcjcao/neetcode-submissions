class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        s = set()
        na, nb, nc = target
        for t in triplets:
            a, b, c = t
            if (a > na or b > nb or c > nc):
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    s.add(i)
        return len(s) == 3
            
        
