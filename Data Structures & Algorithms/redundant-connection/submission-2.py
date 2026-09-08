class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = [[] for _ in range(len(edges) + 1)]
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)

        v = set()
        cS = -1
        cycle = set()
        def mc(par, node):
            nonlocal cS
            if node in v:
                cS = node
                return True

            v.add(node)
            for nei in d[node]:
                if nei == par:
                    continue
                if mc(node, nei):
                    if cS != -1:
                        cycle.add(node)

                    if node == cS:
                        # you return to original node, clear the node cS
                        cS = -1
                    return True
            return False
        mc(-1,1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        return []
            

            