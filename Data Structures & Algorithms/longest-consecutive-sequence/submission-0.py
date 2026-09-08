class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        q = set(nums)
        m = 0
        for k in q:
            if k - 1 not in q:
                l = 1
                while (k+l) in q:
                    l += 1
                m = max(m, l)
        return m