class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        flag = False
        for a, b in intervals:
            if (newInterval[0] <= a <= newInterval[1] or newInterval[0] <= b <= newInterval[1] or a <= newInterval[0] <= b or a <= newInterval[1] <= b):
                newInterval[0] = min(newInterval[0], a)
                newInterval[1] = max(newInterval[1], b)
            else:
                ans.append([a,b])
        
        flag = False

        for i, intl in enumerate(ans):
            if newInterval[1] < intl[0]:
                ans.insert(i, newInterval)
                flag = True
                break

        if (not flag):
            ans.append(newInterval)

        return ans
        
        