class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start = nums[:]
        end = nums[:]
        for i in range(1, len(nums)):
            start[i] *= start[i-1]
        for i in range(len(nums)-2, -1, -1):
            end[i] *= end[i+1]
        print(start, end)
        output = [1] * len(nums)
        for i in range(len(nums)):
            left, right = 1, 1
            if i-1 >= 0:
                left = start[i-1]
            if i+1 < len(nums):
                right = end[i+1]
            output[i] *= left * right
        return output