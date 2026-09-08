class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {i: [] for i in range(n)}
        
        visited = set()
        for edge in edges:
            a, b = edge
            d[a].append(b)
            d[b].append(a)
        print(d)
        total = 0
        def dfs(key):
            nonlocal total
            visited.add(key)
            for val in d[key]:
                if val not in visited:
                    visited.add(val)
                    dfs(val)
            
        for key in d:
            if key not in visited:
                total += 1
                dfs(key)
        return total