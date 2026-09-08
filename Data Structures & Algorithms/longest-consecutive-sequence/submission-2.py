class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        q = set(nums)
        m = 0
        for n in q:
            if n-1 not in q:
                length = 1
                while n+length in q:
                    length += 1
                m = max(m, length)
        return m