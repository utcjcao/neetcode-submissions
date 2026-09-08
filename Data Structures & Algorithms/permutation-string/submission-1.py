class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sol = [0]*26
        for c in s1:
            i = ord(c)-ord('a')
            sol[i] += 1
        cur = [0] * 26
        total = 0
        prev = 0
        for c in s2:
            i = ord(c)-ord('a')
            # what are the cases:
            # 1. we hit a char in the substring

            # 2. char does not fit into what we have
            # have to increment up until it fits

            cur[i] += 1
            while cur[i] > sol[i]:
                j = ord(s2[prev])-ord('a')
                cur[j] -= 1
                prev += 1
            if (sum(cur) == len(s1)):
                return True
        return False