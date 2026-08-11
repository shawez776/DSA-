from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        
        # Initialize tracking arrays
        rowtrack = [0 for _ in range(r)]
        coltrack = [0 for _ in range(c)]
        
        # First pass: record the positions of zeros
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    rowtrack[i] = "-1"
                    coltrack[j] = "-1"
                    
        # Second pass: update the matrix elements based on tracking arrays
        for i in range(0, r):
            for j in range(0, c):
                if rowtrack[i] == "-1" or coltrack[j] == "-1":
                    matrix[i][j] = 0
