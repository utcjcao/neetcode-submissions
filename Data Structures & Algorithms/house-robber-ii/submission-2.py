class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)
        ans = []
        n = len(nums)
        for i in range(len(nums)):
            dp1, dp2 = 0, 0
            counter, ind = 0, i
            while counter < n-1:
                if ind == n:
                    ind=0
                temp = dp2
                dp2 = max(dp2, dp1+nums[ind])
                dp1 = temp
                ind+=1
                counter += 1
            ans.append(dp2)
        return max(ans)