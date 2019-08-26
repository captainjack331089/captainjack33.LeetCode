"""
661. Image Smoother
Category: Array
Difficulty: Easy

"""

"""
Given a 2D integer matrix M representing the gray scale of an image, 
you need to design a smoother to make the gray scale of each cell becomes the 
average gray scale (rounding down) of all the 8 surrounding cells and itself. 
If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].

思路：
这道题考验基本功，方法就是
建立新矩阵，
遍历矩阵， 
把符合边界条件的每个cell的floor值算出来放进新的矩阵
"""
import math
class Solution(object):
    def imageSmoother(self, M):
        row = len(M)
        col = len(M[0])
        new_M = [[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                sum = 0
                count = 0
                for a in [0,-1, 1]:
                    for b in [0, -1, 1]:
                        new_row = i + a
                        new_col = j + b
                        if 0 <= new_row < row and 0 <= new_col < col:
                            sum += M[new_row][new_col]
                            count += 1
                new_M[i][j] = math.floor(sum/count)
        return new_M

if __name__ == "__main__":
    print(Solution().imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))

