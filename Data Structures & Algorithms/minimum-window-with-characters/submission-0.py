class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = float("inf")
        ans = ""
        d= {}
        for c in t:
            d[c] = d.get(c,0) + 1
        n = {}
        prev, total = 0, 0
        for i in range(len(s)):
            # when do i start increasing my prev pointr
            # and for how long?
            n[s[i]] = n.get(s[i], 0) + 1
            if s[i] in d and n[s[i]] <= d[s[i]]:
                total += 1
            if (total == len(t)):
                while (n[s[prev]] > d.get(s[prev], 0)):
                    n[s[prev]] -=  1
                    prev += 1
                if len(s[prev:i+1]) < m:
                    m = len(s[prev:i+1])
                    ans = s[prev:i+1]
                n[s[prev]] -= 1
                prev += 1
                total -= 1
        return ans  