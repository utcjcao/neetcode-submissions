# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        print([(pair.key, pair.value) for pair in pairs])
        if len(pairs) <= 1:
            return pairs
        
        pivot = pairs[-1].key
        left = -1
        for i in range(len(pairs)-1):
            if pairs[i].key < pivot:
                left += 1
                pairs[i], pairs[left] = pairs[left], pairs[i]
                
        
        pairs[-1], pairs[left+1] = pairs[left+1], pairs[-1]
        print([(pair.key, pair.value) for pair in pairs], 'after pivot swap')

        

        

        return self.quickSort(pairs[0:left+1]) + [pairs[left+1]] + self.quickSort(pairs[left+2:])