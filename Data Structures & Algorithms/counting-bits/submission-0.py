class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            n, c = i, 0
            while n > 0:
                if n & 1 == 1:
                    c += 1
                n = n >> 1
            ans.append(c)
        return ans
