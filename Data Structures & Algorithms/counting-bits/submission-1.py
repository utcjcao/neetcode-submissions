class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        look_back = 1
        for i in range(1, n+1):
            if i == look_back * 2:
                look_back *= 2
            ans[i] = ans[i-look_back]+1

        return ans
