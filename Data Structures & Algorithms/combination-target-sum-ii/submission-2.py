class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)
        def s(index, target, so_far):
            if index > len(candidates):
                return
            if target == 0:
                ans.append(so_far)
                    
                return
            else:
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i - 1]:
                        continue
                    t2 = target - candidates[i]
                    so_far.append(candidates[i])
                    if t2 >= 0:
                        s(i+1, t2, so_far.copy())
                    so_far.pop()
                return

        s(0, target, [])
        return ans