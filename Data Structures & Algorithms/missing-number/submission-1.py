class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        q = 1
        for n in range(1,len(nums)+1):
            q *= n
        zFlag = False
        for n in nums:
            if n == 0:
                zFlag = True
            else:
                q = q//n
        if zFlag is False:
            return 0
        return q
