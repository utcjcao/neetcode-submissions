class Solution:
    def ids(self, string):
        alpha = [0] * 26
        for c in string:
            alpha[ord(c)-97] += 1
        return str(alpha)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = {}
        for s in strs:
            i = self.ids(s)
            print(i)
            if i not in g:
                g[i] = []
            g[i].append(s)
        return [g[ans] for ans in g]