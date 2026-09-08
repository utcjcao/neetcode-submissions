class Solution:
    def isHappy(self, n: int) -> bool:
        def summer(n):
            total = 0
            while (n!=0):
                val = (n%10)*(n%10)
                total += val
                n = n//10
            return total
        seen = [n]
        new = summer(n)
        while (new != 1 and new not in seen):
            seen.append(new)
            new = summer(new)
        return new == 1
