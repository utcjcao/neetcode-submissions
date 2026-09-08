class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        s = 0
        res = 0
        for i in range(len(gas)):
            s += gas[i]-cost[i]
            if s < 0:
                s = 0
                res = i+1
        return res