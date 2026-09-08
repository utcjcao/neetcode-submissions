class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        ans = [-1] * (amount+1)
        ans[0] = 0
        for i in range(len(ans)):
            for coin in coins:
                if i-coin >= 0 and ans[i-coin] >= 0:
                    if ans[i] > 0:
                        ans[i] = min(ans[i-coin] + 1, ans[i])
                    else:
                        ans[i] = ans[i-coin] + 1
                            
        print(ans)
        if ans[-1] == 0: return -1
        return ans[-1]