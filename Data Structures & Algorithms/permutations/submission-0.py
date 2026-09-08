class Solution:
    def bfs(self, nums):
        if len(nums) == 1:
            return [nums]
        ans = []
        for i in range(len(nums)):
            q = [n for n in nums]
            new = q.pop(i)
            print('q', q)
            for n in self.bfs(q):
                ans.append([new] + n)
        return ans
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.bfs(nums)