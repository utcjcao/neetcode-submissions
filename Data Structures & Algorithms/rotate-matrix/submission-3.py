class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)-1

        for i in range(len(matrix)//2):
            last = len(matrix) - 1 - i
            for d in range(l):
                matrix[i][i+d], matrix[i+d][last], matrix[last][last-d], matrix[last-d][i] = matrix[last-d][i], matrix[i][i+d], matrix[i+d][last], matrix[last][last-d]
            l-=2

