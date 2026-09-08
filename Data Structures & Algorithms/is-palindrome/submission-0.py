class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = "".join(s.split()).lower()
        temp= ""
        for c in q:
            if c.isalnum():
                temp += c
        i = 0
        print(temp)
        for i in range(len(temp)//2):
            if temp[i] != temp[-(i+1)]:
                return False
        return True