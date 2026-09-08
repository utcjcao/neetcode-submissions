class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        for i in range(1, pow(2,(n*2))):
            counter = 0
            k = format(i, "0" + str(2 * n) +'b')  
            # print(k)
            for q in k:
                if q == "1":
                    counter += 1
                else:
                    counter -= 1
                if counter < 0:
                    break
            if counter == 0:
                print('s')
                s = ""
                for q in k:
                    if q == "1":
                        s +="("
                    else:
                        s += ")"
                ans.append(s)
        return ans