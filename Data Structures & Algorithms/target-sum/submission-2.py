class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = [{} for i in range(len(nums)+1)]
        ans[0][0] = 1
        for i in range(0, len(nums)):
            for a, c in ans[i].items():
                if a+nums[i] not in ans[i+1]:
                    ans[i+1][a+nums[i]] = 0
                ans[i+1][a+nums[i]] += c
                if a-nums[i] not in ans[i+1]:
                    ans[i+1][a-nums[i]] = 0
                ans[i+1][a-nums[i]] += c
        return ans[len(nums)].get(target, 0)
    
