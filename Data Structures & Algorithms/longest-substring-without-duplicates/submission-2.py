class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        l, r = 0,1
        m = 1
        d = {}
        d[s[0]] = 0
        while r < len(s):
            if s[r] in d:
                l = max(l,d[s[r]]+1)
            d[s[r]] = r
            m = max(r-l+1, m)
            print(s[l:r+1], l, r)
            r+=1
        return m