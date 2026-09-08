class Solution:
    
       
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        a  = []
        def backtrack (subset, i):
            if i == len(nums):
                a.append(subset[::])
                return
            
            subset.append(nums[i])
            backtrack(subset, i+1)
            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(subset, i+1)
        backtrack([],0)
        return a

        