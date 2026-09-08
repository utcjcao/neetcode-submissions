class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a, b = {}, {}
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]] = 0
            a[s[i]] += 1
            if t[i] not in b:
                b[t[i]] = 0
            b[t[i]] += 1
        return a == b

