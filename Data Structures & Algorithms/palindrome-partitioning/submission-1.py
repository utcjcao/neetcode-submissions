class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # lets say we know all the partition combos up to i
        # then when we want to add a new character, we check what partions we can make, then combine with all of them

        partitions = [[] for _ in range(len(s))]

        partitions[0] = [[s[0]]]

        for i in range(1, len(s)): # including i 
            for j in range(0, i+1):
                if s[j:i+1] == s[j:i+1][::-1]:
                    # then s[j: i+1] is a partition

                    if j == 0:
                        partitions[i].append([s[j:i+1]])
                    else:

                        for possible in partitions[j-1]:
                            new = possible[::] 
                            new.append(s[j:i+1])
                            partitions[i].append(new)
        
      

        return partitions[-1]


  # for p in partitions[-1]:
        #     p.pop(0)