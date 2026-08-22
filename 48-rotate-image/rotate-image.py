class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #submitted by noor
        """
        Do not return anything, modify matrix in-place instead.
        """
        #optimal solution subbmitd by noor
        #first do the transpose then reverse the list
        n = len(matrix)
        for i in range(0,n-1):
            for j in range(i+1, n):
                matrix[i][j] ,matrix[j][i] = matrix[j][i] ,matrix[i][j]

        for  i in range(0,n):
            matrix[i].reverse()