class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        reachable = [False] * (len(s)+1)
        reachable[0] = True
        for i in range(1, len(s)+1):
            for word in wordDict:
                if (i - len(word) < 0):
                    continue
                if (reachable[i-len(word)] and s[i-len(word):i] == word):
                    reachable[i] = True

        return reachable[-1]