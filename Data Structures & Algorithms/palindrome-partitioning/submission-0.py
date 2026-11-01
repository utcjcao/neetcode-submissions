class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # lets say we know all the partition combos up to i
        # then when we want to add a new character, we check what partions we can make, then combine with all of them

        partitions = [[] for _ in range(len(s)+1)]

        partitions[0] = [[""]]

        for i in range(len(s)): # including i 
            for j in range(0, i+1):
                if s[j:i+1] == s[j:i+1][::-1]:
                    # then s[j: i+1] is a partition

                    for possible in partitions[j]:
                        new = possible[::] 
                        new.append(s[j:i+1])
                        partitions[i+1].append(new)
        
        for p in partitions[-1]:
            p.pop(0)

        return partitions[-1]


