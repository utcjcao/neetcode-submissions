class Solution:
    def climbStairs(self, n: int) -> int:
        def addSteps(remaining: int):
            total = 0
            if remaining <= 1:
                total += 1
            elif remaining >= 2:
                total += addSteps(remaining - 1) + addSteps(remaining - 2)
            return total
        return addSteps(n)
        