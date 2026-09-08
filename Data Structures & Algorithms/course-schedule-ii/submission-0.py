class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        start = {i for i in range(numCourses)}
        prereq = {i: [] for i in range(numCourses)}
        postreq = {i: [] for i in range(numCourses)}
        for p in prerequisites:
            if p[0] in start:
                start.remove(p[0])
            prereq[p[1]].append(p[0])
            postreq[p[0]].append(p[1])
        
        while len(start) > 0:
            new_s = set()
            for s in start:
                order.append(s)
                posts = prereq[s]
                for post in posts:
                    if s in postreq[post]:
                        postreq[post].remove(s)
                    if len(postreq[post]) == 0 and post not in start:
                        new_s.add(post)
            start = new_s

        print(order)
        if len(order) == numCourses:
            return order
        return []
        
    