"""
766. Toeplitz Matrix
Category: Array
Difficulty: Easy

"""
"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

"""
class Solution(object):
    def isToeplitzMatrix1(self,matrix):
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if i >0  and j >0 and matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

    def isToeplitzMatrix2(self,matrix):
        for row in range(len(matrix)-1):
            if matrix[row+1][1:] == matrix[row][:-1]:
                return True
        return False

if __name__ == "__main__":
    print(Solution().isToeplitzMatrix2([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
