"""
463. Island Perimeter
Category: Hash Table
Difficulty: Easy
"""
"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


"""
class Solution(object):
    def islandPerimeter(self,grid):
        count = 0
        neighbor = 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count += 1
                    if row < rows - 1:
                        if grid[row+1][col] == 1:
                            neighbor += 1
                    if col < cols - 1:
                        if grid[row][col+1] == 1:
                            neighbor += 1

        return count*4 - neighbor*2
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
if __name__ == "__main__":
    print(Solution().islandPerimeter(grid))