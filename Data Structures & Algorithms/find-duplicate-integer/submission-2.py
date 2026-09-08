class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f, s = nums[0], nums[0]
        while (True):
            f = nums[nums[f]]
            s = nums[s]
            print(f, s)
            if (f==s):
                break
        s2 = nums[0]
        while (s2 != s):
            s2 = nums[s2]
            s = nums[s]
        return s2
