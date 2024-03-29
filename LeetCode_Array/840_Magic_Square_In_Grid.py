"""
840: Magic Square in Grid
Category: Array
Difficulty: Easy
"""
"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15

"""

class Solution(object):
    def numMagicSquaresInside(self,grid):
        row = len(grid)
        col = len(grid[0])
        result = 0

        def isMagic(a,b,c,d,e,f,g,h,i):
            return (set([a,b,c,d,e,f,g,h,i]) == set(range(1,10)) and (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15))

        for i in range(row-1):
            for j in range(col-1):
                if grid[i][j] != 5:
                    continue
                if isMagic(grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],grid[i][j-1],grid[i][j],grid[i][j+1],grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1]):
                    result +=1
        return result

if __name__ == "__main__":
    print(Solution().numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))