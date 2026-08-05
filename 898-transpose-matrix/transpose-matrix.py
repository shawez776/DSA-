class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])

        result = [[0]* row for _ in range(col)]
        for i in range (0,row):
            for j in range(0,col):
                result[j][i] = matrix[i][j]
        return result 