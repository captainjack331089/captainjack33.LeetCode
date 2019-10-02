"""
447. Number of Boomerangs
Category: Hash Table
Difficulty: Easy
"""
"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""
import collections
class Solution(object):
    def numberOfBoomerangs(self, points):
        result = 0
        for x0,y0 in points:
            lookup = collections.defaultdict(int)
            for x1,y1 in points:
                lookup[(x1-x0)**2 + (y1-y0)**2] += 1
            for i in lookup:
                result += lookup[i] * (lookup[i] - 1)
        return result


points = [[0,0],[1,0],[2,0], [3,0], [6,0], [7,0], [8,0]]
print(Solution().numberOfBoomerangs(points))