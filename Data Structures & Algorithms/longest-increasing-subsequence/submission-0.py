class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = {}
        ans = 0
        for n in nums:
            c = 1
            for e in d:
                if e < n:
                    c = max(d[e]+1,c)
            d[n] = c
            ans = max(ans, d[n])
        print(d)
        return ans
