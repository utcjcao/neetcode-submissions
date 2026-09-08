class Solution:

    def helper (self, nums):
        keeper = []
        if len(nums) == 1:
            return [[], nums]
        subsets = self.helper(nums[1:])
        for subset in subsets:
            keeper.append([nums[0]] + subset)
            keeper.append(subset)
        return keeper
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums)