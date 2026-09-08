class Solution:
    cache = {}
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1] or len(s)==1:
            return s
        elif s in self.cache:
            return self.cache[s]
        else:
            s1 = Solution()
            s2 = Solution()
            s1_sol = s1.longestPalindrome(s[1:])
            s2_sol = s2.longestPalindrome(s[:len(s)-1])
            if len(s1_sol) >= len(s2_sol):
                self.cache[s] = s1_sol
                return s1_sol
            else:
                self.cache[s] = s2_sol
                return s2_sol
        