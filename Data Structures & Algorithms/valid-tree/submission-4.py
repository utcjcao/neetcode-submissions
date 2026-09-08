class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = {i:[] for i in range(n)}
        for a,b in edges:
            if a == b:
                return False
            g[a].append(b)
            g[b].append(a)
        print(g)
        visited = set()
        def dfs(cur, prev):
            visited.add(cur)
            for node in g[cur]:
                if node not in visited: 
                    dfs(node, cur)
                elif node != prev: 
                    print(node, cur, visited)
                    return False
        
        if dfs(0, 0) is False: return False
        print(len(visited))
        return len(visited) == n