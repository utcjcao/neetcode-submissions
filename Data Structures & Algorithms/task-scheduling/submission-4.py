from collections import Counter, defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        total = len(tasks)

        count = Counter(tasks)
        d = defaultdict(list)

        available = []
        cooldown = []
        for key, amt in count.items():
            heapq.heappush(available, (-1 * amt))

        t = 0
        while len(available) > 0 or len(cooldown) > 0:
            while len(cooldown)>0 and cooldown[0][0] <= t:
                _, amt = heapq.heappop(cooldown)
                heapq.heappush(available, amt)

            if len(available) > 0:
                amt = heapq.heappop(available)
                amt += 1
                if amt < 0:
                    heapq.heappush(cooldown, (t + n + 1, amt))

                t += 1
            else:
                t = cooldown[0][0]
        
        return t
        
