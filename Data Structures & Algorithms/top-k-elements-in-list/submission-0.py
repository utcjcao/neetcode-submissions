class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n]+=1
        ans = [(d[n], n) for n in d]
        ans = sorted(ans, reverse=True)
        return [ans[i][1] for i in range(k)]
