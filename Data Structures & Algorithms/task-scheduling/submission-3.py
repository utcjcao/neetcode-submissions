from collections import Counter, defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        total = len(tasks)

        count = Counter(tasks)
        d = defaultdict(list)

        h = []
        for key, amt in count.items():
            heapq.heappush(h, (-1 * amt))

        t = 0
        while total > 0:
            for elem in d[t]:
                heapq.heappush(h, elem)
            if len(h) > 0:
                amt = heapq.heappop(h)
                amt += 1
                if amt < 0:
                    d[t + n + 1].append(amt)
                total -= 1
            t += 1
        return t
        
