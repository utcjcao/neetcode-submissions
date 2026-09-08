class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(a, b, v, prev):
            if (a,b) in v:
                return
            if min(a,b) < 0 or a == len(heights) or b == len(heights[0]):
                return
            if heights[a][b] < prev:
                return 
            v.add((a,b))
            dfs(a + 1, b, v, heights[a][b])
            dfs(a - 1, b, v, heights[a][b])
            dfs(a, b + 1, v, heights[a][b])
            dfs(a, b - 1, v, heights[a][b])

        pv = set()
        av = set()
        for i in range(len(heights)):
            dfs(i,0,pv, heights[i][0])
            dfs(i,len(heights[0])-1,av, heights[i][len(heights[0])-1])
            
        for i in range(len(heights[0])):
            dfs(0,i,pv, heights[0][i])
            dfs(len(heights)-1,i,av, heights[len(heights)-1][i])
        
        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in pv and (i,j) in av:
                    ans.append([i,j])
        return ans