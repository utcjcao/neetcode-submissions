class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # input integers, 1 300
        # output: yes

        n = len(nums)

        dp = [[None for i in range(n+1)] for j in range(n+1)]

        def recurse(l, r):
            if dp[l][r] is not None:
                return

            left_edge = nums[l-1] if l-1 >= 0 else 1
            right_edge = nums[r] if r < n else 1

            if r - l == 0:
                dp[l][r] = 0
            elif r - l == 1:
                dp[l][r] = left_edge * nums[l] * right_edge

            best_so_far = 0
            
            for i in range(l, r):
                recurse(l, i)
                recurse(i+1, r)

                middle = left_edge * nums[i] * right_edge
                total = dp[l][i] + middle + dp[i+1][r]

                best_so_far = max(best_so_far, total)

            dp[l][r] = best_so_far
        
        recurse(0, n)
        return dp[0][n]


