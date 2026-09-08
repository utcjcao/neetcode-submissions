class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        pre = {i for i in range(numCourses)}
        for p in prerequisites:
            a, b = p
            if a in pre: pre.remove(a)
            if b not in adjList:
                adjList[b] = []
            adjList[b].append(a)
        if len(pre) == 0:
            return False
        visited = set()
        while len(pre) > 0:
            cur_p = pre.pop()
            if cur_p not in visited:
                visited.add(cur_p)
                queue = deque()
                queue.append(cur_p)
                print(queue)
                while len(queue) > 0:
                    for i in range(len(queue)):
                        curr = queue.popleft()
                        if curr not in adjList:
                            continue
                        for neighbor in adjList[curr]:
                            if neighbor in adjList:
                                if curr in adjList[neighbor]:
                                    return False
                            if neighbor not in visited:
                                visited.add(neighbor)
                                queue.append(neighbor)
        return len(visited) == numCourses

                