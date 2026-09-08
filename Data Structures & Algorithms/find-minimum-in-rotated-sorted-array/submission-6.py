

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        mid = 0
        cur = float("inf")
        while start < end:
            mid = start + (end-start)//2
            cur = min(cur, nums[mid])
            if nums[mid] > nums[end]:
                start = mid+1 
            else:
                end = mid-1 
            
        return min(cur, nums[start])

