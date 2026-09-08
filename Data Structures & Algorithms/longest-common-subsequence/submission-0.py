class Solution:
    def dp(self, cache, r, c, t1, t2):
        cA, cB = t1[r], t2[c]
        if min(r,c) < 0:
            return 0
        elif cache[r][c] > 0:
            return cache[r][c]
        if cA == cB:
            cache[r][c] = self.dp(cache, r-1 , c-1, t1, t2) + 1
        else:
            cache[r][c] = max(self.dp(cache, r, c-1, t1, t2), 
            self.dp(cache, r-1 , c, t1, t2))
        return cache[r][c]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[0 for i in range(len(text2))] for i in range(len(text1))]
        
        self.dp(cache, len(text1)-1 , len(text2)-1, text1, text2)
        print(cache)        
        return cache[-1][-1]
                