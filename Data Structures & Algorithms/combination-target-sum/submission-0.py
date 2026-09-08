class Solution:
    def helper(self, nums, i, target, used_so_far):
        total = []
        if target == 0:
            return [used_so_far]
        if target < 0 or i >= len(nums):
            return total
        
        a = self.helper(nums, i, target - nums[i], used_so_far + [nums[i]])
        b = self.helper(nums, i+1, target, used_so_far)
        total.extend(a)
        total.extend(b)
        return total

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        all_val = self.helper(nums, 0, target, [])
        return all_val
