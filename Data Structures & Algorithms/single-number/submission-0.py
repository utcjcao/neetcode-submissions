class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        for n in s:
            return n