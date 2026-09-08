class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        for key, val in d.items():
            bucket[val].append(key)
        ans = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
