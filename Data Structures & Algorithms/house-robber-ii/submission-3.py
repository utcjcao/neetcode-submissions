class Solution:
    def help(self, nums):
        dp1, dp2 = 0, 0
        for n in nums:
            temp = dp2
            dp2 = max(dp2, dp1+n)
            dp1 = temp
        return dp2

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)
        return max(self.help(nums[1:]), self.help(nums[:-1]))