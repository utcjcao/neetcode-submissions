class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(a, b):
            if a == n and b == n:
                return [""]
            ans = []
            if a < n:
                for g in dfs(a+1, b):
                    ans.append("(" + g)
            if b < n and a > b:
                for g in dfs(a, b+1):
                    ans.append(")"+ g )
            return ans
        return dfs(0, 0)