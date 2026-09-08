class Solution:
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        print(pair)
        for p, s in pair:
            stack.append((target-p)/s)
            if len(stack) >=2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        return len(stack)



             