"""
867. Transpose Matrix
Category: Array
Difficulty: Easy
"""
"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000

"""
A = [[1,2,3],[4,5,6]]
class Solution(object):
    def transpose(self,A):
        row = len(A)
        col = len(A[0])
        new_A = [[0]*row for _ in range(col)]

        for i in range(row):
            for j in range(col):
                new_A[j][i] = A[i][j]
        return new_A

if __name__ == "__main__":
    print(Solution().transpose(A))
