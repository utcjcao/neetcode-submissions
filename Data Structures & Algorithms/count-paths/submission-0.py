class Solution:
    def dp(self, cache, r, c, m, n):
        if r == m or c == n:
            return 0
        elif cache[r][c] > 0:
            return cache[r][c]
        elif r == m-1 and c == n-1:
            cache[r][c]=1
            return 1
        cache[r][c] = self.dp(cache, r+1, c, m, n) + self.dp(cache, r, c+1, m, n)
        return cache[r][c]
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0 for i in range(n)] for j in range(m)]
        self.dp(cache, 0, 0, m, n)
        print(cache)
        return cache[0][0]