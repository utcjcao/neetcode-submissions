class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = {i for i in range(len(nums)+1)}
        for n in nums:
            s.remove(n)
        return s.pop()