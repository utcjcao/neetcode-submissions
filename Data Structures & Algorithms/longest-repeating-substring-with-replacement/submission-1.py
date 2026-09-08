class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        m = 0
        d = {}
        for r in range(len(s)):
            if s[r] not in d:
                d[s[r]] = 0
            d[s[r]] += 1
            # condition to check if number of unlike characters > k
            while ((r-l+1)-max([d[i] for i in d]) > k):
                d[s[l]] -= 1
                l += 1
            # we check for max here b/c atthis point we know the
            # condition is true
            m = max(m, r-l+1)
            print(d)

        return m
