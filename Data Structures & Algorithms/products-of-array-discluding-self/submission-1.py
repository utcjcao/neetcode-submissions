class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input: array of integers 
        # output: array of integers of length nums, where each value is the total
        # product of all elements except the one at the current index

        # [1,2,3]
        # [6,3,2]

        # [-1, 2, -3]
        # [-6, 3, -2]

        # [0, 3, 4]
        # [12, 0, 0]

        # [0, 3, 4, 0]
        # [0, 0, 0, 0]

        zero_c = nums.count(0)
        if (zero_c > 1):
            return [0 for i in range(len(nums))]
        if (zero_c == 1):
            product = 1
            zero_i = 0
            for i in range(len(nums)):
                n = nums[i]
                if n != 0:
                    product *= n
                else:
                    zero_i = i
            ans = [0 for i in range(len(nums))]
            ans[zero_i] = product
            return ans
        
        product = 1
        for i in range(len(nums)):
            n = nums[i]
            if n != 0:
                product *= n
        ans = []
        for i in range(len(nums)):
            ans.append(product // nums[i])
        return ans


        # we'll count all the zeros
        # if zero count > 1:
        # return an array of len n of just 0
        # if zero count == 1:
        # return an array of 0s, except at the index of 0, where we'll have the product of
        # zero count == 0
        # if we have no zeros, then we'll output the actual output array
        # found the total product
        # and for each elem in output, we'll have total product/elem in array
