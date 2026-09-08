class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bot, top = 0, len(matrix) - 1
        mid = (bot + top)//2
        while top-bot > 1:
            val = matrix[mid][0]
            if val == target:
                return True
            elif val > target:
                top = mid
            else:
                bot = mid
            mid = (bot + top)//2 
        arr = matrix[bot] + matrix[top] 
        nbot, ntop = 0, len(arr) - 1
        mid = (nbot+ntop)//2
        while ntop >= nbot:
            val = arr[mid]
            if val == target:
                return True
            elif val > target:
                ntop = mid -1 
            else:
                nbot = mid + 1
            mid = (ntop+nbot)//2
        return False