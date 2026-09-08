class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        ans[0][0] = 1
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if (j-coins[i] >= 0):
                    ans[i][j] += ans[i][j-coins[i]]
                    ans[i][j] += sum([ans[k][j-coins[i]] for k in range(0, i)])
        for l in ans:
            print(l)
        return sum([ans[k][-1] for k in range(len(coins))])