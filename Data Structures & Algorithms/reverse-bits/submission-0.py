class Solution:
    def reverseBits(self, n: int) -> int:
        total = 0
        cur_am = 1
        for i in range(32):
            have_1 =  (n & 1)
            total += have_1
            if i != 31: total *= 2
            n = n >> 1
        return total
        