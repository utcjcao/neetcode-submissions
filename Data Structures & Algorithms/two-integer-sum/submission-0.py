class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        con = {}
        for i in range(len(nums)):
            if (target-nums[i] in con):
                return [con[target-nums[i]], i]
            else:
                con[nums[i]] = i