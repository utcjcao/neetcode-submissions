class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if u can find min index, than that gives you both the ranges for 
        # both rotated sides. dependingin on where the target fits, you can just bin search tehre
        mi = -1
        cur = float("inf")
        l, r = 0, len(nums)-1
        while (l<=r):
            m = (l+r)//2
            if (nums[m] < cur):
                cur = nums[m]
                mi = m
            if (nums[m] > nums[r]):
                l = m+1
            else:
                r = m-1
        if (nums[0] <= target <= nums[mi-1]):
            l, r = 0, mi-1
            if r == -1: 
                r = len(nums)-1
            print(l, r)
            while l <= r:
                m = (l+r)//2
                if (nums[m] > target):
                    r = m-1
                elif (nums[m] <target):
                    l = m+1
                else:
                    return m
            return -1
        else:
            print('second')
            l, r = mi, len(nums)-1
            while l <= r:
                m = (l+r)//2
                if (nums[m] > target):
                    r = m-1
                elif (nums[m] <target):
                    l = m+1
                else:
                    return m
            return -1