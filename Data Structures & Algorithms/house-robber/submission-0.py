class Solution:
    def memo(self, nums, i, included, notIncluded):
        if i == 0:
            included[i], notIncluded[i] = nums[i], 0
        elif i == 1:
            included[i], notIncluded[i] = notIncluded[i-1] + nums[i], included[i-1]
        else:
            included[i] = nums[i] + max(notIncluded[i-1], included[i-2])
            notIncluded[i] = max(notIncluded[i-1], included[i-1])
        
    def rob(self, nums: List[int]) -> int:
        included, notIncluded = {}, {}
        for i in range(len(nums)):
            self.memo(nums, i, included, notIncluded)
        return max(included[len(nums)-1], notIncluded[len(nums)-1])