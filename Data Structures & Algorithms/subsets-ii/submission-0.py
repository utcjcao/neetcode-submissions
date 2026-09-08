class Solution:
    def helper (self, nums):
        keeper = []
        if len(nums) == 1:
            return [[], nums]
        subsets = self.helper(nums[1:])
        for subset in subsets:
            if [nums[0]] + subset not in keeper:
                keeper.append([nums[0]] + subset)
            if subset not in keeper:
                keeper.append(subset)
        return keeper
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        return self.helper(nums)

        