class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(s) != 0:
                while len(s) > 0 and temperatures[s[-1]] < temperatures[i]:
                    j = s.pop()
                    ans[j] = i-j
            s.append(i)
        return ans
                
            