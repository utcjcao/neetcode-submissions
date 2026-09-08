class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        bottom, top = 0, len(nums)-1
        while bottom <= top:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                top = mid  - 1
            else: 
                bottom = mid + 1
            mid = (bottom + top)//2
        return -1