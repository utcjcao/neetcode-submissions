class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, i = 0, 0
        while i < len(nums)-1:
            m = 0
            q = i
            for j in range(1, nums[i]+1):
                if i+j >= len(nums)-1:
                    q = len(nums)
                    break
                else:
                    if nums[i+j]+i+j>=m:
                        m = nums[i+j]+i+j
                        q = i+j
            i = q
            jumps += 1
        return jumps