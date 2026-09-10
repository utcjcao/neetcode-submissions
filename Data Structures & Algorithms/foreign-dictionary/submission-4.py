from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # iterate downwards, 
        # if equal, then it doesnt give us any info
        #  if not equal, and characters havent been connected, create an edge in the graph
        # if we eventaully reach end of one of the strings
        # if front string is longer, return false early
        # else continue

        d = defaultdict(set)
        freq = defaultdict(int)
        seen = set()

        for i in range(len(words)):
            for c in words[i]:
                seen.add(c)
        
        for i in range(1, len(words)):
            first, second = words[i-1], words[i]
            if (len(first) > len(second) and first.startswith(second)):
                return ""
            for i in range(min(len(first), len(second))):
                if (first[i] == second[i]):
                    continue
                if (second[i] not in d[first[i]]):
                    d[first[i]].add(second[i])
                    freq[second[i]]+=1
                break

                

        ans = ""
        q = deque()
        for c in seen:
            print(c, freq[c])
            if (freq[c] == 0):
                ans += c
                q.append(c)
        
        while (len(q) > 0):
            cur = q.pop()
            for c in d[cur]:
                freq[c]-=1
                if (freq[c] == 0 and c not in ans):
                    ans += c
                    q.append(c)

        if (len(ans) == len(freq)):
            return ans
        print(ans)
        return ""
        


