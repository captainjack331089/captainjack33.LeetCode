"""
566. Reshape the Matrix
Category: Array
Difficulty: Easy
"""
"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.

"""
"""
思路：这道题其实就是给定(M x N)的矩阵，要求改成 r x c 的矩阵，
"""

class Solution(object):
    def reshapeTheMatrix(self, nums, r, c):
        row = len(nums)
        column =len(nums[0])

        if row * column != r * c:
            return nums

        new_row = []
        new_matrix = []

        for i in range(row):
            for j in range(column):
                new_row.append(nums[i][j])
                if len(new_row) == c: #注意点： 矩阵的长度其实就等于矩阵的列数
                    new_matrix.append(new_row)
                    new_row = []
        return new_matrix

if __name__ == "__main__":
    print(Solution().reshapeTheMatrix([[1,2],[3,4]], 1, 4))
    print(Solution().reshapeTheMatrix([[1, 2], [3, 4]], 2, 4))