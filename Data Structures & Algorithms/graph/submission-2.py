class Graph:
    
    def __init__(self):
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = []
        if dst not in self.adj:
            self.adj[dst] = []
        self.adj[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj or dst not in self.adj[src]:
            return False
        self.adj[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        q = deque()
        v = set()
        q.append(src)
        v.add(src)

        while len(q) > 0:
            for i in range(len(q)):
                cur = q.popleft()
                print(cur)
                if cur == dst: return True
                v.add(cur)
                for ne in self.adj[cur]:
                    if ne not in v:
                        q.append(ne)
        return False
                
