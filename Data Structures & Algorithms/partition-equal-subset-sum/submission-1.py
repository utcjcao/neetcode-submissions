class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # brute force, we can generate all possible subsets and check if there exists a diff such that == 0

        # maybe if we know all the possible partition diffs of i -1, when we intro 
        # the value at i, we can use that to infer if a zero diff is possible? 

        # can we keep track of all the possible partition diffs at i-1? 

        prev = set()
        prev.add(nums[0])

        for i in range(1, len(nums)):
            # we intro val = nums[i]

            val = nums[i]
            new = set()

            for q in prev:
                new.add(q+val)
                new.add(q-val)

            prev = new
        print(prev)
        return 0 in prev

            # for every diff in prev, we know we can have either diff + val, or diff - val (we are basically in)
        