class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = "+-*/"
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in operands:
                stack.append(int(tokens[i]))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                total = 0
                if tokens[i] == "+":
                    total = val2 + val1
                elif tokens[i] == "*":
                    total = val2 * val1
                elif tokens[i] == "-":
                    total = val2 - val1
                elif tokens[i] == "/":
                    total = val2 / val1
                    total = int(total)
                stack.append(total)
                print(stack)
        return stack[-1]