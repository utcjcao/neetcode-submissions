class Solution:
    def countSubstrings(self, s: str) -> int:
        l = 0
        ans = [0] * (len(s)+1)
        for r in range(1, len(s)+1):
            l = 0
            while l < r:
                if s[l:r] == s[l:r][::-1]:
            
                    ans[r] += 1
                l+=1
                
            if r > 0: ans[r] += ans[r-1]
        return ans[-1]
            