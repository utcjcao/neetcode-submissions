class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        for i in range(len(num1)-1, -1, -1):
            val1 = ord(num1[i])-ord('0');
            total = 0
            for j in range(len(num2)-1, -1, -1):
                val2 = ord(num2[j])-ord('0')
                total += val2 * val1 * pow(10, len(num2)-1-j)
            print(total)
            ans += total * pow(10, len(num1)-1-i)
        return str(ans)

                 