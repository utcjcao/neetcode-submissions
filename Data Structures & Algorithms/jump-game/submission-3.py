class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums)-1:
            if nums[i] == 0:
                break
            i += max([nums[min(j,len(nums)-1)] + j for j in range(1,nums[i]+1)])
        return i >= len(nums)-1