class Solution:
    def dp(self, cache, r, c, s1, s2, s3):
        if min(r,c) < 0:
            return False
        elif cache[r][c] != False:
            return cache[r][c]
        elif r == 0 and c == 0:
            cache[0][0] = True
            return True
        prev = self.dp(cache, r-1, c, s1, s2, s3) or self.dp(cache, r, c-1, s1, s2, s3)
        valid = (s3[r+c-1] == s1[r-1] or s3[r+c-1] == s2[c-1])
        cache[r][c] = valid and prev
        return cache[r][c]


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        if s1 == "":
            return s2 == s3
        elif s2 == "":
            return s1 == s3
        cache = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        self.dp(cache, len(s1), len(s2), s1, s2, s3)
        return cache[-1][-1]
    
        

        